from git import Repo
from conftest import GITEA_GIT_BASE, OWNER, REPOSITORIES_DIR

FLAG = 'pypi-AgEIcHlwaS5vcmcCJGNmNTI5MjkyLWYxYWMtNDEwYS04OTBjLWE4YzNjNGY1ZTBiZAACJXsicGVybWlzc2lvbnMiOiAidXNlciI' \
       'sICJ2ZXJzaW9uIjogMX0AAAYg7T5yHIewxGoh-3st7anbMSCoGhb-U3HnzHAFLHBLNBY'
JOB_NAME = 'duchess'


def test_duchess(gitea_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/{JOB_NAME}.git',
                           REPOSITORIES_DIR / JOB_NAME,
                           branch='main')
    assert FLAG in repo.git.show(f'43f216c2268a94ff03e5400cd4ca7a11243821b0:.pypirc')
