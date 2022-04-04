module.exports = function (result) {
  this.out(result.name, function () {
    throw new Error('(non-)graceful cleanup testing');
  });
};
