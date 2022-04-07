from git import Repo
from uuid import uuid4
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER, JenkinsClient
from utils import branch_and_replace_file_content

REPO_NAME = 'cheshire-cat'
JOB_NAME = f'{OWNER.lower()}-{REPO_NAME}'


def test_cheshire_cat(gitea_client, jenkins_client):
    admin_jenkins_client = JenkinsClient('http://localhost:8080', username='admin', password='ciderland5#',
                                         useCrumb=True)
    assert b'Only build jobs with label expressions matching this node' in \
           admin_jenkins_client.get('/computer/(built-in)/configure').content
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/{REPO_NAME}.git',
                           REPOSITORIES_DIR / REPO_NAME,
                           branch='main')
    new_branch_name_one = uuid4().hex
    replace_tuples = [('virtualenv venv', 'cat ~/flag5.txt'),
                      ('pylint', 'echo'),
                      ('pytest', 'true'),
                      ('agent any', "agent {label 'built-in'}")]
    branch_and_replace_file_content(repo, new_branch_name_one, 'Jenkinsfile', replace_tuples)
    res = gitea_client.post(f'/repos/{OWNER}/{REPO_NAME}/pulls',
                            json={'head': new_branch_name_one, 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    assert jenkins_client.find_in_last_build_console(JOB_NAME, '6B31A679-6D70-469D-9F8D-6D6E80B3C29C')

