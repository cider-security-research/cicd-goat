[![cicd-goat](goat_logo.png)](#)
[![Maintained by Cider Security](https://img.shields.io/badge/maintained%20by-Cider%20Security-brightgreen)](https://cidersecurity.io)
[![](https://img.shields.io/badge/Top%2010%20Risks-9%2F10-2de4fd)](https://www.cidersecurity.io/top-10-cicd-security-risks/)
[![cider-security-research](https://circleci.com/gh/cider-security-research/cicd-goat.svg?style=svg)](https://circleci.com/gh/cider-security-research/cicd-goat)
![Version](https://img.shields.io/docker/v/cidersecurity/goat-jenkins-server?sort=semver&style=plastic)
![Docker pulls](https://img.shields.io/docker/pulls/cidersecurity/goat-jenkins-server?style=plastic)

Deliberately vulnerable CI/CD environment.
Hack CI/CD pipelines, catch the flags.

The CI/CD goat project allows engineers and security practitioners to learn and practice CI/CD security through a set of 10 challenges, enacted against a real, full blown CI/CD environment. The scenarios are of varying difficulty levels, with each scenario focusing on one primary attack vector.

CI/CD Goat was created by [Cider Security](https://www.cidersecurity.io/).

## Download & Run
**There's no need to clone the repository.**
### Linux & Mac:

```sh
curl -o cicd-goat/docker-compose.yaml --create-dirs https://raw.githubusercontent.com/cider-security-research/cicd-goat/main/docker-compose.yaml
cd cicd-goat && docker-compose up -d
```
### Windows (Powershell):
```PowerShell
curl -o cicd-goat/docker-compose.yaml --create-dirs https://raw.githubusercontent.com/cider-security-research/cicd-goat/main/docker-compose.yaml
get-content docker-compose.yaml | %{$_ -replace "bridge","nat"}
cd cicd-goat && docker-compose up -d
```

## Usage
### Instructions
* **WARNING!** Avoid browsing the repository files as they contain spoilers.
* To configure your git client for accessing private repositories we suggest cloning using the http url.
* In each challenge, find the flag - in the format of _flag#_ (e.g _flag2_), or another format if mentioned specifically.
* If needed, use the hints on CTFd.
* There is no need to exploit CVEs.
* No need to hijack admin accounts of Gitea or Jenkins.

### Take the challenge
1. Login to CTFd at http://localhost:8000 to view the challenges:
   * Username: `alice`
   * Password: `alice`

2. Hack:
   * Jenkins http://localhost:8080
     * Username: `alice`
     * Password: `alice`
   * Gitea http://localhost:3000
     * Username: `thealice`
     * Password: `thealice`

3. Insert the flags on CTFd and find out if you got it right.

### Troubleshooting
* If Gitea shows a blank page, refresh the page.
* When forking a repository, don't change the name of the forked repository.

## Solutions
:see_no_evil: Warning: Spoilers!
See [Solutions](solutions).

## Contributing
### Environment
1. Clone the repository.
2. Rename .git folders to make them usable:<br/>
    ```sh
    python prepare.py git
    ```
3. Install testing dependencies: 
    ```sh
    pip install pipenv
    pipenv install --deploy
    ```
4. Run the development environment:
    ```sh
    rm -rf tmp tmp-ctfd/
    cp -R ctfd/data/ tmp-ctfd/
    docker-compose -f docker-compose-dev.yaml up -d
    ```
5. Make the desired changes:
   * All services except CTFd are completely configured as code so desired changes should be made to the files in the appropriate folders.
   * To make changes in CTFd, use the [admin credentials](break-glass.md).
6. Shutdown the environment, move changes made in CTFd to data/ and rebuild it:
    ```sh
    docker-compose -f docker-compose-dev.yaml down
    ./apply.sh
    docker-compose -f docker-compose-dev.yaml up -d --build
    ```
7. Run tests: `pytest`
8. Rename .git folders to allow push:
    `python prepare.py notgit`
9. Commit and push!

### Contributing
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

???hidden malicious additions to gitea and ctfd???
???add todo???
