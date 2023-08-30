// //1rst Daily Challenge
// function sortWords(list) {
//     return new Promise((resolve, reject) => {
//         if (list.length > 4) {
//             let list2sorted = list.map(word => word.toUpperCase()).sort()
//             resolve(list2sorted)
//         }else{
//             reject("The array is not long enough.")
//         }
//     })
// }

// function makeAllCaps(list){
//     let str = 0
//     return new Promise((resolve,reject) =>{
//         for(let i = 0; i < list.length; i++){
//             if (typeof(list[i]) === "string"){
//                 str = str + 1
//             }else{
//                 str = str + 0
//             }
//         }
//         if (str  == list.length){
//             resolve(list.map(word => word.toUpperCase()));
//         }else{
//             reject("It is being rejected because not all the words are string.");
//         }
//     })
// }

// // //in this example, the catch method is executed
// makeAllCaps([1, "pear", "banana"])
//     .then((arr) => sortWords(arr))
//     .then((result) => console.log(result))
//     .catch(error => console.log(error))

// makeAllCaps(["apple", "pear", "banana"])
//     .then((arr) => sortWords(arr))
//     .then((result) => console.log(result))
//     .catch(error => console.log(error))

// makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//     .then((arr) => sortWords(arr))
//     .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
//     .catch(error => console.log(error))

//2nd Daily Challenge

const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`
 
function toJs(){
    let morse2 = JSON.parse(morse)
    return new Promise((resolve, reject) => {
        if (Object.keys(morse2).lenght === 0){
            reject(error("Object empty."))
        }else{
            resolve(morse2)
        }
})
}
function toMorse(morseJS){
    prompt("Enter a word or a sentence: ")
    for (key in )
}
toJs()
    .then((result) => console.log(result))
    .catch((error) => console.log(error))