let api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
let searchform = document.getElementById("searchform")
let searchinput = document.getElementById("searchinput")
let gifimg = document.getElementById("imageGif")
let deleteAll = document.getElementById("deleteAll")

searchform.addEventListener("submit", (e) => {
    e.preventDefault();
    let searchitem = searchinput.value;
    console.log(searchitem)
    fetchGif(searchitem);
}
)

function delchGif() {
    gifimg.innerHTML = ""
}

deleteAll.addEventListener("click", delchGif)
// this cannot be used as parameter in line 42 as the gifContainer
// is not accessible outside the function.
// function removeitem(){
//     gifContainer.remove()
// }

async function fetchGif(searchitem) {
    console.log(searchitem)

    const url = `https://api.giphy.com/v1/gifs/random?tag=${searchitem}&api_key=${api_key}`
    console.log(url)
    try {
        let response = await fetch(url);
        let data = await response.json();
        console.log(data)
        const gifUrl = data.data.images.original.url
        console.log(gifUrl)

        const gifContainer = document.createElement("div")
        const imgif = document.createElement("img")
        const del = document.createElement("button")
        del.innerHTML = "Delete"
        del.addEventListener("click",() =>{
            gifContainer.remove()
        })
        imgif.src = gifUrl
        gifimg.appendChild(gifContainer)
        gifContainer.appendChild(imgif)
        gifContainer.appendChild(del)
    } catch (error) {
        console.log(error)
        console.log("An error occurred during the hunt.")
    }
}
