//ex 1
// #1
// function funcOne() {
//     const a = 5;
//     if (a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }
// funcOne()

// // #2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()

// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // // #3.1 - run in the console:
// funcFour()
// funcFive()


// //#4
// let a = 1;
// function funcSix() {
//     const a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // // #4.1 - run in the console:
// funcSix()
// // // #4.2 What will happen if the variable is declared
// // // with const instead of let ?

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared 
// with const instead of let ?

//ex 2
let winBattle =()=>{
    return true
}
const experiencePoints = winBattle()? 10 : 1;
console.log(experiencePoints)
//ex 3
let Checktype = (a) =>{
    return typeof(a) === "string"
}
console.log(Checktype("ABCD"))
console.log(Checktype(1234))

//ex 4 
 let sum = (a,b)=> a + b;
 console.log(sum(1,2))

//ex 5
//First, use function declaration and invoke it.
function kgToGramDeclaration(weight){
    return weight * 1000;
}
// console.log(kgToGramDeclaration(2))
// //Then, use function expression and invoke it.
const kgToGram = function(weight){
    return weight * 1000;
}
// console.log(kgToGram(4))
//Finally, use a one line arrow function and invoke it.
const ktg = w =>  w * 1000;
console.log(ktg(6))



//ex 6
//Create a self invoking function that takes 4 arguments
(function(numberofchildren, partnersname , geographiclocation, jobtitle){
    let sentence = `You will be a ${jobtitle} in ${geographiclocation}, and married to ${partnersname} with ${numberofchildren} kids.`
    //The function should display in the DOM a sentence
    document.getElementById("container").textContent = sentence
})(3,"Chase","Portland","Web-developer");
//ex 7
//Create a Navbar in your HTML file.
//In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
(function(){
    let n = prompt("Hello! what's your name? ")
    document.getElementById("navbar").textContent = "Welcome " + n
})();
//ex 8
// The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.
function makeJuice(size)
{
    //The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence 
function addIngredients(a,b,c){
return `The client wants a ${size} juice, containing ${a}, ${b}, ${c}`;
    }
return addIngredients("apple","ice","refreshing water")
}
let s = prompt("Enter the desired beverage size(large/medium/small) : ")
document.write(makeJuice(s))


// -----Part II-----
//In the makeJuice function, create an empty array named ingredients.
function makeJuice(size){
    let ingredients = [];
    //The addIngredients function should now receive 3 ingredients, and push them into the ingredients array

    function addIngredients(a,b,c){
        ingredients.push(a);
        ingredients.push(b);
        ingredients.push(c);
    }
addIngredients("apple","ice","refreshing water");
addIngredients("kiwi","sugar","syrup");

//Create a new inner function named displayJuice that displays on the DOM a sentence
    function displayJuice(){
        return `The client wants a ${size} juice, containing ${ingredients.join(' ,')}.`;
        }
return displayJuice()

}
let f = prompt("Enter the desired beverage size(large/medium/small) : ")
document.write(makeJuice(f))