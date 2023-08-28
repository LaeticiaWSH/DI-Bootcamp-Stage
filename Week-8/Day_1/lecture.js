let myObj = {
    name: "John",
    lastName: "Doe",
    age: 25,
    friends: ["Mark", "Lucie", "Ana"]
}
const k = Object.keys(Object)
const v = Object.values(Object)
// for ([key,value] of Object.entries(myObj)){

// }
const user = { name: 'Lydia', age: 21 };
const admin = { admin: true, ...user };
console.log(admin);