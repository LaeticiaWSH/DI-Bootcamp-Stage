// Ex 1
// My predicted output : I am John Doe from Vancouver,Canada.Latitude(49.2827, -123.1207)
const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const { name, location: { country, city, coordinates: [lat, lng] } } = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

//Ex 2
function displayStudentInfo(objUser) {
    const {first,last} = objUser
    console.log(`Your full name is ${first} ${last}`)
}

displayStudentInfo({ first: 'Elie', last: 'Schoppik' });

//Ex 3
//turn the users object into an array
const users = { user1: 18273,
     user2: 92833,
      user3: 90315 
    }
const {user1,user2,user3} = users
console.log([["user1", user1], ["user2", user2], ["user3", user3]])

//Modify the outcome of part 1, by multipling the user’s ID by 2.
console.log([["user1", user1 * 2], ["user2", user2 * 2], ["user3", user3 * 2]])

// Ex 4
// my predicted output = typeof member = object
class Person {
    constructor(name) {
        this.name = name;
    }
}

const member = new Person('John');
console.log(typeof member);

//Ex 5
class Dog {
    constructor(name) {
        this.name = name;
    }
};
// Analyze the options below. Which constructor will successfully extend the Dog class?
// my answer:
// 

class Labrador extends Dog {
    constructor(size) {
        super(name);
        this.size = size;
    }
};

//Ex 6
//[2] === [2]
// {} === {}
//My opinion : I thought it was going to be true....BUT GOD I AM WRONG

//What is, for each object below, the value of the property number and why?
const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number)
// since the object2.number = object1.number and at line 75 the object1 is set to 4 the object2.number will be 4
console.log(object3.number)
// since the object3.number = object1.number at line 72 .
console.log(object4.number)
// it just performs what line 73 told it to do.

//Create a class Animal with the attributes name, type and color. The type is the animal type
class Animal{
    constructor(name,type,color){
        this.name = name
        this.type = type
        this.color = color
    }
}
class Mamal extends Animal{
    constructor(name,type,color,soundmake){
    super(name,type,color);
    this.soundmake = soundmake
    }
    sound(){
        console.log(`The ${this.type} named ${this.name} of color ${this.color} make the ${this.soundmake} sound.`)
    }
    farmerCow(name,type,color){
        console.log(`Mooooo I'm a ${type} named ${name} and I'm ${color}`)

    }
}

let cow = new Mamal('Mitzie','cow','white and black','mooo')
cow.sound()
cow.farmerCow("Lily","cow","brown and white")

