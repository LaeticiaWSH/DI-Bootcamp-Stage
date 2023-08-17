let addressNumber = 24
let addressStreet = "Cross and Redoute St"
let country = "Mauritius"

let globalAddress = addressNumber + addressStreet + " " + country
console.log(globalAddress)

let birth_year = 2003
let future_year = 2024
let possible_age = future_year - birth_year
let display  = ` I will be ${possible_age} years old in ${future_year}.`
console.log(display)
console.log(1 === '1') //false
console.log(1 == "1") //True

let x = 3
x = ++x
console.log (x)

let array = ['cat', 'dog', 'fish', 'rabbit', 'cow']
console.log(array.slice(1,2))
console.log (array.splice(3,1,"horse"))
console.log (array)
console.log(array.length)

let treasure = {
    username :"Laëticia",
    password : "Lolipop54"
}
let database = [treasure]
console.log(database)

newsfeed = [
    {
        username: "Laëticia",
        timeline : "2023"
    }
      ,{
        username: "Laëticia",
        timeline: "2023"
    },
      {
        username: "Laëticia",
        timeline: "2023"
    }
]
console.log(newsfeed)

// let age = prompt('How old are you?');
// alert(`You are ${age} years old!`);

// if (age < 18) {
//     alert("Sorry, you are too young to drive this car. Powering off")
// } else if (age == 18 ){
//     alert("Congratulations on your first year of driving. Enjoy the ride!")
// }else if(age > 18){
//     alert("Powering On. Enjoy the ride!")
// }

let a = 2 + 2;

// switch (a) {
//     case 3:
//         alert('Too small');
//         break;
//     case 4:
//         alert('Exactly!');
//         break;
//     case 5:
//         alert('Too large');
//         break;
//     default:
//         alert("I don't know such values");
// }

for (let i = 0; i < 2; i++) {
    console.log("the current number is " + i)
}
for (let i = 0; i < 16; i++) {
    if ((i % 2) === 0){
        console.log(i + " is even")
    } else if ((i % 2) != 0){
        console.log(i + " is odd")
    }
}

let names= ["john", "sarah", 23, "Rudolf",34]
// for( let i = 0; i < names.length;i++){
//         let item = names[i]
//     if (typeof(item) == 'string'){
//         if (item.charAt(0)!= item.charAt(0).toUpperCase){
//             item = item.charAt(0).toUpperCase() +item.slice(1);
//             console.log(item)
//         }
//     }else if(typeof(item) != 'string'){
//          continue;
//     }
// }
for (let i = 0; i < names.length; i++) {
    let item = names[i]
    if (typeof (item) == 'string') {
        console.log(item)
    }else {
        break;

    }
}

        
