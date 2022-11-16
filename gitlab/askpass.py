#!/usr/bin/env python3
from sys import argv
from os import environ

if 'username' in argv[1].lower():
    print(environ['GIT_USERNAME'])
    exit()

if 'password' in argv[1].lower():
    print(environ['GIT_PASSWORD'])
    exit()

exit(1)
