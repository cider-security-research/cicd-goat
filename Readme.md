# Jenkins Docker Setup

This repo contains:

- Required docker configurations to setup of Jenkins which is quick and reproducible.
- Jenkins docker installation [page](https://www.jenkins.io/doc/book/installing/docker/) provides us with more detailed explaination.
- This repo just convert the same set of instructions into easier portable solution using `docker-compose`.

# Usage:

```bash
$ docker-compose up --build
Creating JenkinsDocker ... done
Creating JenkinsServer ... done
```
JenkinsServer is now accecible at [localhost:8080/](http://localhost:8080/).


Now Jenkins Server is accessible at [localhost:8080](http://localhost:8080/).

## Details:

The [`docker-compose.yaml`](./docker-compose.yaml) file defines following components:

- Jenkins Network: Defines underlying bridge network.
- Jenkins Server: This is jenkins server container definition.
- Jenkins Docker: A `docker:dind` container to enable running docker inside docker.

### Jenkins Network:

Here we will be setting up the underlying network for the containers to communicate between themself. We create a bridge network with name space as `jenkins`.

```yaml
networks:
  jenkins:
    driver: bridge # Defines bridge network to be used by services defined later.
```

### Jenkins Docker:

It is a good practice to run the Jenkins job inside docker containers rather than Jenkins host machine itself. 

- This enables us to maintain isolation between multiple Jenkins Pipelines and Jobs.
- Also we ahieve an easily reproducible/debuggable job execution environment setup.

Since this is a Jenkins Server setup running as docker container we would need to setup `docker-inside-docker`, i.e to be able to run docker commands and containers (JOBS containers) inside another docker container (Jenkins Server Container). This is made possible with using `docker:dind` container.

Here JenkinsDocker container starts docker-engine and exposes it at address `tcp://docker:2376`. This address will be used later by JenkinsServer container to bring up Jobs containers.

```yaml
services:
  jenkins_docker:
    image: docker:dind
    networks:
      jenkins:
        aliases:
          - docker # Defines to use jenkins network defined above also under the alias name `docker`.
    container_name: JenkinsDocker
    privileged: true
    environment:
      - DOCKER_TLS_CERTDIR=/certs
    ports:
      - "2376:2376" # Exposes docker serveer port 2376 to be used by jenkins server container at "tcp://docker:2376".
    volumes:
      - ./jenkins-docker-certs:/certs/client # Docker client certs.
      - ./jenkins-data:/var/jenkins_home # Preserves Jenkins data like job definitions, credentials, build logs, etc.
      - ./extras:/extras # Any extra data or files you want to cache between server restart can be saved here `/extras/`.
```

### Jenkins Server:

As last part of the equation, we would bring up JenkinsSever container using customised image `jenkins/jenkins:lts-slim`. JenkinsServer is now accecible at [localhost:8080/](http://localhost:8080/).

```yaml
services:
  jenkins_server:
    build:
      context: # Build container from the custom Dockerfile defined in the repo.
    networks:
      - jenkins # Use jenkins network defined earlier
    container_name: JenkinsServer
    restart: always
    environment: # Define docker env variable to connect to docker-engine defined in JenkinsDocker container.
      - DOCKER_HOST=tcp://docker:2376
      - DOCKER_CERT_PATH=/certs/client
      - DOCKER_TLS_VERIFY=1
    ports:
      - "8080:8080" # For UI
      - "50000:50000" # For API
    volumes:
      - ./jenkins-data:/var/jenkins_home:rw # Docker client certs.
      - ./jenkins-docker-certs:/certs/client:ro # Preserves Jenkins data like job definitions, credentials, build logs, etc.
      - ./extras:/extras:rw # Any extra data or files you want to cache between server restart can be saved here `/extras/`.
```

### Dockerfile

We have customised docker image `jenkins/jenkins:lts-slim` in the [Dockerfile](devops/workshop/jenkins/Dockerfile) to

- Include few useful plugins and
- Installed docker cli to be able to build our jobs inside docker containers to maintain isolation.

```Dockerfile
FROM jenkins/jenkins:lts-slim
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
       apt-transport-https \
       ca-certificates curl gnupg2 \
       software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88
RUN add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins blueocean:1.24.3

```

### Other useful components:

```bash
$ tree -aL 1
.
├── .dockerignore # Contains file patterns to ignore, while creating docker context
├── .git
├── .gitignore # Ignores docker volume mounts
├── Dockerfile
├── LICENSE
├── Readme.md
├── docker-compose.yaml
├── docker-data
├── extras # extras volume mount
├── jenkins-data # Jenkins build logs, etc volume mount
└── jenkins-docker-certs # docker certs volume mount
```
