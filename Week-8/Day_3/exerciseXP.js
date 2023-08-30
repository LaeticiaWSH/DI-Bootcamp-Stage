//Exercise 1 : Giphy API
let q = "hilarious"
let rating = "g"
let api_key ="hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
const Url = `https://api.giphy.com/v1/gifs/search?q=${q}&rating=${rating}&api_key=${api_key}`;

fetch(Url)
    .then(response => response.json())
    .then(data => console.log(data["data"]))
    .catch(error => console.error('Error:', error));

//Exercise 2 : Giphy API
q = "sun"
let limit = 10
let offset = 2

const apiUrl = `https://api.giphy.com/v1/gifs/search?q=${q}&limit=${limit}&offset=${offset}&api_key=${api_key}`;

fetch(apiUrl)
    .then(response => response.json())
    .then(data => console.log(data["data"]))
    .catch(error => console.error('Error:', error));

//Exercise 3 : Async Function

const fetchdata = async(endpoint) =>{
    try{
        const response = await fetch(endpoint);
        let result = await response.json();
        return result.result["properties"];
    }catch(error){
        console.log(error);
    }
}


async function main(){
    let endpoint = "https://www.swapi.tech/api/starships/9/"
    for(let i = 0; i<11; i++){
        const data = await fetchdata(endpoint);
        console.log(data)
    }
}
main()

//Exercise 4: Analyze
function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();
