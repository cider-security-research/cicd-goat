folder('dodo') {
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
              password('A62F0E52-7D67-410E-8279-32447ADAD916')
            }
          }
        }
      }
    }
  }
}
job('dodo/dodo') {
  scm {
    git {
      remote {
        url('http://gitea:3000/Wonderland/dodo.git')
      }
      branch('main')
    }
  }
  triggers {
    pollSCM {
      scmpoll_spec('*/1 * * * *')
    }
  }
  wrappers {
    credentialsBinding {
      usernamePassword('USERNAME', 'FLAG7', 'flag7')
    }
  }
  steps {
    shell('checkov -o json -d . > checkov-result.json')
    shell('curl -X POST http://wonderland:9000/upload -H "Content-Type: application/json" -d @checkov-result.json -H "Authorization: Bearer ${FLAG7}" || true')
  }
}