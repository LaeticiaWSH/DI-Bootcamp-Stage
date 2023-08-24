const numbers = [10, 11, 12, 15, 20];

numbers.forEach((n,i,num) => {
    if (num[i] %2 === 0){
        console.log(n)
    }
}) 
const words = ["wow", "hey", "bye"];
words.some((string) => {return (string.charAt(0) === "h");})
// // by function method.
// const words = ["wow", "hey", "bye"];
// function checkL(word) {
//     {
//         return word.charAt(0) === "h"
//     }
// }
// words.some(checkL);

const words1 = ["hello", "hey", "hola"];
// // Different ways of writing it shorter and shorter.
// words1.every(function(string) {return(string[0] === "h" );})
// words1.every((string) => {return(string[0] === "h" );})
words1.every((string) => string[0] === "h" )

let party = [
    {
        desert: 'Chocolate Mousse',
        calories: 30,
    },
    {
        desert: 'Apple Pie',
        calories: 15,
    },
    {
        desert: 'Croissant',
        calories: 50,
    },
    {
        desert: 'Strawberry Icecream',
        calories: 5,
    },
]
let party2 = party.filter((party) => { return party.desert !== 'Apple Pie'})
// const reducer = (accumulator,calories) => accumulator + calories ;

//we put zero at the end to define acc as it is an array of objects(dict) ==> it means "accumulator = 0".
// the "cal" parameter refers to the array "party2"
let sum = party2.reduce((accumulator,cal) => {return accumulator + cal.calories},0)
