from git import Repo
from base64 import b64encode
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER
from utils import branch_and_replace_file_content
from uuid import uuid4
from time import sleep

JOB_NAME = 'mock-turtle'
WITH_CREDENTIALS = """withCredentials([usernamePassword(credentialsId: 'flag10', usernameVariable: 'USERNAME', passwordVariable: 'TOKEN')]) {
                    sh 'echo $TOKEN | base64'
                }
                withCredentials"""
REMOVE_WORDS = 'Eel is a little Python library for making simple Electron-like offline HTML/JS GUI apps, with'


def test_mock_turtle(gitea_client, jenkins_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/{JOB_NAME}.git',
                           REPOSITORIES_DIR / JOB_NAME,
                           branch='main')
    new_branch_name = uuid4().hex
    replace_tuples = [('1.0.11', '1.0.12')]
    branch_and_replace_file_content(repo, new_branch_name, 'version', replace_tuples, commit=False, push=False)
    replace_tuples = [(REMOVE_WORDS, '')]
    branch_and_replace_file_content(repo, new_branch_name, 'README.md', replace_tuples, commit=False, push=False)
    replace_tuples = [('withCredentials', WITH_CREDENTIALS)]
    branch_and_replace_file_content(repo, new_branch_name, 'Jenkinsfile', replace_tuples)
    res = gitea_client.post(f'/repos/{OWNER}/{JOB_NAME}/pulls',
                            json={'head': new_branch_name, 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    jenkins_client.build_job('mock-turtle/main')
    sleep(5)
    flag = b64encode('D54734AB-7B83-4931-A9BB-171476101FDF'.encode()).decode()
    assert jenkins_client.find_in_last_build_console('main', flag, job_path=f'{JOB_NAME}/job/')
