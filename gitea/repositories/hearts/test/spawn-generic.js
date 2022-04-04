// vim: expandtab:ts=2:sw=2

var
  path = require('path'),
  readJsonConfig = require('./util').readJsonConfig,
  spawn = require('./spawn'),
  tmp = require('../lib/tmp');

var config = readJsonConfig(process.argv[2]);
spawn.graceful = !!config.graceful;

var fnUnderTest = null;

if (config.async) fnUnderTest = (config.file) ? tmp.file : tmp.dir;
else fnUnderTest = (config.file) ? tmp.fileSync : tmp.dirSync;

// make sure that we have a SIGINT handler so CTRL-C the test suite
// will not leave anything behing
process.on('SIGINT', process.exit);

// do we test against tmp doing a graceful cleanup?
if (config.graceful) tmp.setGracefulCleanup();

// import the test case function and execute it
var fn = require(path.join(__dirname, 'outband', config.tc));
if (config.async)
  fnUnderTest(config.options, function (err, name, fdOrCallback, cb) {
    if (err) spawn.err(err);
    else {
      var result = null;
      if (config.file) result = { name: name, fd: fdOrCallback, removeCallback: cb };
      else result = { name: name, removeCallback: fdOrCallback };
      fn.apply(spawn, [result, tmp]);
    }
  });
else {
  fn.apply(spawn, [fnUnderTest(config.options), tmp]);
}

