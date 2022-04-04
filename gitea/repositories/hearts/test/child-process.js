// vim: expandtab:ts=2:sw=2

var
  fs = require('fs'),
  path = require('path'),
  exists = fs.exists || path.exists,
  spawn = require('child_process').spawn;

const ISTANBUL_PATH = path.join(__dirname, '..', 'node_modules', 'istanbul', 'lib', 'cli.js');

module.exports.genericChildProcess = _spawnProcess('spawn-generic.js');
module.exports.childProcess = _spawnProcess('spawn-custom.js');

function _spawnProcess(spawnFile) {
  return function (testCase, configFile, cb, signal) {
    const
      configFilePath = path.join(__dirname, 'outband', configFile),
      commandArgs = [path.join(__dirname, spawnFile), configFilePath];

    exists(configFilePath, function (configExists) {
      if (configExists) return _doSpawn(commandArgs, cb, signal);

      cb(new Error('ENOENT: configFile ' + configFilePath + ' does not exist'));
    });
  };
}

function _doSpawn(commandArgs, cb, signal) {
  const
    node_path = process.argv[0],
    stdoutBufs = [],
    stderrBufs = [];
  let
    child,
    done = false,
    stderrDone = false,
    stdoutDone = false;

  if (process.env.running_under_istanbul) {
    commandArgs = [
      ISTANBUL_PATH, 'cover', '--report' , 'none', '--print', 'none',
      '--dir', path.join('coverage', 'json'), '--include-pid',
      commandArgs[0], '--', commandArgs[1]
    ];
  }

  // spawn doesn’t have the quoting problems that exec does,
  // especially when going for Windows portability.
  child = spawn(node_path, commandArgs);
  child.stdin.end();

  function _close() {
    // prevent race conditions
    if (stderrDone && stdoutDone && !done) {
      const
        stderr = _bufferConcat(stderrBufs).toString(),
        stdout = _bufferConcat(stdoutBufs).toString();
      done = true;
      cb(null, stderr, stdout);
    }
  }

  child.on('error', function _spawnError(err) {
    if (!done) {
      done = true;
      cb(err);
    }
  });

  child.stdout.on('data', function _stdoutData(data) {
    stdoutBufs.push(data);
  }).on('close', function _stdoutEnd() {
    stdoutDone = true;
    _close();
  });

  child.stderr.on('data', function _stderrData(data) {
    stderrBufs.push(data);
  }).on('close', function _stderrEnd() {
    stderrDone = true;
    _close();
  });

  if (signal) {
    setTimeout(function () {
      // SIGINT does not work on node <8.12.0
      child.kill(signal);
    }, 1000);
  }
}

function _bufferConcat(buffers) {
  if (Buffer.concat) {
    return Buffer.concat.apply(this, arguments);
  }

  return new Buffer(buffers.reduce(function (acc, buf) {
    for (let i = 0; i < buf.length; i++) {
      acc.push(buf[i]);
    }
    return acc;
  }, []));
}
