# CI/CD Goat
![](https://github.com/cider-rnd/cicd-goat-dev/actions/workflows/ci.yml/badge.svg)

![logo](http://url.com)

Deliberately vulnerable CI/CD environment.

## Introduction
This project aims to raise awareness for CI/CD security and to help people learn in a fun way how to secure CI/CD environments.

## Installation
### Linux & Mac:

**No need to clone the repository**
```sh
curl -o cicd-goat/docker-compose.yaml --create-dirs https://raw.githubusercontent.com/cider-rnd/cicd-goat-dev/main/docker-compose.yaml
cd cicd-goat && docker-compose up -d
```
### Windows:

**No need to clone the repository**

Powershell:
```PowerShell
curl -o cicd-goat/docker-compose.yaml --create-dirs https://raw.githubusercontent.com/cider-rnd/cicd-goat-dev/main/docker-compose.yaml
get-content docker-compose.yaml | %{$_ -replace "bridge","nat"}
cd cicd-goat && docker-compose up -d
```

## Usage
### Instructions
* **!!!SPOILER ALERT!!!** Don't browse the repository files before solving the challenges as they contain spoilers.
* To configure your git client for accessing private repositories we suggest cloning using the http url.
* In each challenge, find the flag - in the format of flag# (e.g flag2), or another format if mentioned specifically. Could be credential, file, etc.
* Insert the flag on CTFd and find out if you got it right.
* If needed, use the hints on CTFd from top to bottom.
* No need to access or hack the infrastructure or other users.
* No need to exploit CVEs.
* Don’t execute code on the Jenkins Controller unless you’re asked to.

### Take the challenge
1. Login to CTFd at http://localhost:8000 to view the challenges:
   * Username: `alice`
   * Password: `alice`

2. Start hacking!!!
   * Jenkins http://localhost:8080
     * Username: `alice`
     * Password: `alice`
   * Gitea http://localhost:3000
     * Username: `thealice`
     * Password: `thealice`

### Troubleshooting
* When forking a repository don't change the forked repository name as it won't build on Jenkins.
* Jobs might take time to start running if the agent is occupied by another job.

### Solutions
See [Spoilers.md](Spoilers.md#Solutions)

## Development
1. Install testing dependencies: 
    ```sh
    pip install pipenv
    pipenv install --deploy
    ```
2. Run the development environment:
    ```sh
    rm -rf tmp tmp-data/
    cp -R data/ tmp-data/
    docker-compose -f docker-compose-dev.yaml up -d
    ```
3. Make the desired changes:
   * Jenkins is completely configured as code so desired changes should be made to the files in "jenkins-server" or "jenkins-agent" folders.
   * To make changes in Gitea and CTFd, use the admin credentials in [Spoilers.md](Spoilers.md#Admin Credentials)
4. Shutdown the environment, move changes in Gitea and CTFd to data/ and rebuild it:
    ```sh
    docker-compose -f docker-compose-dev.yaml down
    ./commit.sh
    docker-compose -f docker-compose-dev.yaml up -d --build
    ```
5. Run tests: `pytest`
7. Commit and push!

## Contributing
Follow the checklist below to add a challenge:
  1. CTFd:
     1. Write challenge description.
     2. Write hints.
     3. Insert the flag.
  2. Gitea:
     1. Create repository and configure relevant access permissions.
     2. Use another OS repository that has MIT license as a template.
  3. Jenkins:
     1. Configure a job that runs automatically.
     2. Validate that the new challenge doesn't interfere with other challenges.
  4. Make sure the flag is not accessible when solving other challenges.
  5. Write tests.
  6. Write the solution on Spoilers.md.
  7. Update Readme.md if needed.
