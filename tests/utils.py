from pathlib import Path


def branch_and_replace_file_content(repo, new_branch_name, relative_file_path, replace_tuples, commit=True, push=True):
    previous_branch = repo.head.reference
    if new_branch_name not in repo.heads:
        repo.create_head(new_branch_name, 'HEAD')
    repo.head.reference = repo.heads[new_branch_name]
    file_path = Path(repo.working_tree_dir) / relative_file_path
    file_content = file_path.read_text()
    for old, new in replace_tuples:
        file_content = file_content.replace(old, new)
    with open(file_path, 'w') as f:
        f.write(file_content)
    repo.git.add(file_path)
    if commit:
        repo.index.commit('update')
    if push:
        repo.git.push('origin', '-u', new_branch_name)
    repo.head.reference = previous_branch


def branch_and_write_file(repo, new_branch_name, relative_file_path, content, commit=True, push=True):
    previous_branch = repo.head.reference
    if new_branch_name not in repo.heads:
        repo.create_head(new_branch_name, 'HEAD')
    repo.head.reference = repo.heads[new_branch_name]
    file_path = Path(repo.working_tree_dir) / relative_file_path
    with open(file_path, 'w') as f:
        f.write(content)
    repo.git.add(file_path)
    if commit:
        repo.index.commit('update')
    if push:
        repo.git.push('origin', '-u', new_branch_name)
    repo.head.reference = previous_branch
