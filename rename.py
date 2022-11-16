#!/usr/bin/env python3
from pathlib import Path
from sys import argv
from shutil import move
from itertools import chain

GITEA_REPOSITORIES_PATH = 'gitea/repositories'
GITLAB_REPOSITORIES_PATH = 'gitlab/repositories'


def mover(src, dst):
    for path in chain(Path(GITEA_REPOSITORIES_PATH).iterdir(), Path(GITLAB_REPOSITORIES_PATH).iterdir()):
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




