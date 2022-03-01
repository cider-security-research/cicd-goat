# CI/CD Goat Development
![](https://github.com/cider-rnd/cicd-goat-dev/actions/workflows/ci.yml/badge.svg)

This is the development repository for [https://github.com/cider-rnd/cicd-goat](https://github.com/cider-rnd/cicd-goat)

![Logo_on dark@3x](https://user-images.githubusercontent.com/88270351/143437403-79b0ae54-a117-420d-b1a2-b285c0d8db59.png)

* Add testing status image

## Installation
```
no need to clone
curl
* For Windows machines run the following command: sed -i 's/bridge/nat/' docker-compose.yaml
docker-compose up -d
```

## Usage


## Development
### Requirements
* Python
* pip install requirements
### How to develop
1. Install the environment:
  ```
  git clone git@github.com:cider-rnd/cicd-goat-dev.git
  cd cicd-goat-dev
  cp -R data/ tmp-data/
  ```
  * For Windows machines run the following command: `sed -i 's/bridge/nat/' docker-compose-dev.yaml`
  `docker-compose -f docker-compose-dev.yaml up -d`
  
2. Make the desired changes:
* Jenkins is completly configured as code so desired changes should be made to files in "jenkins-server" or "jenkins-agent" folders.
* To make changes in Gitea and CTFd, use the credentials below to make the changes inside the system:
  * CTFd: http://localhost:8000
    * username: admin
    * password: ciderland
  * Gitea: http://localhost:3000
    * username: red_queen
    * password: ciderland
4. Run `docker-compose -f docker-compose-dev.yaml down`
5. Run `./commit.sh`
6. Install testing dependencies: `pip install -r requirements.txt`
7. Run tests: `pytest` 

## Todo
1. Add troubleshooting section.
2. Windows cant be tested because windows container cannot run jenkins

## Contribution
* Add scenario checklist
  * Tests should be able to run successfully multiple times on the same environment to ease development. 
* update versions checklist


