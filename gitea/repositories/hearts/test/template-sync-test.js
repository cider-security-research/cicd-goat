/* eslint-disable no-octal */
// vim: expandtab:ts=2:sw=2

const
  assert = require('assert'),
  tmp = require('../lib/tmp');

describe('tmp', function () {
  describe('dirSync()', function () {
    it('with invalid template', function () {
      try {
        tmp.dirSync({template:'invalid'});
      } catch (err) {
        assert.equal(err.message, 'Invalid template, found "invalid".', 'should have thrown the expected error');
      }
    });
  });

  describe('fileSync()', function () {
    it('with invalid template', function () {
      try {
        tmp.fileSync({template:'invalid'});
      } catch (err) {
        assert.equal(err.message, 'Invalid template, found "invalid".', 'should have thrown the expected error');
      }
    });
  });
});
