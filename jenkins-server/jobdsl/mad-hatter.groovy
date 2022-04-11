multibranchPipelineJob('wonderland-mad-hatter') {
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
              id('flag3')
              description('')
              username('flag3')
              password('ACD6E6B8-3584-4F43-AB9C-ACD080B8EBB2')
            }
            usernamePassword {
              scope('GLOBAL')
              id('jenkins3')
              description('')
              username('jenkins_hatter')
              password('jenjen123&^*')
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
          repository('mad-hatter')
          serverUrl("http://gitea:3000")
        }
      }
    }
  }
  factory{
    remoteJenkinsFileWorkflowBranchProjectFactory{
      localMarker("")
      matchBranches(false)
      fallbackBranch("main")
      remoteJenkinsFile("Jenkinsfile")
      remoteJenkinsFileSCM{
        gitSCM{
          userRemoteConfigs{
            userRemoteConfig{
              name("mad-hatter-pipeline") 
              url("http://gitea:3000/Wonderland/mad-hatter-pipeline.git") 
              refspec("") 
              credentialsId("jenkins3") 
            }
            browser{} 
            gitTool("") 
          }
          branches {
            branchSpec {
              name('*/main')
            }
          }
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