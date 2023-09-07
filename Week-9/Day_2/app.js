// // THis is for CommonJS
// const g = require("./maths.js");
// // const greeting = require("./maths.js");

// const sname = "Mike Taylor";

// g.greeting(sname);


// // const add = require('./maths.js');
// g.add(4,6);
var validator = require("email-validator");
console.log(validator.validate("test@email.com"));
