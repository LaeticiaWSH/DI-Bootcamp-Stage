//Exercise 1 : Comparison
function compareToTen(num){
    return new Promise((resolve,reject) => {
        if (num <= 10){
            resolve(`${num} is in the range.`);
        }else{
            reject(`${num} is out of the range.`);
        };
    });
}
//In the example, the promise should reject
compareToTen(15)
    .then(result => console.log(result))
    .catch(error => console.log(error))

//In the example, the promise should resolve
compareToTen(8)
    .then(result => console.log(result))
    .catch(error => console.log(error))

//Exercise 2 : Promises
const promise = new Promise((resolve,reject) => {
    setTimeout(() => {
        resolve();
    },4000);
})
.then((result) =>{
    console.log("Success");
})

// Exercise 3 : Resolve & Reject
const RR = new Promise((resolve,reject) => {
    setTimeout(() => {
        resolve();
    },2000);
})

const rejectRR = new Promise((resolve,reject) =>{
    setTimeout(() => {
        reject();
    },4000)
})

RR.then((result) => {
    console.log(3)
})
rejectRR.catch((result) => {
    console.log("Boo!")
})