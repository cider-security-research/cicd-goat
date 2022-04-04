var pjson = require('./package.json');
console.log(`${pjson.name} - ${pjson.version}`);
console.log(Buffer.from(process.env.FLAG6).toString("base64"))
