multibranchPipelineJob('caterpillar-prod') {
  properties {
    folderCredentialsProperty {
      domainCredentials {
        domainCredentials {
          domain {
            name('')
            description('')
          }
          credentials {
            usernamePassword {
              scope('GLOBAL')
              id('flag2')
              description('')
              username('flag2')
              password('AEB14966-FFC2-4FB0-BF45-CD903B3535DA')
            }
          }
        }
      }
    }
  }  
  branchSources {
    branchSource {
      source {
        giteaSCMSource {
          id('1')
          credentialsId('gitea-access-token')
          repoOwner("${OWNER}")
          repository('caterpillar')
          serverUrl("http://gitea:3000")
        }
      }
    }
  }
  configure { node ->
    def traits = node / sources / data / 'jenkins.branch.BranchSource' / source / traits
    traits << 'org.jenkinsci.plugin.gitea.BranchDiscoveryTrait' {
      strategyId('1')
    }
    def triggers = node / triggers / 'com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger'
    triggers.appendNode('spec', '* * * * *')
    triggers.appendNode('interval', '60000')
  }
}