/* eslint-disable no-octal */
// vim: expandtab:ts=2:sw=2

const
  assertions = require('./assertions'),
  childProcess = require('./child-process').childProcess,
  os = require('os'),
  testCases = [
    'SIGINT',
    'SIGTERM'
  ];

// skip tests on win32
const isWindows = os.platform() === 'win32';
const tfunc = isWindows ? xit : it;

describe('tmp', function () {
  describe('issue121 - clean up on terminating signals', function () {
    for (let tc of testCases) {
      tfunc('for signal ' + tc, function (done) {
        // increase timeout so that the child process may terminate in time
        this.timeout(5000);
        issue121Tests(tc)(done);
      });
    }
  });
});

function issue121Tests(signal) {
  return function (done) {
    childProcess(this, 'issue121.json', function (err, stderr, stdout) {
      if (err) return done(err);
      else if (stderr) return done(new Error(stderr));

      assertions.assertDoesNotExist(stdout);
      done();
    }, signal);
  };
}
