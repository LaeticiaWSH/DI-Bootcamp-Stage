function checkAge(age) {
    if (age < 18) {
        const message = "Sorry, you're too young.";
        return message;
    } else {
        const message = "Yay! You're old enough!";
        return message;
}
}

console.log(checkAge(21))
function chechyear(year){
    if(year > 2000){
        const message = "You are in the 21st century"
        return message
    }else{
        const message = "You live in the Middle Age"
        return message
    }
}
console.log(chechyear(2040))


function numbers() {
    for (var i = 0; i < 5; i += 1) {
        console.log(i);
    }
    console.log(i)
};

numbers();
function multiply(a, b = 1) {
    return a * b;
}

console.log(multiply(5, 2));
//expected output: 10

console.log(multiply(5));
//expected output: 5

function getFee(isMember) {
    return (isMember ? "$2.00" : "$10.00");
}

console.log(getFee(true));
// expected output: "$2.00"

console.log(getFee(false));
// expected output: "$10.00"

console.log(getFee(1));
// expected output: "$2.00"
// because Boolean(1) is true

// const calculus = (num1,num2,sym) =>{
//     return sym === "+"? num1 + num2:
//            sym === "-" ? num1 - num2:
//            sym === "*" ? num1 * num2:
          
           
// }

// console.log(calculus(4,2,"/"));
// console.log(calculus(2, 4, "+"));

// function verify(name) {            // outer function  
//     function isJohn() {             // inner function
//         return name === "John";     // full access to argument        
//     }
//     if (isJohn()) {
//         alert("Yep, this is John");
//     }else{
//         alert("definately not john")
//     }
// }
// verify("Sara");
function addSquares(a, b) {
    function square(x) {
        return x * x;
    }
    console.log(square(a) + square(b));
}
d = addSquares(2, 3); 
e = addSquares(3, 4); 
c = addSquares(4, 5);

const hummus = function (factor) {
    const ingredient = function (amount, unit, name) {
        let ingredientAmount = amount * factor;
        if (ingredientAmount > 1) {
            unit += "s";
        }
        console.log(`${ingredientAmount} ${unit} ${name}`);
    };
    ingredient(1, "can", "chickpeas");
    ingredient(0.25, "cup", "tahini");
    ingredient(0.25, "cup", "lemon juice");
    ingredient(1, "clove", "garlic");
    ingredient(2, "tablespoon", "olive oil");
    ingredient(0.5, "teaspoon", "cumin");
};

hummus(2)

// let add = (function () {
//     let counter = 0;
//     function calculus() {
//         counter += 1;
//         return counter
//     }
//     return calculus
// })();

// // add();
// // add();
// // add();
// console.log(add());
// console.log(add());

// function outside(x) {
//     function inside(y) {
//         return x + y;
//     }
//     return inside;
// }

// let fnInside = outside(3);
// console.log(fnInside)
// function inside(y) {
//   return x + y;
// }
// console.dir(fnInside)
// // Closure (outside) x: 3

// let result = fnInside(5); // The same as calling outside(3)(5)
// console.log(result) 

const multiply = (n, m) => (n * m)
multiply(3, 4) === 12 // true

// const curryedMultiply = (n) => (m) => multiply(n, m)
// let triple = curryedMultiply(3)
// triple(4) === 12 // true