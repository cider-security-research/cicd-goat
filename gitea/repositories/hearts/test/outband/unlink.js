const fs = require('fs');

module.exports = function (result) {
  const stat = fs.statSync(result.name);
  if (stat.isFile()) {
    // TODO must also close the file, otherwise the file will be closed during garbage collection, which we do not want
    // TODO #241 get rid of the open file descriptor
    fs.unlinkSync(result.name);
  } else {
    fs.rmdirSync(result.name);
  }
  this.out(result.name);
};
