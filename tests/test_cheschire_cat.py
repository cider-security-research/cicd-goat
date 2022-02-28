from git import Repo
from base64 import b64encode
from uuid import uuid4
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER
from utils import branch_and_replace_file_content, find_in_console


def test_cheshire_cat(gitea_client, jenkins_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/cheshire-cat.git',
                           REPOSITORIES_DIR / 'cheshire-cat',
                           branch='main')
    new_branch_name = uuid4().hex
    replace_tuples = [('agent any', "agent {label 'built-in'}"),
                      ('virtualenv venv', 'cat ~/flag5.txt'),
                      ('pylint', 'echo'),
                      ('pytest', 'true')]
    branch_and_replace_file_content(repo, new_branch_name, 'Jenkinsfile', replace_tuples)
    res = gitea_client.post(f'/repos/{OWNER}/cheshire-cat/pulls',
                            json={'head': new_branch_name, 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    assert find_in_console(jenkins_client, 'cheshire-cat', '6B31A679-6D70-469D-9F8D-6D6E80B3C29C')
