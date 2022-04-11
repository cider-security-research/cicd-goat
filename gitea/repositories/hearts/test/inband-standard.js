/* eslint-disable no-octal */
// vim: expandtab:ts=2:sw=2

var
  fs = require('fs'),
  path = require('path'),
  assertions = require('./assertions'),
  rimraf = require('rimraf'),
  tmp = require('../lib/tmp');

module.exports = function inbandStandard(isFile, beforeHook, sync = false) {
  var testMode = isFile ? 0o600 : 0o700;
  describe('without any parameters', inbandStandardTests({ mode: testMode, prefix: 'tmp-' }, null, isFile, beforeHook, sync));
  describe('with prefix', inbandStandardTests({ mode: testMode, prefix: 'tmp-' }, { prefix: 'tmp-something' }, isFile, beforeHook, sync));
  describe('with postfix', inbandStandardTests({ mode: testMode, prefix: 'tmp-' }, { postfix: '.txt' }, isFile, beforeHook, sync));
  describe('with template and no leading path', inbandStandardTests({ mode: testMode, prefix: 'tmp-clike-', postfix: '-postfix' }, { template: 'tmp-clike-XXXXXX-postfix' }, isFile, beforeHook, sync));
  describe('with template and leading path', inbandStandardTests({ mode: testMode, prefix: 'tmp-clike-', postfix: '-postfix' }, { template: path.join(tmp.tmpdir, 'tmp-clike-XXXXXX-postfix')}, isFile, beforeHook, sync));
  describe('with name', inbandStandardTests({ mode: testMode }, { name: 'tmp-using-name' }, isFile, beforeHook, sync));
  describe('with mode', inbandStandardTests(null, { mode: 0o755 }, isFile, beforeHook, sync));
  describe('with multiple options', inbandStandardTests(null, { prefix: 'tmp-multiple', postfix: 'bar', mode: 0o750 }, isFile, beforeHook, sync));
  describe('with tmpdir option', inbandStandardTests(null, { tmpdir: path.join(tmp.tmpdir, 'tmp-external'), mode: 0o750 }, isFile, beforeHook, sync));
  if (isFile) {
    describe('with discardDescriptor', inbandStandardTests(null, { mode: testMode, discardDescriptor: true }, isFile, beforeHook, sync));
    describe('with detachDescriptor', inbandStandardTests(null, { mode: testMode, detachDescriptor: true }, isFile, beforeHook, sync));
  }
};


function inbandStandardTests(testOpts, opts, isFile, beforeHook, sync = false) {
  return function () {
    opts = opts || {};
    testOpts = testOpts || {};

    // topic reference will be created by the beforeHook
    const topic = { topic: null, opts: opts };

    // hack for tmpdir option, otherwise the whole test shebang would have to be refactored
    if (opts.tmpdir) {
      if (!fs.existsSync(opts.tmpdir)) {
        // let tmp cleanup the dir on process exit, also we do not care if it is left over
        tmp.dirSync({name: path.relative(tmp.tmpdir, opts.tmpdir), unsafeCleanup: true});
      }
    }

    // bind everything to topic so we avoid global
    before(beforeHook.bind(topic));

    it('should return a proper result', function () {
      assertions.assertProperResult(this.topic, isFile && !opts.discardDescriptor);
    }.bind(topic));

    it('temporary ' + (isFile ? 'file' : 'directory') + ' should exist', function () {
      assertions.assertExists(this.topic.name, isFile);
    }.bind(topic));

    it('temporary ' + (isFile ? 'file' : 'directory') + ' should have the expected mode', function () {
      assertions.assertMode(this.topic.name, testOpts.mode || opts.mode);
    }.bind(topic));

    if(testOpts.prefix || opts.prefix) {
      it('should have the expected prefix', function () {
        assertions.assertPrefix(this.topic.name, testOpts.prefix || opts.prefix);
      }.bind(topic));
    }

    if (opts.postfix || testOpts.postfix) {
      it('should have the expected postfix', function () {
        assertions.assertPostfix(this.topic.name, testOpts.postfix || opts.postfix);
      }.bind(topic));
    }

    it('should have been created in the expected directory', function () {
      assertions.assertDir(this.topic.name, testOpts.dir || opts.dir || opts.tmpdir || tmp.tmpdir);
    }.bind(topic));

    if (opts.name) {
      it('should have the expected name', function () {
        assertions.assertName(this.topic.name, opts.name);
      }.bind(topic));
    }

    if (sync) {
      it('should have a working removeCallback', function () {
        try {
          this.topic.removeCallback();
        } catch (err) {
          // important: remove file or dir unconditionally
          try {
            rimraf.sync(this.topic.name);
          } catch (_ignored) {
            // ignore
          }
          throw err;
        }
      }.bind(topic));
    } else {
      it('should have a working removeCallback', function (done) {
        const self = this;
        this.topic.removeCallback(function (err) {
          if (err) return done(err);
          try {
            assertions.assertDoesNotExist(self.topic.name);
          } catch (err) {
            rimraf.sync(self.topic.name);
            return done(err);
          }
          done();
        });
      }.bind(topic));
    }
  };
}
