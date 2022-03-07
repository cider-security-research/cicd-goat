# CI/CD Goat Development
![](https://github.com/cider-rnd/cicd-goat-dev/actions/workflows/ci.yml/badge.svg)

This is the development repository for [https://github.com/cider-rnd/cicd-goat](https://github.com/cider-rnd/cicd-goat)

![Logo_on dark@3x](https://user-images.githubusercontent.com/88270351/143437403-79b0ae54-a117-420d-b1a2-b285c0d8db59.png)

* Add testing status image

## Installation
Linux & Mac:
```
no need to clone
curl
docker-compose up -d
```
Windows:
```
no need to clone
curl?
get-content docker-compose.txt | %{$_ -replace "expression","replace"}
sed -i 's/bridge/nat/' docker-compose.yaml
docker-compose up -d
```

## Usage


## Development
1. Install the environment accroding to installation above but replace...:
2. cp -R data/ tmp-data/
  `docker-compose -f docker-compose-dev.yaml up -d`
  
2. Make the desired changes:
* Jenkins is completely configured as code so desired changes should be made to files in "jenkins-server" or "jenkins-agent" folders.
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
2. move docker files to root
3. Windows can't be tested because windows container cannot run jenkins

## Contribution
* Add scenario checklist
  * Tests should cleanup after them
* update versions checklist


