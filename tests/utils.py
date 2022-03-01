from pathlib import Path


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

