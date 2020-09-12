
var length = 16;                               // Number
console.log(typeof(length));
var lastName = "Johnson";                      // String
console.log(typeof(lastName));
var x = {firstName:"John", lastName:"Doe"};    // Object
console.log(typeof(x));
var cars = ["Saab", "Volvo", "BMW"];
console.log(typeof(cars));
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
person = null;    // Now value is null, but type is still an object
console.log(typeof(person));
person = undefined; 
console.log(typeof(person));