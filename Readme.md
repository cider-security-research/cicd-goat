# CI/CD Goat Development
This is the build repository for [https://github.com/cider-rnd/cicd-goat](https://github.com/cider-rnd/cicd-goat)

![Logo_on dark@3x](https://user-images.githubusercontent.com/88270351/143437403-79b0ae54-a117-420d-b1a2-b285c0d8db59.png)

## Development
1. Install the environment:
  ```
  git clone git@github.com:cider-rnd/cicd-goat-dev.git
  cd cicd-goat-dev
  docker-compose -f docker-compose-dev.yaml up -d
  ```
2. Make the desired changes on the systems using:
  ```
  * CTFd: http://localhost:8000
    * username: alice
    * password: alice
  * Gitea: http://localhost:3000
    * username: thealice
    * password: thealice
  * Jenkins: http://localhost:9090
    * username: alice
    * password: alice
  ``` 
4. Change the TAG in `build.sh` and run `./build.sh build` to build and push images of the new version.
5. Change the tags in docker-compose.yaml and run `docker-compose up -d` to run test environment.
6. Test the new environment.
7. After tests have passed run: `./build.sh publish` to publish the new version as latest.

## Todo
1. Create images for all other services, publish new version and remove data folder from main repo.
2. Fix agent jenkins_home permission issues on linux.


