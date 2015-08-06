var Person = require('./person');
var john = new Person('john');
john.talk();//在index文件中，你不再是接收一个对象作为返回值，而是函数，这得归功于对module.exports的重写