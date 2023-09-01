const sname = document.getElementById("name")
const h = document.getElementById("h")
const g = document.getElementById("g")
const b = document.getElementById("b")
const hw = document.getElementById("hw")
let searchitem = document.getElementById("look")
// let api_url = "https://www.swapi.tech/api/people/"


searchitem.addEventListener("click", (e) => {
    e.preventDefault();

    let min = Math.ceil(1)
    let max = Math.floor(83)
    let randNum = Math.floor(Math.random() * (max - min + 1)) + min
    personSearch(randNum)

})

document.addEventListener("DOMContentLoaded", function() {
    if (document.readyState !== "complete") {
        document.querySelector("#load").style.visibility = "hidden";
        document.querySelector("#loader").style.visibility = "visible";
    } else {
        document.querySelector("#loader").style.display = "none";
        document.querySelector("#load").style.visibility = "visible";
    }
});

async function personSearch(randNum){
    let url = `https://www.swapi.tech/api/people/${randNum}`
    try {
        let response = await fetch(url);
        let data = await response.json();

        let res = await fetch(data.result.properties.homeworld);
        let val = await res.json();
       
        let home = val.result.properties.name

        
        let n = data.result.properties.name;
        console.log(n)
        let height = data.result.properties.height;
        console.log(height)
        let gender = data.result.properties.gender;
        console.log(gender)
        let dob = data.result.properties.birth_year;
        console.log(dob)


        sname.innerHTML = n
        h.innerHTML = "Height: " + height;
        g.innerHTML = "Gender: " + gender;
        b.innerHTML = "Birth Year: " + dob;
        hw.innerHTML = "Home World: " + home;

    } catch (error) {
        console.log(error)
        sname.innerHTML = "Oh No!That person isn't available."
        h.innerHTML = "";
        g.innerHTML = "";
        b.innerHTML = "";
        hw.innerHTML = "";

    }
}




