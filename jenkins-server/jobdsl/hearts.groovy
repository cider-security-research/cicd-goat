job('wonderland-hearts') {
  label('agent1')
  scm {
    git {
      remote {
        url('http://gitea:3000/Wonderland/hearts.git')
      }
      branch('main')
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