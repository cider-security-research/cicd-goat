/* eslint-disable no-octal */

var
  assert = require('assert'),
  fs = require('fs'),
  path = require('path'),
  existsSync = fs.existsSync || path.existsSync;


module.exports.assertName = function assertName(name, expected) {
  assert.ok(typeof name == 'string');
  if (expected) {
    assert.equal(path.basename(name), expected, 'should be the expected name');
  } else {
    assert.ok(name.length > 0, 'an empty string is not a valid name');
  }
};


module.exports.assertMode = function assertMode(name, mode) {
  var stat = fs.statSync(name);

  // mode values do not work properly on Windows. Ignore “group” and
  // “other” bits then. Ignore execute bit on that platform because it
  // doesn’t exist—even for directories.
  if (process.platform === 'win32') {
    assert.equal(stat.mode & 0o600, mode & 0o600);
  } else {
    assert.equal(stat.mode & 0o777, mode);
  }
};


module.exports.assertDir = function assertDir(name, dir) {
  assert.equal(name.slice(0, dir.length), dir, 'should have the expected dir as the leading path');
};


module.exports.assertPrefix = function assertPrefix(name, prefix) {
  assert.equal(path.basename(name).slice(0, prefix.length), prefix, 'should have the provided prefix');
};


module.exports.assertPostfix = function assertPostfix(name, postfix) {
  assert.equal(name.slice(name.length - postfix.length, name.length), postfix, 'should have the provided postfix');
};


module.exports.assertProperResult = function assertProperResult(result, withfd) {
  assert.ok(result);
  assert.ok(result.name, 'should have a name');
  if (withfd) assert.ok(result.fd, 'should have an fd');
  else assert.strictEqual(result.fd, undefined, 'should not have a file descriptor (fd)');
  assert.ok(typeof result.removeCallback == 'function', 'should have a removeCallback');
};


module.exports.assertExists = function assertExists(name, isfile) {
  assert.ok(existsSync(name), name + ' should exist');
  var stat = fs.statSync(name);
  if (isfile) assert.ok(stat.isFile(), name + ' should be a file');
  else assert.ok(stat.isDirectory(), name + ' should be a directory');
};


module.exports.assertDoesNotExist = function assertDoesNotExist(name) {
  assert.ok(!existsSync(name), name + ' should not exist');
};

module.exports.assertDoesNotStartWith = function assertDoesNotStartWith(s, prefix, msg) {
  if (s.indexOf(prefix) == 0) assert.fail(msg || s);
};

