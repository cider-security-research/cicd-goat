/* eslint-disable no-octal */
// vim: expandtab:ts=2:sw=2

var
  assert = require('assert'),
  inbandStandardTests = require('./inband-standard'),
  assertions = require('./assertions'),
  childProcess = require('./child-process').genericChildProcess,
  rimraf = require('rimraf'),
  tmp = require('../lib/tmp');


// make sure that everything gets cleaned up
tmp.setGracefulCleanup();


describe('tmp', function () {
  describe('#fileSync()', function () {
    describe('when running inband standard tests', function () {
      inbandStandardTests(true, function before() {
        this.topic = tmp.fileSync(this.opts);
      }, true);

      describe('with invalid tries', function () {
        it('should result in an error on negative tries', function () {
          try {
            tmp.fileSync({ tries: -1 });
            assert.fail('should have failed');
          } catch (err) {
            assert.ok(err instanceof Error);
          }
        });

        it('should result in an error on non numeric tries', function () {
          try {
            tmp.fileSync({ tries: 'nan' });
            assert.fail('should have failed');
          } catch (err) {
            assert.ok(err instanceof Error);
          }
        });
      });
    });

    describe('when running issue specific inband tests', function () {
      it('on issue #182: should not replace empty postfix with ".tmp"', function () {
        const tmpobj = tmp.fileSync({ postfix: '' });
        assert.ok(!tmpobj.name.endsWith('.tmp'));
      });
    });

    describe('when running standard outband tests', function () {
      it('on graceful', function (done) {
        childProcess(this, 'graceful-file-sync.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (!stderr) return done(new Error('stderr expected'));
          try {
            assertions.assertDoesNotExist(stdout);
          } catch (err) {
            rimraf.sync(stdout);
            return done(err);
          }
          done();
        });
      });

      it('on non graceful', function (done) {
        childProcess(this, 'non-graceful-file-sync.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (!stderr) return done(new Error('stderr expected'));
          try {
            assertions.assertExists(stdout, true);
            rimraf.sync(stdout);
          } catch (err) {
            return done(err);
          }
          done();
        });
      });

      it('on keep', function (done) {
        childProcess(this, 'keep-file-sync.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (stderr) return done(new Error(stderr));
          try {
            assertions.assertExists(stdout, true);
            rimraf.sync(stdout);
          } catch (err) {
            return done(err);
          }
          done();
        });
      });

      it('on unlink (keep == false)', function (done) {
        childProcess(this, 'unlink-file-sync.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (stderr) return done(new Error(stderr));
          try {
            assertions.assertDoesNotExist(stdout);
          } catch (err) {
            rimraf.sync(stdout);
            return done(err);
          }
          done();
        });
      });
    });

    describe('when running issue specific outband tests', function () {
      it('on issue #115', function (done) {
        childProcess(this, 'issue115-sync.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (stderr) return done(new Error(stderr));
          try {
            assertions.assertDoesNotExist(stdout);
          } catch (err) {
            rimraf.sync(stdout);
            return done(err);
          }
          done();
        });
      });
      it('on issue #115', function (done) {
        childProcess(this, 'issue115-sync.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (stderr) return done(new Error(stderr));
          try {
            assertions.assertDoesNotExist(stdout);
          } catch (err) {
            rimraf.sync(stdout);
            return done(err);
          }
          done();
        });
      });
    });
  });
});
