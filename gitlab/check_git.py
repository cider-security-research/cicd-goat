#!/usr/bin/env python3
from pathlib import Path


repositories = Path(__file__).parent.resolve() / 'repositories'
for folder in repositories.iterdir():
    if folder.is_dir():
        not_git = folder / 'not.git'
        if not_git in folder.iterdir():
            raise Exception('not.git folder found instead of .git')
exit(0)


