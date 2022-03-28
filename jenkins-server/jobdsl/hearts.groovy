job('hearts') {
  label('agent1')
  scm {
    git {
      remote {
        url('http://gitea:3000/Wonderland/hearts.git')
      }
      branch('main')
    }
  }
  triggers {
    pollSCM {
      scmpoll_spec('*/1 * * * *')
    }
  }
  steps {
    shell('''node -v
npm prune
npm install
npm test''')
    shell('''npm prune
rm node_modules -rf''')
  }
}