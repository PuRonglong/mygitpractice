module.exports = Person;

function Person(name){
    this.name = name;
};

Person.prototype.talk = function(){
    console.log('我的名字是',this.name);
}