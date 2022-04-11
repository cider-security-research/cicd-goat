from pathlib import Path
import pytest
import requests
from requests.auth import HTTPBasicAuth
import shutil
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import NoBuildData
from time import sleep, time
from uuid import uuid4

# import logging
# import http.client

OWNER = 'Wonderland'
REPOSITORIES_DIR = Path(__file__).resolve().parent / 'repositories'
GITEA_GIT_BASE = 'http://thealice:thealice@localhost:3000'
RUNNING_BUILD_TIMEOUT = 120
START_BUILD_TIMEOUT = 30
FORK_ORG = 'test'
GITEA_BASE = 'http://localhost:3000'
GITEA_API_BASE = f'{GITEA_BASE}/api/v1'


# logging.basicConfig(level=logging.DEBUG)
# http.client.HTTPConnection.debuglevel = 5


class GiteaApiClient:
    token = requests.post(f'{GITEA_API_BASE}/users/thealice/tokens',
                          auth=HTTPBasicAuth('thealice', 'thealice'),
                          json={'name': str(uuid4())}).json()['sha1']

    def post(self, endpoint, data=None, json=None, **kwargs):
        return requests.post(f'{GITEA_API_BASE}{endpoint}',
                             data=data, json=json, headers={'Authorization': f'token {self.token}'}, **kwargs)

    def get(self, endpoint, params=None, **kwargs):
        return requests.get(f'{GITEA_API_BASE}{endpoint}',
                            params=params, headers={'Authorization': f'token {self.token}'}, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return requests.put(f'{GITEA_API_BASE}{endpoint}',
                            data=data, headers={'Authorization': f'token {self.token}'}, **kwargs)

    def create_fork(self, owner, repo):
        res = self.get('/orgs')
        assert res.status_code == 200
        for org in res.json():
            if FORK_ORG in org['username']:
                break
        else:
            res = self.post('/orgs',
                            json={"full_name": "test", 'username': 'test', 'visibility': 'public'})
            assert res.status_code == 201
        res = self.get('/orgs/test/repos')
        for repo_dict in res.json():
            if repo == repo_dict['name']:
                return True
        else:
            res = self.post(f'/repos/{owner}/{repo}/forks',
                            json={"organization": FORK_ORG})
            if res.status_code == 202:
                return True
            print(res.status_code, res.content)
            return False


class JenkinsClient(Jenkins):
    def post(self, endpoint, data=None, **kwargs):
        return self.requester.post_url(f'{self.baseurl}{endpoint}', data=data, timeout=120, **kwargs)

    def get(self, endpoint, **kwargs):
        return self.requester.get_url(f'{self.baseurl}{endpoint}', **kwargs)

    def find_in_last_build_console(self, job_path, string, start_job=True):
        if start_job:
            res = self.post(f'/job/{job_path}/build?delay=0')
            assert res.status_code == 200 or res.status_code == 201

        if '/job/' in job_path:
            job_name = f'{job_path.split("/")[0]}/{job_path.split("/")[-1]}'
        else:
            job_name = job_path

        def search_last_build(job):
            start = time()
            last_build = ''
            while 1:
                if not job.is_queued_or_running():
                    try:
                        last_build = job.get_last_build()
                    except NoBuildData:
                        pass
                    break
                if time() - start > RUNNING_BUILD_TIMEOUT:
                    break
                sleep(1)
            if not last_build:
                try:
                    last_build = job.get_last_build()
                except NoBuildData:
                    return False, ''
            if string in last_build.get_console():
                return True, ''
            return False, last_build.get_console()

        start_time = time()
        while 1:
            results = [search_last_build(job) for name, job in self.get_jobs()
                       if job_name in name]
            if [result for result, console in results if results]:
                return True
            if time() - start_time > START_BUILD_TIMEOUT:
                break
        print('--------------------------\n'.join([console for result, console in results if console]))
        return False


@pytest.fixture()
def gitea_client():
    return GiteaApiClient()


@pytest.fixture()
def jenkins_client():
    return JenkinsClient('http://localhost:9090', username='alice', password='alice', useCrumb=True)


try:
    shutil.rmtree('tests/repositories')
except FileNotFoundError:
    pass
