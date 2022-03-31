from git import Repo
from base64 import b64encode
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER, FORK_ORG
from utils import branch_and_replace_file_content
from subprocess import run
from pathlib import Path

COV_ORG = 'Cov'
COV_JOB_NAME = 'march-hare'
CLIENT_JOB_NAME = 'dormouse'
PART_PRIVATE_KEY = 'b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn'
TESTS_PATH = Path(__file__).parent
SSH_CMD = f'scp -o StrictHostKeyChecking=no -P 2222 -i {TESTS_PATH}/data/march_and_dormouse/key ' \
          f'{TESTS_PATH}/data/march_and_dormouse/reportcov.sh ' \
          'root@localhost:/var/www/localhost/htdocs'
CHMOD_CMD = f'chmod 400 {TESTS_PATH}/data/march_and_dormouse/key'


def test_march_and_dormouse(gitea_client, jenkins_client):
    assert gitea_client.create_fork(COV_ORG, COV_JOB_NAME)
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{FORK_ORG}/{COV_JOB_NAME}.git',
                           REPOSITORIES_DIR / COV_JOB_NAME,
                           branch='main')
    replace_tuples = [('docs', 'bok')]
    branch_and_replace_file_content(repo, 'main', 'README.rst', replace_tuples)
    res = gitea_client.post(f'/repos/{COV_ORG}/{COV_JOB_NAME}/pulls',
                            json={'head': f'{FORK_ORG}:main', 'base': 'main', 'title': '`env`'})
    assert res.status_code == 201
    assert jenkins_client.find_in_last_build_console(COV_JOB_NAME, PART_PRIVATE_KEY, start_job=False)
    assert res.status_code == 201
    result = run(CHMOD_CMD, capture_output=True, text=True, shell=True)
    assert not result.stderr
    result = run(SSH_CMD, capture_output=True, text=True, shell=True)
    print(result.stderr)
    flag = b64encode('31350FBC-A959-4B4B-A8BD-DCA7AC9248A6'.encode()).decode()
    assert jenkins_client.find_in_last_build_console(CLIENT_JOB_NAME, flag)
