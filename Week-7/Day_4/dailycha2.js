// function getCarHonda(Inventory) {
//     for (let i = 0; i < Inventory.length;i++){
//         if (Inventory[i].car_make == "Honda"){
//             return `This is a car ${Inventory[i].car_make} ${Inventory[i].car_model} from ${Inventory[i].car_year}`
//         }
       
//     }
// };

function sortCarInventoryByYear(carInventory){
    let sorted = carInventory.sort()
    let sortCar = sorted.sort((c1,c2) => (c1.car_year > c2.car_year) ? 1 : (c1.car_year < c2.car_year)? -1 : 0)
    return sortCar;
    
}

function getCarHonda(carInventory){
    let CarHonda = carInventory.filter((car) => { return car.car_make === "Honda" })
    return `This is a ${CarHonda[0].car_make} ${CarHonda[0].car_model} from ${CarHonda[0].car_year}.`
}


// let Inventory2 = Inventory.map()
const Inventory = [
    { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
    { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
    { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
    { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
    { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];
// let result = getCarHonda(Inventory)
console.log(getCarHonda(Inventory))
console.log(sortCarInventoryByYear(Inventory))




