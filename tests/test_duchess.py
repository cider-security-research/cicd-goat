from git import Repo
from conftest import GITEA_GIT_BASE, OWNER, REPOSITORIES_DIR
from pathlib import Path

FLAG = 'pypi-AgEIcHlwaS5vcmcCJGNmNTI5MjkyLWYxYWMtNDEwYS04OTBjLWE4YzNjNGY1ZTBiZAACJXsicGVybWlzc2lvbnMiOiAidXNlciI' \
       'sICJ2ZXJzaW9uIjogMX0AAAYg7T5yHIewxGoh-3st7anbMSCoGhb-U3HnzHAFLHBLNBY'


def test_duchess(gitea_client):
    repo = Repo.clone_from(f'{GITEA_GIT_BASE}/{OWNER}/duchess.git',
                           REPOSITORIES_DIR / 'duchess',
                           branch='master')
    assert FLAG in repo.git.show(f'43f216c2268a94ff03e5400cd4ca7a11243821b0:.pypirc')
