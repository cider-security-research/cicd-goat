multibranchPipelineJob('wonderland-dormouse') {
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
              id('flag9')
              description('')
              username('flag9')
              password('31350FBC-A959-4B4B-A8BD-DCA7AC9248A6')
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
          repository('dormouse')
          serverUrl("http://gitea:3000")
        }
      }
    }
  }
  configure { node ->
    def traits = node / sources / data / 'jenkins.branch.BranchSource' / source / traits
    traits << 'org.jenkinsci.plugin.gitea.BranchDiscoveryTrait' {
      strategyId('3')
    }
  }
}