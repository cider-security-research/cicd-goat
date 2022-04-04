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
  describe('#file()', function () {
    describe('when running inband standard tests', function () {

      inbandStandardTests(true, function before(done) {
        var that = this;

        tmp.file(this.opts, function (err, name, fd, removeCallback) {
          if (err) return done(err);
          that.topic = { name: name, fd: fd, removeCallback: removeCallback };
          done();
        });
      });

      describe('with invalid tries', function () {
        it('should result in an error on negative tries', function (done) {
          tmp.file({ tries: -1 }, function (err) {
            try {
              assert.ok(err instanceof Error, 'should have failed');
            } catch (err) {
              return done(err);
            }
            done();
          });
        });

        it('should result in an error on non numeric tries', function (done) {
          tmp.file({ tries: 'nan' }, function (err) {
            try {
              assert.ok(err instanceof Error, 'should have failed');
            } catch (err) {
              return done(err);
            }
            done();
          });
        });
      });
    });

    describe('when running issue specific inband tests', function () {
      it('on issue #182: should not replace empty postfix with ".tmp"', function (done) {
        tmp.file({ postfix: '' }, function (err, path) {
          try {
            assert.ok(!path.endsWith('.tmp'));
          } catch (err) {
            return done(err);
          }
          done();
        });
      });
    });

    describe('when running standard outband tests', function () {
      it('on graceful', function (done) {
        childProcess(this, 'graceful-file.json', function (err, stderr, stdout) {
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
        childProcess(this, 'non-graceful-file.json', function (err, stderr, stdout) {
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
        childProcess(this, 'keep-file.json', function (err, stderr, stdout) {
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
        childProcess(this, 'unlink-file.json', function (err, stderr, stdout) {
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
        childProcess(this, 'issue115.json', function (err, stderr, stdout) {
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