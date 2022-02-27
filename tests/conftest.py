from pathlib import Path

import pytest
import requests
from requests.auth import HTTPBasicAuth
import shutil
from jenkinsapi.jenkins import Jenkins
from uuid import uuid4

GITEA_BASE = 'http://localhost:3000'
GITEA_API_BASE = f'{GITEA_BASE}/api/v1'
OWNER = 'Wonderland'
REPOSITORIES_DIR = Path(__file__).resolve().parent / 'repositories'
GITEA_GIT_BASE = 'http://thealice:thealice@localhost:3000'


class GiteaApiClient:
    token = requests.post(f'{GITEA_API_BASE}/users/thealice/tokens',
                          auth=HTTPBasicAuth('thealice', 'thealice'),
                          json={'name': str(uuid4())}).json()['sha1']

    @staticmethod
    def post(endpoint, data=None, json=None, **kwargs):
        return requests.post(f'{GITEA_API_BASE}{endpoint}',
                             data=data, json=json, headers={'Authorization': f'token {GiteaApiClient.token}'}, **kwargs)

    @staticmethod
    def get(endpoint, params=None, **kwargs):
        return requests.get(f'{GITEA_API_BASE}{endpoint}',
                            params=params, headers={'Authorization': f'token {GiteaApiClient.token}'}, **kwargs)

    @staticmethod
    def put(endpoint, data=None, **kwargs):
        return requests.put(f'{GITEA_API_BASE}{endpoint}',
                            data=data, headers={'Authorization': f'token {GiteaApiClient.token}'}, **kwargs)


@pytest.fixture()
def gitea_client():
    return GiteaApiClient()


@pytest.fixture()
def jenkins_client():
    return Jenkins('http://localhost:8080', username='admin', password='admin')


try:
    shutil.rmtree('tests/repositories')
except FileNotFoundError:
    pass
