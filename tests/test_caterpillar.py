from utils import branch_and_replace_file_content
from conftest import GITEA_GIT_BASE, REPOSITORIES_DIR, OWNER, GITEA_API_BASE
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
ENV_TOKEN = 'a644940c92efe2d1876e16a5d29e6c6d7e199b68'


def test_caterpillar(gitea_client, jenkins_client):
    assert gitea_client.create_fork(OWNER, 'caterpillar')
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/test/caterpillar.git',
                           REPOSITORIES_DIR / 'caterpillar',
                           branch='main')
    new_branch_name = uuid4().hex
    branch_and_replace_file_content(repo, new_branch_name, 'Jenkinsfile', [('virtualenv venv', 'env'),
                                                                           ('pylint', 'echo'),
                                                                           ('pytest', 'true')])
    res = gitea_client.post(f'/repos/{OWNER}/caterpillar/pulls',
                            json={'head': f'test:{new_branch_name}', 'base': 'main', 'title': 'updates'})
    assert res.status_code == 201
    assert jenkins_client.find_in_last_build_console('caterpillar-test', ENV_TOKEN)
    res = gitea_client.get(f'/repos/{OWNER}/caterpillar/contents/Jenkinsfile')
    assert res.status_code == 200
    res = requests.put(f'{GITEA_API_BASE}/repos/{OWNER}/caterpillar/contents/Jenkinsfile',
                       data={'content': JENKINSFILE_CONTENT,
                             'sha': res.json()['sha']},
                       headers={'Authorization': f'token {ENV_TOKEN}'})
    if res.status_code != 200:
        print(res.status_code, res.content)
        assert False
    flag = b64encode('AEB14966-FFC2-4FB0-BF45-CD903B3535DA'.encode()).decode()
    assert jenkins_client.find_in_last_build_console('caterpillar-prod', flag)
