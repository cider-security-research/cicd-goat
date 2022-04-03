import sqlite3
from binascii import hexlify
from hashlib import pbkdf2_hmac
from random import choice
from string import ascii_letters, digits
from time import time
import requests
from giteacasc.base import GiteaBase
from requests.auth import HTTPBasicAuth
import git


class Gitea(GiteaBase):
    YAML_USERS = 'users'
    YAML_ORGS = 'orgs'
    YAML_REPOS = 'repos'

    def __init__(self, username, password):
        GiteaBase.token = requests.post(f'{Gitea.gitea_api_base_url}/users/{username}/tokens',
                                        auth=HTTPBasicAuth(username, password),
                                        json={'name': 'token'}).json()['sha1']

    def create_user(self, username, email, password, must_change_password=False, token=None):
        res = self.post('/admin/users', json={'username': username,
                                              'email': email,
                                              'password': password,
                                              'must_change_password': must_change_password})
        if res.status_code != 201:
            res.raise_for_status()
        user = User(res.json()['id'], username, email, must_change_password)
        if token:
            user.create_token(token)
        return user

    def create_org(self, owner_name, org_name, teams=None, repos=None):
        res = self.get(f'/admin/orgs')
        if res.status_code != 200:
            res.raise_for_status()
        for org in res.json():
            if org_name == org['username']:
                return Org(org_name)
        res = self.post(f'/admin/users/{owner_name}/orgs', json={'username': org_name})
        if res.status_code != 201:
            res.raise_for_status()
        org = Org(org_name)
        if teams:
            for team in teams:
                org.create_team(team, teams[team])
        if repos:
            for name in repos:
                org.create_repo(**repos[name])
        return org


class User(GiteaBase):
    def __init__(self, uid, username, email, must_change_password=True):
        self.uid = uid
        self.name = username
        self.email = email
        self.must_change_password = must_change_password

    def create_token(self, token, name='token'):
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
        now = int(time())
        con.execute(f"INSERT INTO access_token VALUES ({token_id + 1}, {self.uid}, '{name}', '{token_hash}', '{salt}', "
                    f"'{token_last_eight}', {now}, {now})")
        con.execute(f"UPDATE sqlite_sequence SET seq=1 WHERE name='access_token'")
        con.commit()
        con.close()


class Org(GiteaBase):
    def __init__(self, org_name):
        self.name = org_name

    def create_team(self, name, permissions, members):
        res = self.post(f'/orgs/{self.name}/teams', json={'name': name, 'permissions': permissions})
        if res.status_code != 201:
            res.raise_for_status()
        for username in members:
            res = self.put(f"/teams/{res.json()['id']}/members/{username}")
            if res.status_code != 204:
                res.raise_for_status()

    def create_repo(self, name, private, git_repo_path=None, default_branch='main', collaborators=None,
                    branch_protections=None, teams=None, releases=None, webhooks=None):
        res = self.post(f'/orgs/{self.name}/repos', json={'name': name,
                                                          'default_branch': default_branch,
                                                          'private': private})
        if res.status_code != 201:
            res.raise_for_status()
        repo = Repo(self.name, name, private, default_branch)
        if git_repo_path:
            repo.push_code(git_repo_path)
        if collaborators:
            for collaborator in collaborators:
                repo.add_collaborator(collaborator, collaborators[collaborator])
        if branch_protections:
            for branch in branch_protections:
                repo.set_branch_protection(branch, **branch_protections[branch])
        if teams:
            for name in teams:
                repo.add_teams(name)
        if releases:
            for name in releases:
                repo.create_release(name, releases[name])
        if webhooks:
            for url in webhooks:
                repo.create_webhook(url, **webhooks[url])
        return repo


class Repo(GiteaBase):
    def __init__(self, org_name, repo_name, private, default_branch):
        self.org = org_name
        self.name = repo_name
        self.private = private
        self.default_branch = default_branch

    def push_code(self, git_repo_path):
        repo = git.Repo(git_repo_path)
        repo.git.push('origin', '--tags', '-u', self.default_branch)

    def add_collaborator(self, collaborator, permission):
        self.put(f'/repos/{self.org}/{self.name}/collaborators/{collaborator}',
                 json={'permission': permission})

    def set_branch_protection(self, branch, required_approvals=None):
        self.post(f'/repos/{self.org}/{self.name}/branch_protections',
                  json={'branch_name': branch, 'required_approvals': required_approvals})

    def add_team(self, name):
        self.put(f'/repos/{self.org}/{self.name}/teams/{name}')

    def create_release(self, tag, name):
        self.post(f'/repos/{self.org}/{self.name}/releases', json={'name': name, 'tag_name': tag})

    def create_webhook(self, url, events=None, branch_filter=None):
        self.post(f'/repos/{self.org}/{self.name}/hooks',
                  json={'type': 'gitea',
                        'config': {'url': url, 'content_type': 'application/json'},
                        'branch_filter': branch_filter,
                        'events': events})
