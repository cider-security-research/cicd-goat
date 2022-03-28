// Currently there is no option to configure per project authorization using casc
// https://issues.jenkins.io/browse/JENKINS-56774
multibranchPipelineJob('cheshire-cat') {
  branchSources {
    branchSource {
      source {
        giteaSCMSource {
          id('1')
          credentialsId('gitea-access-token')
          repoOwner("${OWNER}")
          repository('cheshire-cat')
          serverUrl("http://gitea:3000")
        }
      }
    }
  }
  configure { node ->
    def traits = node / sources / data / 'jenkins.branch.BranchSource' / source / traits
    traits << 'org.jenkinsci.plugin.gitea.OriginPullRequestDiscoveryTrait' {
      strategyId('2')
    }
    def triggers = node / triggers / 'com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger'
    triggers.appendNode('spec', '* * * * *')
    triggers.appendNode('interval', '60000')
  } 
}