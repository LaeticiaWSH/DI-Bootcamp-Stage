// Ex1 ---Part 1
const people = ["Greg", "Mary", "Devon", "James"];
console.log(people.splice(0,1))
// Write code to remove “Greg” from the people array.
console.log(people)

// Write code to replace “James” to “Jason”.
console.log(people.splice(2,1,"Jason"))
console.log(people)
// Write code to add your name to the end of the people array.
console.log(people.push("Laëticia"))
console.log(people)

// Write code that console.logs Mary’s index. 
console.log(people.indexOf("Mary"))

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
console.log(people.slice(1,3))

// Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(people.indexOf("Foo"))
// Ans = since "Foo" is not in the list the index is negative .

// Create a variable called last which value is the last element of the array.
let last = people[people.length - 1]
console.log(last)

//Ex 1 -- Part 2
// Using a loop, iterate through the people array and console.log each person.
l = people.length
for (let i = 0; i < l; i++){
    console.log(people[i])
}

// Using a loop, iterate through the people array and exit the loop after you console.log “Devon” . 
l = people.length
for (let i = 0; i < l; i++) {
    console.log(people[i])
    if (people[i] == "Devon"){
        break;
    }
}

// Ex 2
//Create an array called colors where the value is a list of your five favorite colors.
const colors = ["Red","Blue","Brown","Green","Pink"]

// Loop through the array and as you loop console.
for(let i = 1;i < colors.length + 1 ;i++){
    console.log("My #" + i + " choice is " + colors[i - 1])
}

// // Ex 3
// // Prompt the user for a number.
// let num = prompt("Enter a number")

// // While the number is smaller than 10 continue asking the user for a new number.
// let i = 1
// while (i < 10){
//     prompt("Enter a number")
//     i++

// Ex 4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}
// Console.log the number of floors in the building.
let totalfloor = building.numberOfFloors
console.log(totalfloor)

// Console.log how many apartments are on the floors 1 and 3.
console.log(building.numberOfAptByFloor.firstFloor)
console.log(building.numberOfAptByFloor.thirdFloor)

// Console.log the name of the second tenant and the number of rooms he has in his apartment. 
console.log(building.nameOfTenants[1])
console.log(building.numberOfRoomsAndRent.dan[0])

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200
let duo_rent = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]
let dan_rent = building.numberOfRoomsAndRent.dan[1]
if (duo_rent > dan_rent){
    building.numberOfRoomsAndRent.dan[1] =  1200

}
console.log(building)

// Ex 5
// Create an object called family with a few key value pairs
const family = {
    mother : "Sandra",
    father : "Eliot",
    daughter : "Kaela",
    son : "JJ"
}
let x = Object.keys(family).length

for (let i = 0; i < x;i++){
    console.log(Object.keys(family)[i])
}
for (let i = 0; i < x;i++){
    console.log(Object.values(family)[i])
}

// Ex 6
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}
// Given the object above and using a for loop, console.log
let z =Object.keys(details).length
for(let i = 0; i < z; i++){
        console.log(Object.keys(details)[i])
        console.log(Object.values(details)[i])
}
// Ex 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let size = names.length
let society_name;
for (let i = 0;i < size;i++){
    n = names[i]
    index = n.slice(0,1)
    society_name += index
}
console.log(society_name)