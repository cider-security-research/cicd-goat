module.exports = {
  "env": {
    "es6": true,
    "node": true
  },
  "plugins": [
    "mocha"
  ],
  "extends": "eslint:recommended",
  "rules": {
    "indent": [
      "error",
      2
    ],
    "linebreak-style": [
      "error",
      "unix"
    ],
    "quotes": [
      "error",
      "single"
    ],
    "semi": [
      "error",
      "always"
    ],
    "no-extra-boolean-cast": 0
  }
};
