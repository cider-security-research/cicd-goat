multibranchPipelineJob('wonderland-mock-turtle') {
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
              id('mock-turtle-token')
              description('')
              username('mock-turtle-ci')
              password('03f186631edec80f38b9cc2f7f45870a30cc33e2')
            }
            usernamePassword {
              scope('GLOBAL')
              id('flag10')
              description('')
              username('flag10')
              password('D54734AB-7B83-4931-A9BB-171476101FDF')
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
          repository('mock-turtle')
          serverUrl("http://gitea:3000")
          traits {
            headWildcardFilter {
              includes('main PR-*')
              excludes('')
            }
          }
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
              name("mock-turtle")
              url("http://gitea:3000/Wonderland/mock-turtle.git")
              refspec("")
              credentialsId("mock-turtle-token")
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
      strategyId('3')
    }
    traits << 'org.jenkinsci.plugin.gitea.OriginPullRequestDiscoveryTrait' {
      strategyId('1')
    }
    def triggers = node / triggers / 'com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger'
    triggers.appendNode('spec', '* * * * *')
    triggers.appendNode('interval', '60000')
  }
}