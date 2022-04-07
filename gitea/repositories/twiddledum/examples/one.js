var dedupe = require('../')

console.log('----------- primitive types -----------')
var a = [1, 2, 2, 3]
var b = dedupe(a)

console.log(a)
console.log('becomes')
console.log(b)

console.log('----------- complex types types -----------')
var aa = [{a: 2}, {a: 1}, {a: 1}, {a: 1}]
var bb = dedupe(aa)

console.log(aa)
console.log('becomes')
console.log(bb)

console.log('----------- complex types types with custom hasher -----------')
var aaa = [{a: 2, b: 1}, {a: 1, b: 2}, {a: 1, b: 3}, {a: 1, b: 4}]
var bbb = dedupe(aaa, value => value.a)

console.log(aaa)
console.log('becomes')
console.log(bbb)