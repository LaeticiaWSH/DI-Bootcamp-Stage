// //First part
let x = "* "
let len = prompt("Enter your number: ")
for (let i = 0;i < len;i++){
    console.log(x.repeat(i))
}

//Second part 
let leng = 6
for (let i = 1; i < 2; i++) {
    pattern = ""
    for (let j = 0; j < leng; j++){
        pattern += " *"
        console.log(pattern)
    }
}

