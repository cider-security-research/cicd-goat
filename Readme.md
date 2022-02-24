# CI/CD Goat Development
This is the development repository for [https://github.com/cider-rnd/cicd-goat](https://github.com/cider-rnd/cicd-goat)

![Logo_on dark@3x](https://user-images.githubusercontent.com/88270351/143437403-79b0ae54-a117-420d-b1a2-b285c0d8db59.png)

## Installation
```
curl
docker-compose up -d
```

## Development
1. Install the environment:
  ```
  git clone git@github.com:cider-rnd/cicd-goat-dev.git
  cd cicd-goat-dev
  cp -R data/ tmp-data/
  docker-compose -f docker-compose-dev.yaml up -d
  ```
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
6. Run tests: `pytest` 

## Todo
1. Create images for all other services, publish new version and remove data folder from main repo.
2. Fix agent jenkins_home permission issues on linux.
3. Change image names.
4. Add solutions, detailed challange description from docs and admin credentials.
5. Add troubleshooting section.

## Contribution
* Add scenario checklist
* update versions checklist

