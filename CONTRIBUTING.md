# Contributing
## Development
1. Clone the repository.
2. Rename .git folders to make them usable:<br/>
    ```sh
    ./rename.py git
    ```
3. Install testing dependencies: 
    ```sh
    pip3 install pipenv==2023.12.1
    pipenv install --deploy
    ```
4. Run the development environment to experiment with new changes:
    ```sh
    rm -rf tmp tmp-ctfd/
    cp -R ctfd/data/ tmp-ctfd/
    docker compose -f docker-compose-dev.yaml up -d
    ```
5. Make the desired changes:
   * All services except CTFd are completely configured as code so desired changes should be made to the files in the appropriate folders.
   * To make changes in CTFd, use the [admin credentials](break-glass.md).

6. Shutdown the environment, move changes made in CTFd and rebuild it:
    ```sh
    docker compose -f docker-compose-dev.yaml down
    ./apply.sh # save CTFd changes
    docker compose -f docker-compose-dev.yaml up -d --build
    ```
7. Run tests:
   ```shell
   pytest -n 2 tests/
   ```
8. Rename .git folders to allow push:
    ```shell
    ./rename.py notgit
    ```
9. Commit and push!

## Checklist
Follow the checklist below to add a challenge:
  1. CTFd:
     1. Write challenge description.
     2. Choose category according to difficulty level.
     3. Make sure the challenge is visible and has value according to difficulty.
     4. Write hints in order of usage.
     5. Add a flag. Make sure to select if it's case-insensitive.
  2. Gitea:
     1. Configure a new repository in gitea.yaml.
     2. Create the repository under [gitea/repositories](gitea/repositories). Use an open-source repository that use the MIT license as a template for the challenge repository.
  3. Jenkins:
     1. Configure Jenkins and add new jobdsl files in the casc.yaml file.
     2. Make sure jobs don't run periodically. Jobs should be triggered by events / polling.
     3. Validate that the new challenge doesn't interfere with other challenges.
  4. GitLab:
     1. Configure Gitlab by changing the gitlab.tf file and run `terraform init` to update lock file.
     2. To upload new repositories add the releqvant line in repositories.sh.
     3. If any additional files are needed place them inside the resources' folder.
  5. Make sure the flag is not accessible when solving other challenges.
  6. Write tests.
  7. Write the solution.
  8. Update README.md if needed.
  9. In order to run the CI, make sure you have a CircleCI account and that you’ve clicked “Set Up Project” on your fork of the project.