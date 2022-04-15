pipelineJob('wonderland-dodo') {
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

        stage ('Scan and Deploy') {
            steps {
                sh \'\'\'
                    checkov -d . --check CKV2_AWS_39,CKV2_AWS_38,CKV_AWS_20,CKV_AWS_57
                    terraform init -no-color
                    terraform plan -no-color
                    terraform apply -no-color -auto-approve
                    res=`awslocal --endpoint-url=http://localstack:4566 s3api get-bucket-acl --bucket dodo | jq '.Grants[] | select(.Grantee.Type == "Group" and .Grantee.URI == "http://acs.amazonaws.com/groups/global/AllUsers" and .Permission == "READ")' &> /dev/null`
                    if [ -z "$res" ]
                    then
                        echo "Secure"
                    else
                        echo "FLAG7: A62F0E52-7D67-410E-8279-32447ADAD916"
                    fi
                \'\'\'
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
}
