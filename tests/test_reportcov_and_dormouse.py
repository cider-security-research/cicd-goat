from git import Repo
from base64 import b64encode
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, FORK_ORG, GITEA_BASE, OWNER, JenkinsClient
from utils import branch_and_replace_file_content
from subprocess import run
from pathlib import Path
import requests
from time import sleep

COV_ORG = 'Cov'
COV_REPO_NAME = 'reportcov'
COV_JOB_NAME = f'{COV_ORG.lower()}-{COV_REPO_NAME}'
CLIENT_REPO_NAME = 'dormouse'
CLIENT_JOB_NAME = f'{OWNER.lower()}-{CLIENT_REPO_NAME}'
PART_PRIVATE_KEY = 'b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn'
TESTS_PATH = Path(__file__).parent
SSH_CMD = f'scp -o StrictHostKeyChecking=no -P 2222 -i {TESTS_PATH}/data/reportcov_and_dormouse/key ' \
          f'{TESTS_PATH}/data/reportcov_and_dormouse/reportcov.sh ' \
          'root@localhost:/var/www/localhost/htdocs'
CHMOD_CMD = f'chmod 400 {TESTS_PATH}/data/reportcov_and_dormouse/key'


def test_reportcov_and_dormouse(gitea_client, jenkins_client):
    res = jenkins_client.post(f'/job/{CLIENT_JOB_NAME}/build?delay=0')
    assert res.status_code == 200 or res.status_code == 201
    assert gitea_client.create_fork(COV_ORG, COV_REPO_NAME)
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{FORK_ORG}/{COV_REPO_NAME}.git',
                           REPOSITORIES_DIR / COV_REPO_NAME,
                           branch='main')
    replace_tuples = [('docs', 'bok')]
    branch_and_replace_file_content(repo, 'main', 'README.rst', replace_tuples)
    requests.get(f'{GITEA_BASE}/{COV_ORG}/{COV_REPO_NAME}')
    res = gitea_client.post(f'/repos/{COV_ORG}/{COV_REPO_NAME}/pulls',
                            json={'head': f'{FORK_ORG}:main', 'base': 'main', 'title': '`env`'})
    sleep(20)
    admin_client = JenkinsClient('http://localhost:8080', username='admin', password='ciderland5#', use_crumb=True)
    assert admin_client.find_in_last_build_console(COV_JOB_NAME, PART_PRIVATE_KEY, start_job=False)
    assert res.status_code == 201
    result = run(CHMOD_CMD, capture_output=True, text=True, shell=True)
    assert not result.stderr
    result = run(SSH_CMD, capture_output=True, text=True, shell=True)
    print(result.stderr)
    flag = b64encode('31350FBC-A959-4B4B-A8BD-DCA7AC9248A6'.encode()).decode()
    assert jenkins_client.find_in_last_build_console(f'{CLIENT_JOB_NAME}/job/main', flag)
