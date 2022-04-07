from git import Repo
from base64 import b64encode
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER
from utils import branch_and_replace_file_content
from uuid import uuid4
from time import sleep

REPO_NAME = 'mock-turtle'
WITH_CREDENTIALS = """withCredentials([usernamePassword(credentialsId: 'flag10', usernameVariable: 'USERNAME', passwordVariable: 'TOKEN')]) {
                    sh 'echo $TOKEN | base64'
                }
                withCredentials"""
REMOVE_WORDS = 'Eel is a little Python library for making simple Electron-like offline HTML/JS GUI apps, with'
JOB_NAME = f'{OWNER.lower()}-{REPO_NAME}'


def test_mock_turtle(gitea_client, jenkins_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/{REPO_NAME}.git',
                           REPOSITORIES_DIR / REPO_NAME,
                           branch='main')
    new_branch_name = uuid4().hex
    replace_tuples = [('1.0.11', '1.0.12')]
    branch_and_replace_file_content(repo, new_branch_name, 'version', replace_tuples, commit=False, push=False)
    replace_tuples = [(REMOVE_WORDS, '')]
    branch_and_replace_file_content(repo, new_branch_name, 'README.md', replace_tuples, commit=False, push=False)
    replace_tuples = [('withCredentials', WITH_CREDENTIALS)]
    branch_and_replace_file_content(repo, new_branch_name, 'Jenkinsfile', replace_tuples)
    res = gitea_client.post(f'/repos/{OWNER}/{REPO_NAME}/pulls',
                            json={'head': new_branch_name, 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    res = jenkins_client.post(f'/job/{JOB_NAME}/build?delay=0')
    assert res.status_code == 200 or res.status_code == 201
    sleep(10)
    flag = b64encode('D54734AB-7B83-4931-A9BB-171476101FDF'.encode()).decode()
    assert jenkins_client.find_in_last_build_console(JOB_NAME, flag)
