/* eslint-disable no-octal */
// vim: expandtab:ts=2:sw=2

var
  assert = require('assert'),
  path = require('path'),
  inbandStandardTests = require('./inband-standard'),
  childProcess = require('./child-process').genericChildProcess,
  assertions = require('./assertions'),
  rimraf = require('rimraf'),
  tmp = require('../lib/tmp');


// make sure that everything gets cleaned up
tmp.setGracefulCleanup();


describe('tmp', function () {
  describe('#dir()', function () {
    describe('when running inband standard tests', function () {
      inbandStandardTests(false, function before(done) {
        var that = this;
        tmp.dir(this.opts, function (err, name, removeCallback) {
          if (err) return done(err);
          that.topic = { name: name, removeCallback: removeCallback };
          done();
        });
      });

      describe('with invalid tries', function () {
        it('should result in an error on negative tries', function (done) {
          tmp.dir({ tries: -1 }, function (err) {
            try {
              assert.ok(err instanceof Error, 'should have failed');
            } catch (err) {
              return done(err);
            }
            done();
          });
        });

        it('should result in an error on non numeric tries', function (done) {
          tmp.dir({ tries: 'nan' }, function (err) {
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
    });

    describe('when running standard outband tests', function () {
      it('on graceful cleanup', function (done) {
        childProcess(this, 'graceful-dir.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (!stderr) return done(new Error('stderr expected'));
          try {
            assertions.assertDoesNotExist(stdout);
          } catch (err) {
            //rimraf.sync(stdout);
            return done(err);
          }
          done();
        });
      });

      it('on non graceful cleanup', function (done) {
        childProcess(this, 'non-graceful-dir.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (!stderr) return done(new Error('stderr expected'));
          try {
            assertions.assertExists(stdout);
            rimraf.sync(stdout);
          } catch (err) {
            return done(err);
          }
          done();
        });
      });

      it('on keep', function (done) {
        childProcess(this, 'keep-dir.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (stderr) return done(new Error(stderr));
          try {
            assertions.assertExists(stdout);
            rimraf.sync(stdout);
          } catch (err) {
            return done(err);
          }
          done();
        });
      });

      it('on unlink (keep == false)', function (done) {
        childProcess(this, 'unlink-dir.json', function (err, stderr, stdout) {
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

      it('on unsafe cleanup', function (done) {
        childProcess(this, 'unsafe.json', function (err, stderr, stdout) {
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

      it('on non unsafe cleanup', function (done) {
        childProcess(this, 'non-unsafe.json', function (err, stderr, stdout) {
          if (err) return done(err);
          if (stderr) return done(new Error(stderr));
          try {
            assertions.assertExists(stdout);
            assertions.assertExists(path.join(stdout, 'should-be-removed.file'), true);
            if (process.platform == 'win32')
              assertions.assertExists(path.join(stdout, 'symlinkme-target'), true);
            else
              assertions.assertExists(path.join(stdout, 'symlinkme-target'));
            rimraf.sync(stdout);
          } catch (err) {
            return done(err);
          }
          done();
        });
      });
    });

    describe('when running issue specific outband tests', function () {
      it('on issue #62', function (done) {
        childProcess(this, 'issue62.json', function (err, stderr, stdout) {
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

