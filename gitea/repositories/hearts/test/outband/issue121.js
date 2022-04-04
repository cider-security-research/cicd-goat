// vim: expandtab:ts=2:sw=2

const tmp = require('../../lib/tmp');

process.on('SIGINT', function () {
  process.exit(0);
});

process.on('SIGTERM', function () {
  process.exit(0);
});

// https://github.com/raszi/node-tmp/issues/121
module.exports = function () {

  tmp.setGracefulCleanup();

  const result = tmp.dirSync({ unsafeCleanup: true });

  this.out(result.name, function () { });

  setTimeout(function () {
    throw new Error('ran into timeout');
  }, 10000);
};
