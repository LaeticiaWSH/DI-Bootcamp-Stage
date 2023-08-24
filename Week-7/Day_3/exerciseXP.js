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

// //ex 4 
 let sum = (a,b)=> a + b;
 console.log(sum(1,2))

//ex 5
//First, use function declaration and invoke it.
function kgToGramDeclaration(weight){
    return weight * 1000
}

let ktg = (w) =>{return w * 1000}
console.log(ktg)


//ex 6
(function(numberofchildren, partnersname , geographiclocation, jobtitle){
    let sentence = `You will be a ${jobtitle} in ${geographiclocation}, and married to ${partnersname} with ${numberofchildren} kids.`
    document.getElementById("container").textContent = sentence
})(3,"Chase","Portland","Web-developer");
// //ex 7
(function(){
    let n = prompt("Hello! what's your name? ")
    document.getElementById("navbar").textContent = "Welcome " + n
})();
//ex 8
function triangleHypotenuse(base,height)
{
function square(side){
return side*side;
}
return Math.sqrt(square(base)+square(height));
}
document.write("Hypotenuse of triangle is : "+triangleHypotenuse(3,4));

function makeJuice(size)
{
function addIngredients(a,b,c){
return `The client wants a ${size} juice, containing ${a}, ${b}, ${c}`;
    }
return addIngredients("apple","ice","refreshing water")
}
let s = prompt("Enter the desired beverage size(large/medium/small) : ")
document.write(makeJuice(s))


function makeJuice(size){
    let ingredients = [];
    function addIngredients(a,b,c){
        ingredients.push(a);
        ingredients.push(b);
        ingredients.push(c);
    }
addIngredients("apple","ice","refreshing water");
addIngredients("kiwi","sugar","syrup");

    function displayJuice(){
        return `The client wants a ${size} juice, containing ${ingredients.join(' ,')}.`;
        }
return displayJuice()

}
let f = prompt("Enter the desired beverage size(large/medium/small) : ")
document.write(makeJuice(s))