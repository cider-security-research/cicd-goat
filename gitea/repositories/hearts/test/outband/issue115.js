var fs = require('fs');

module.exports = function (result) {
  // creates a tmp file and then closes the file descriptor as per issue 115
  // https://github.com/raszi/node-tmp/issues/115
  const self = this;
  fs.closeSync(result.fd);
  result.removeCallback(function () {
    self.out(result.name, self.exit);
  });
};

