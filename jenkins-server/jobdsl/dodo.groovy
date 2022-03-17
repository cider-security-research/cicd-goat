pipelineJob('dodo') {
  definition {
    cpsScm {
      scm {
        git {
          remote {
            url('http://gitea:3000/Wonderland/dodo.git')
          }
          branch('main')
        }
      }
    }
    cpsFlowDefinition {
      sandbox(true)
      script('''pipeline {
    agent any

    stages {
        stage ('Checkout') {
            steps {
                git branch: 'main', url: 'http://gitea:3000/Wonderland/dodo.git'
            }
        }

        stage ('Security Scan') {
            steps {
                sh "checkov -d ."
            }
        }

        stage ('Deploy') {
            steps {
                sh """terraform init -no-color
                terraform import aws_iam_role.tf-iam-role-replication-12345 tf-iam-role-replication-12345
                terraform plan -no-color
                terraform apply -no-color -auto-approve
                """
            }
        }

        stage ('Validate deployment') {
            steps {
                sh \'''res=awslocal s3api get-bucket-acl --bucket dodo | jq '.Grants[] | select(.Grantee.Type == "Group" and .Grantee.URI == "http://acs.amazonaws.com/groups/global/AllUsers" and .Permission == "READ")' &> /dev/null
                      if [ -z "$res" ]
                      then
                          echo "Valid"
                      else
                          echo "FLAG7: A62F0E52-7D67-410E-8279-32447ADAD916"
                      fi
                \'''
            }
        }

    }
    post {
        always {
            cleanWs()
        }
    }
}'''.stripIndent())
    }
  }
  triggers {
    pollSCM {
      scmpoll_spec('*/1 * * * *')
    }
  }
}