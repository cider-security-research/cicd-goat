// vim: expandtab:ts=2:sw=2

function _writeSync(stream, str, cb) {
  var flushed = stream.write(str);
  if (flushed) {
    return cb(null);
  }

  stream.once('drain', function _flushed() {
    cb(null);
  });
}

module.exports = {
  graceful: false,
  out: function (str, cb) {
    cb = cb || this.exit;
    _writeSync(process.stdout, str, cb);
  },
  err: function (errOrStr, cb) {
    cb = cb || this.exit;
    if (!this.graceful) _writeSync(process.stderr, (errOrStr instanceof Error) ? errOrStr.toString() : errOrStr, cb);
    else cb();
  },
  fail: function (errOrStr, cb) {
    cb = cb || this.exit;
    _writeSync(process.stderr, (errOrStr instanceof Error) ? errOrStr.toString() : errOrStr, cb);
  },
  exit: function (code) {
    process.exit(code || 0);
  }
};

