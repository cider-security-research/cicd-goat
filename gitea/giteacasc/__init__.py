import click
import yaml
from giteacasc.gitea import Gitea
import os

@click.command()
@click.argument('path', type=str)
@click.option('-u', '--username', 'admin_username', help='Admin username.')
@click.option('-p', '--password', 'admin_password', help='Admin password.')
def giteacasc(path, admin_username, admin_password):
    with open(path, 'r') as y:
        config = yaml.safe_load(y.read())
    ### add schema validation ###
    ### add doc strings ###
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.environ['GIT_ASKPASS'] = os.path.join(project_dir, 'askpass.py')
    os.environ['GIT_USERNAME'] = admin_username
    os.environ['GIT_PASSWORD'] = admin_password
    g = Gitea(admin_username, admin_password)
    if Gitea.YAML_USERS in config:
        for username in config[Gitea.YAML_USERS]:
            g.create_user(username, **config[Gitea.YAML_USERS][username])
    if Gitea.YAML_ORGS in config:
        for org_name in config[Gitea.YAML_ORGS]:
            g.create_org(admin_username, org_name, **config[Gitea.YAML_ORGS][org_name])


