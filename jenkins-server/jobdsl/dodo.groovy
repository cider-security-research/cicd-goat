folder('wonderland-dodo') {
  properties {
    folderCredentialsProperty{
      domainCredentials {
        domainCredentials {
          domain {
            name('')
            description('')
          }
          credentials {
            usernamePassword {
              scope('GLOBAL')
              id('flag7')
              description('')
              username('flag7')
              password('QTYyRjBFNTItN0Q2Ny00MTBFLTgyNzktMzI0NDdBREFEOTE2Cg==')
            }
          }
        }
      }
    }
  }
}
pipelineJob('wonderland-dodo/wonderland-dodo') {
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
    wrappers {
    credentialsBinding {
      usernamePassword('USERNAME', 'FLAG7', 'flag7')
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
                        decoded=`echo $FLAG7 | base64 -d`
                        echo "FLAG7: $decoded"
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
