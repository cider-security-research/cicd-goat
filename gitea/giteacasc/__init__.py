import click
import yaml
from giteacasc.gitea import Gitea, YAML_USERS, YAML_ORGS


@click.command()
@click.argument('path', type=str)
@click.option('-u', '--username', 'admin_username', help='Admin username.')
@click.option('-p', '--password', 'admin_password', help='Admin password.')
def giteacasc(path, admin_username, admin_password):
    with open(path, 'r') as y:
        config = yaml.safe_load(y.read())
    ### add schema validation ###
    ### add doc strings ###
    g = Gitea(admin_username, admin_password)
    if YAML_USERS in config:
        for username in config[YAML_USERS]:
            g.create_user(username, **config[YAML_USERS][username])
    if YAML_ORGS in config:
        for org_name in config[YAML_ORGS]:
            g.create_org(admin_username, org_name, config[YAML_ORGS][org_name])


