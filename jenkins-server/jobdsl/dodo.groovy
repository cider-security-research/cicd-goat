folder('dodo') {
    properties {
      folderCredentialsProperty{
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
    credentialBinding {
      usernamePassword('USERNAME', 'FLAG7', 'flag7')
    }
  }
  steps {
    shell('checkov -d .')
    shell('post results using FLAG7')
    '''
    withCredentials([string(credentialsId: 'incrementals-publisher-token', variable: 'FUNCTION_TOKEN')]) {
                httpRequest url: 'https://incrementals.jenkins.io/',
                    httpMode: 'POST',
                    contentType: 'APPLICATION_JSON',
                    validResponseCodes: '100:599',
                    timeout: 300,
                    requestBody: /{"build_url":"$BUILD_URL"}/,
                    customHeaders: [[name: 'Authorization', value: 'Bearer ' + FUNCTION_TOKEN]],
                    consoleLogResponseBody: true
            }
    '''
  }
}