from pathlib import Path
import pytest
import requests
from requests.auth import HTTPBasicAuth
import shutil
from jenkinsapi.jenkins import Jenkins
from uuid import uuid4
from jenkinsapi.custom_exceptions import NoBuildData
from time import sleep

GITEA_BASE = 'http://localhost:3000'
GITEA_API_BASE = f'{GITEA_BASE}/api/v1'
OWNER = 'Wonderland'
REPOSITORIES_DIR = Path(__file__).resolve().parent / 'repositories'
GITEA_GIT_BASE = 'http://thealice:thealice@localhost:3000'
BUILD_TIMEOUT = 120


class GiteaApiClient:
    token = requests.post(f'{GITEA_API_BASE}/users/thealice/tokens',
                          auth=HTTPBasicAuth('thealice', 'thealice'),
                          json={'name': str(uuid4())}).json()['sha1']

    @staticmethod
    def post(endpoint, data=None, json=None, **kwargs):
        return requests.post(f'{GITEA_API_BASE}{endpoint}',
                             data=data, json=json, headers={'Authorization': f'token {GiteaApiClient.token}'}, **kwargs)

    @staticmethod
    def get(endpoint, params=None, **kwargs):
        return requests.get(f'{GITEA_API_BASE}{endpoint}',
                            params=params, headers={'Authorization': f'token {GiteaApiClient.token}'}, **kwargs)

    @staticmethod
    def put(endpoint, data=None, **kwargs):
        return requests.put(f'{GITEA_API_BASE}{endpoint}',
                            data=data, headers={'Authorization': f'token {GiteaApiClient.token}'}, **kwargs)

    def create_fork(self, owner, repo):
        res = self.get('/orgs')
        assert res.status_code == 200
        for org in res.json():
            if 'test' in org['username']:
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
                            json={"organization": "test"})
            if res.status_code == 202:
                return True
            return False


class JenkinsClient(Jenkins):
    def post(self, endpoint, data=None, **kwargs):
        return self.requester.post_url(f'{self.baseurl}{endpoint}', data=data, timeout=120, **kwargs)

    def get(self, endpoint, **kwargs):
        return self.requester.get_url(f'{self.baseurl}{endpoint}', **kwargs)

    def find_in_last_build_console(self, job_name, string):
        res = self.post(f'/job/{job_name}/build?delay=0')
        assert res.status_code == 200
        sleep(5)
        consoles = []
        for tmp_job_name, job_instance in self.get_jobs():
            if job_name in tmp_job_name:
                for i in range(BUILD_TIMEOUT):
                    try:
                        last_build = job_instance.get_last_build()
                        if not job_instance.is_queued_or_running():
                            break
                        raise NoBuildData
                    except NoBuildData:
                        sleep(1)
                else:
                    raise TimeoutError(f'{job_name} job is running for too long')
                if string in last_build.get_console():
                    return True
                consoles.append(last_build.get_console())
        else:
            print('----------\n'.join(consoles))
            return False


@pytest.fixture()
def gitea_client():
    return GiteaApiClient()


@pytest.fixture()
def jenkins_client():
    return JenkinsClient('http://localhost:8080', username='admin', password='ciderland5#', useCrumb=True)


try:
    shutil.rmtree('tests/repositories')
except FileNotFoundError:
    pass
client = JenkinsClient('http://localhost:8080', username='admin', password='ciderland5#', useCrumb=True)

checks = 0
timeout = 0
while checks < 10 and timeout < BUILD_TIMEOUT:
    queue_json = client.get('/queue/api/json').json()
    if not queue_json['items']:
        checks += 1
    timeout += 1
    sleep(1)
