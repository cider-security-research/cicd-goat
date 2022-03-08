from git import Repo
from uuid import uuid4
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER
from utils import branch_and_replace_file_content


def test_cheshire_cat(gitea_client, jenkins_client):
    assert b'Only build jobs with label expressions matching this node' in \
           jenkins_client.get('/computer/(built-in)/configure')
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/cheshire-cat.git',
                           REPOSITORIES_DIR / 'cheshire-cat',
                           branch='main')
    new_branch_name_one = uuid4().hex
    replace_tuples = [('virtualenv venv', 'cat ~/flag5.txt'),
                      ('pylint', 'echo'),
                      ('pytest', 'true'),
                      ('agent any', "agent {label 'built-in'}")]
    branch_and_replace_file_content(repo, new_branch_name_one, 'Jenkinsfile', replace_tuples)
    res = gitea_client.post(f'/repos/{OWNER}/cheshire-cat/pulls',
                            json={'head': new_branch_name_one, 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    assert jenkins_client.find_in_last_build_console('cheshire-cat', '6B31A679-6D70-469D-9F8D-6D6E80B3C29C')

