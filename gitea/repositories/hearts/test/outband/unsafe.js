var
  fs    = require('fs'),
  join  = require('path').join;

module.exports = function (result) {
  // file that should be removed
  var fd = fs.openSync(join(result.name, 'should-be-removed.file'), 'w');
  fs.closeSync(fd);

  // in tree source
  var symlinkSource = join(__dirname, 'fixtures', 'symlinkme');
  // testing target
  var symlinkTarget = join(result.name, 'symlinkme-target');

  // symlink that should be removed but the contents should be preserved.
  // Skip on Windows because symlinks require elevated privileges (instead just
  // create the file)
  if (process.platform === 'win32') {
    fs.writeFileSync(symlinkTarget);
  } else {
    fs.symlinkSync(symlinkSource, symlinkTarget, 'dir');
  }

  this.out(result.name);
};
