//Exercise 1 : Find The Numbers Divisible By 23
function displayNumbersDivisible(){
    let sum = []
    for(let i = 0;i < 501;i++){
        if (i % 23 == 0){
            sum.push(i)
            console.log(i)
        }
    }
    let add = 0
    for (x of sum){
        add += x
    }
    console.log(add)
}
displayNumbersDivisible()