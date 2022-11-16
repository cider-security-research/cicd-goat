#!/bin/bash

cd /setup/repositories/pygryphon
python3 -m twine upload --repository gitlab dist/* --config /setup/resources/gryphon/.pypirc

export DOCKER_HOST=tcp://docker:2375
docker pull python:3.8
docker tag python:3.8 gitlab:5050/wonderland/nest-of-gold/python:3.8
docker login --username=root --password=ciderland5# gitlab:5050
docker push gitlab:5050/wonderland/nest-of-gold/python:3.8