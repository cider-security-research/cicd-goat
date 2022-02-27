from pathlib import Path
from jenkinsapi.custom_exceptions import NoBuildData
from time import sleep


def create_fork(gitea_client, owner, repo):
    res = gitea_client.get('/orgs')
    assert res.status_code == 200
    for org in res.json():
        if 'test' in org['username']:
            break
    else:
        res = gitea_client.post('/orgs',
                                json={"full_name": "test", 'username': 'test', 'visibility': 'public'})
        assert res.status_code == 201
    res = gitea_client.get('/orgs/test/repos')
    for repo_dict in res.json():
        if repo == repo_dict['name']:
            return True
    else:
        res = gitea_client.post(f'/repos/{owner}/{repo}/forks',
                                json={"organization": "test"})
        if res.status_code == 202:
            return True
        return False


def branch_and_replace_file_content(repo, new_branch_name, relative_file_path, replace_tuples):
    new_branch = repo.create_head(new_branch_name)
    repo.head.reference = new_branch
    file_path = Path(repo.working_tree_dir) / relative_file_path
    file_content = file_path.read_text()
    for old, new in replace_tuples:
        file_content = file_content.replace(old, new)
    with open(file_path, 'w') as f:
        f.write(file_content)
    repo.git.add(file_path)
    repo.index.commit('update')
    repo.git.push('origin', '-u', new_branch)


def find_in_console(jenkins_client, job_name, string):
    for tmp_job_name, job_instance in jenkins_client.get_jobs():
        if job_name in tmp_job_name:
            try:
                last_build = job_instance.get_last_build()
                while 1:
                    if not last_build.is_running():
                        break
                    sleep(1)
                if string in job_instance.get_last_build().get_console():
                    return True
            except NoBuildData:
                continue
    else:
        return False

