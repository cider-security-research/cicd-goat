multibranchPipelineJob('caterpillar-test') { 
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
    traits << 'org.jenkinsci.plugin.gitea.ForkPullRequestDiscoveryTrait' {
      strategyId('2')
      trust(class: 'org.jenkinsci.plugin.gitea.ForkPullRequestDiscoveryTrait$TrustEveryone')
    }
    def triggers = node / triggers / 'com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger'
    triggers.appendNode('spec', '* * * * *')
    triggers.appendNode('interval', '60000')
  }
}