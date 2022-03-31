from git import Repo
from conftest import REPOSITORIES_DIR, GITEA_GIT_BASE, OWNER
from utils import branch_and_replace_file_content, branch_and_write_file
from time import sleep


def test_dodo(gitea_client, jenkins_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/dodo.git',
                           REPOSITORIES_DIR / 'dodo',
                           branch='main')
    replace_tuples = [('acl           = "private"', 'acl           = "public-read"')]
    branch_and_replace_file_content(repo, 'main', 'main.tf', replace_tuples, commit=False, push=False)
    branch_and_write_file(repo, 'main', '.checkov.yaml', 'soft-fail: true\ncheck:\n  - MY_CHECK')
    # Wait for job to trigger
    sleep(61)
    assert jenkins_client.find_in_last_build_console('dodo', 'A62F0E52-7D67-410E-8279-32447ADAD916')
