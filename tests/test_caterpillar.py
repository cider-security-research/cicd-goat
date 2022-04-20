from utils import branch_and_replace_file_content
from conftest import GITEA_GIT_BASE, REPOSITORIES_DIR, OWNER, GITEA_API_BASE, FORK_ORG
from git import Repo
from uuid import uuid4
from base64 import b64encode
import requests

JENKINSFILE_CONTENT = "cGlwZWxpbmUgewogICAgYWdlbnQgYW55CiAgICBzdGFnZXMgewogICAgICAgIHN0YWdlKCdzdGVwMScpIHsKICAgIC" \
                      "AgICAgICAgc3RlcHMgewogICAgICAgICAgICAgICAgc2ggJ2VudicKICAgICAgICAgICAgfQogICAgICAgIH0KICAg" \
                      "ICAgICBzdGFnZSgnc3RlcDInKSB7CiAgICAgICAgICAgIHN0ZXBzIHsKICAgICAgICAgICAgICAgIHdpdGhDcmVkZW" \
                      "50aWFscyhbdXNlcm5hbWVQYXNzd29yZChjcmVkZW50aWFsc0lkOiAnZmxhZzInLCB1c2VybmFtZVZhcmlhYmxlOiA" \
                      "nVVNFUk5BTUUnLCBwYXNzd29yZFZhcmlhYmxlOiAnRkxBRzInKV0pIHsKICAgICAgICAgICAgICAgIHNoICdlY2hv" \
                      "ICRGTEFHMiB8IGJhc2U2NCcKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgIAogICAgICAgICAgICB9C" \
                      "iAgICAgICAgfQogICAgfQp9"
ENV_TOKEN = '5d3ed5564341d5060c8524c41fe03507e296ca46'
REPO_NAME = 'caterpillar'
JOB_NAME = f'{OWNER.lower()}-{REPO_NAME}'


def test_caterpillar(gitea_client, jenkins_client):
    assert gitea_client.create_fork(OWNER, REPO_NAME)
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{FORK_ORG}/{REPO_NAME}.git',
                           REPOSITORIES_DIR / REPO_NAME,
                           branch='main')
    new_branch_name = uuid4().hex
    branch_and_replace_file_content(repo, new_branch_name, 'Jenkinsfile', [('virtualenv venv', 'env'),
                                                                           ('pylint', 'echo'),
                                                                           ('pytest', 'true')])
    res = gitea_client.post(f'/repos/{OWNER}/{REPO_NAME}/pulls',
                            json={'head': f'{FORK_ORG}:{new_branch_name}', 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    assert jenkins_client.find_in_last_build_console(f'{JOB_NAME}-test', ENV_TOKEN)
    res = gitea_client.get(f'/repos/{OWNER}/{REPO_NAME}/contents/Jenkinsfile')
    assert res.status_code == 200
    res = requests.put(f'{GITEA_API_BASE}/repos/{OWNER}/{REPO_NAME}/contents/Jenkinsfile',
                       data={'content': JENKINSFILE_CONTENT,
                             'sha': res.json()['sha']},
                       headers={'Authorization': f'token {ENV_TOKEN}'})
    if res.status_code != 200:
        print(res.status_code, res.content)
        assert False
    flag = b64encode('AEB14966-FFC2-4FB0-BF45-CD903B3535DA'.encode()).decode()
    assert jenkins_client.find_in_last_build_console(f'{JOB_NAME}-prod', flag)
