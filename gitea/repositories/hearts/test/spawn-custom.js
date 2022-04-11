// vim: expandtab:ts=2:sw=2

var
  path = require('path'),
  readJsonConfig = require('./util').readJsonConfig,
  spawn = require('./spawn');

var config = readJsonConfig(process.argv[2]);
spawn.graceful = !!config.graceful;

// import the test case function and execute it
var fn = require(path.join(__dirname, 'outband', config.tc));
fn.apply(spawn);
