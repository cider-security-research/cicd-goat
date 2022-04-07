// vim: expandtab:ts=2:sw=2

var
  fs = require('fs');

module.exports.readJsonConfig = function readJsonConfig(path) {
  var contents = fs.readFileSync(path);
  return JSON.parse(contents);
};
