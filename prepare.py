#!/usr/bin/env python3
from pathlib import Path
from sys import argv
from shutil import move

REPOSITORIES_PATH = 'gitea/repositories'


def mover(src, dst):
    for path in Path(REPOSITORIES_PATH).iterdir():
        if path.is_dir():
            dot_git = path / src
            try:
                move(str(dot_git), str(dot_git.parent / dst))
            except FileNotFoundError:
                continue


if argv[1] == 'notgit':
    mover('.git', 'not.git')
elif argv[1] == 'git':
    mover('not.git', '.git')
else:
    print(f'Invalid argument: {argv[1]}')
    exit()




