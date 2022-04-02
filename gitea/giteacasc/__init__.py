import click
import yaml
import requests
from requests.auth import HTTPBasicAuth
from string import ascii_letters, digits
from random import choice
from hashlib import pbkdf2_hmac
import sqlite3
from time import time
from binascii import hexlify

YAML_USERS = 'users'
YAML_ORGS = 'orgs'
YAML_PASSWORD = 'password'
YAML_EMAIL = 'email'
YAML_TOKEN = 'token'
YAML_PEOPLE = 'people'
YAML_TEAMS = 'teams'
YAML_REPOS = 'repos'


class GiteaBase:
    gitea_base_url = 'http://localhost:3000'
    gitea_api_base_url = f'{gitea_base_url}/api/v1'
    token = None

    def post(self, endpoint, data=None, json=None, **kwargs):
        return requests.post(f'{self.gitea_api_base_url}{endpoint}',
                             data=data, json=json, headers={'Authorization': f'token {self.token}'}, **kwargs)

    def get(self, endpoint, params=None, **kwargs):
        return requests.get(f'{self.gitea_api_base_url}{endpoint}',
                            params=params, headers={'Authorization': f'token {self.token}'}, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return requests.put(f'{self.gitea_api_base_url}{endpoint}',
                            data=data, headers={'Authorization': f'token {self.token}'}, **kwargs)


class Gitea(GiteaBase):
    def __init__(self, username, password):
        GiteaBase.token = requests.post(f'{Gitea.gitea_api_base_url}/users/{username}/tokens',
                                        auth=HTTPBasicAuth(username, password),
                                        json={'name': 'token'}).json()['sha1']

    def create_user(self, username, email, password, must_change_password=False):
        res = self.post('/admin/users', json={'username': username,
                                              'email': email,
                                              'password': password,
                                              'must_change_password': must_change_password})
        if res.status_code != 201:
            res.raise_for_status()
        return res.json()['id']

    @staticmethod
    def create_token(uid, token, name='token'):
        salt = ''.join(choice(ascii_letters + digits) for _ in range(10))
        # token = str(sha1(uuid4()))
        token_hash = hexlify(pbkdf2_hmac('sha256',
                                         bytes(token, 'utf-8'),
                                         bytes(salt, 'utf-8'),
                                         10000, dklen=50)).decode()
        token_last_eight = token[-8:]
        con = sqlite3.connect('/data/gitea/gitea.db')
        cur = con.cursor()
        token_id = cur.execute('SELECT MAX(id) FROM access_token').fetchall()[0][0]
        print(token_id)
        now = int(time())
        con.execute(f"INSERT INTO access_token VALUES ({token_id + 1}, {uid}, '{name}', '{token_hash}', '{salt}', "
                    f"'{token_last_eight}', {now}, {now})")
        con.execute(f"UPDATE sqlite_sequence SET seq=1 WHERE name='access_token'")
        con.commit()
        print(cur.execute('SELECT * FROM access_token').fetchall())
        con.close()

    def create_org(self, owner_name, org_name):
        res = self.get(f'/admin/orgs')
        if res.status_code != 200:
            res.raise_for_status()
        for org in res.json():
            if org_name == org['username']:
                return Org(org_name)
        res = self.post(f'/admin/users/{owner_name}/orgs', json={'username': org_name})
        if res.status_code != 201:
            res.raise_for_status()
        return Org(org_name)


class Org(GiteaBase):
    def __init__(self, org_name):
        self.name = org_name

    def create_repo(self, name):
        pass

    def add_people(self, username):
        pass

    def create_team(self, name, people):
        pass


class Repo(GiteaBase):
    def __init__(self, name, visibility, git_repo_path, collaborators=None):
        pass

    def add_collaborators(self, collab_dict):
        pass

    def set_branch_protection(self, name, required_approvals=None):
        pass

    def add_teams(self, teams_dict):
        pass

    def create_release(self, name, tag):
        pass

    def create_webhook(self, url, events=None, branch_filter=None):
        pass


class Configure(Gitea):
    def users(self, users):
        for username in users:
            uid = self.create_user(username,
                                   users[username][YAML_EMAIL],
                                   users[username][YAML_PASSWORD])
            if YAML_TOKEN in users[username]:
                self.create_token(uid, users[username][YAML_TOKEN])

    def people(self, org, people):
        pass

    def teams(self, org, teams):
        pass

    def repos(self, org, repos):
        pass


@click.command()
@click.argument('path', type=str)
@click.option('-u', '--username', 'admin_username', help='Admin username.')
@click.option('-p', '--password', 'admin_password', help='Admin password.')
def giteacasc(path, admin_username, admin_password):
    with open(path, 'r') as y:
        config = yaml.safe_load(y.read())
    configure = Configure(admin_username, admin_password)
    if YAML_USERS in config:
        configure.users(config[YAML_USERS])
    """
    if YAML_ORGS in config:
    for org_name in config[YAML_ORGS]:
        org = configure.create_org(admin_username, org_name)
        if YAML_PEOPLE in config[YAML_ORGS]:
            configure.people(org, config[YAML_ORGS][YAML_PEOPLE])
        if YAML_TEAMS in config[YAML_ORGS]:
            configure.teams(org, config[YAML_ORGS][YAML_TEAMS])
        if YAML_REPOS in config[YAML_ORGS]:
            configure.repos(org, config[YAML_ORGS][YAML_REPOS])
    """
