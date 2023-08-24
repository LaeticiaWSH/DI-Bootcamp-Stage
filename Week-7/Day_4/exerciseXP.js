// //Exercise 1 : Colors
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
colors.forEach((item,index) => {
    console.log(`${index + 1}# choice is ${item}.`)
})

colors.some((color) => color === "Violet")
// { console.log("Yeah");} else{console.log("No...")}
if (colors.some((color) => color === "Violet")) {
    console.log("Yeah");
} else {
    console.log("No...");
}

// Exercise 2 : Colors #2
//const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th", "st", "nd", "rd"];

let n;
colors.forEach((item,index) =>{
    if (index + 1 === 1){
        n = ordinal[1]
        console.log(`${index + 1}${n} choice is ${item}.`)
    } else if(index + 1 === 2){
        n = ordinal[2]
        console.log(`${index + 1}${n} choice is ${item}.`)

    } else if (index + 1 === 3) {
        n = ordinal[3]
        console.log(`${index + 1}${n} choice is ${item}.`)
    } else {
        n = ordinal[0]
        console.log(`${index + 1}${n} choice is ${item}.`)
    }
})

//ex 3
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);

// const country = "USA";
// console.log([...country]);

// let newArray = [...[, ,]];
// console.log(newArray);

//ex 4
const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
{ firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
{ firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
{ firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
{ firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
{ firstName: 'Wes', lastName: 'Reid', role: 'Instructor' },
{ firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor' }];

const welcomeStudents = users.map((user) => `Hello ${user.firstName}`)
console.log(welcomeStudents)
const fullstackres = users.filter((user) => { return user.role === "Full Stack Resident"})
console.log(fullstackres)

const lname = fullstackres.map((user) => user.lastName)
console.log(lname)

//ex 5
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
const string = epic.reduce((acc, val) => acc + val)
console.log(string)

//ex 6
const students = [{ name: "Ray", course: "Computer Science", isPassed: true },
{ name: "Liam", course: "Computer Science", isPassed: false },
{ name: "Jenner", course: "Information Technology", isPassed: true },
{ name: "Marco", course: "Robotics", isPassed: true },
{ name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
{ name: "Jamie", course: "Big Data", isPassed: false }];

let pass = students.filter((student) => {return student.isPassed === true})
console.log(pass)

pass.forEach((student) =>{
    console.log(`Good job ${student.name}, you passed the course in ${student.course}.`)
})




