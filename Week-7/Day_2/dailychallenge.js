//let form = document.getElementById("libform")
let button = document.getElementById("lib-button")
let story = document.getElementById("story")
let shuffle = document.getElementById("shuffle")

button.addEventListener('click',getinfo)
function getinfo(event){

        let noun = document.getElementById("noun").value 
        let adjective = document.getElementById("adjective").value
        let person = document.getElementById("person").value
        let verb = document.getElementById("verb").value
        let place = document.getElementById("place").value
    if (noun == "" || adjective == "" || person == "" || verb == "" || place == ""){
    alert("Please enter values to all the blank spaces.")
    }else{
    story.textContent = `Once upon a time, there was a ${adjective} ${noun} named ${person}. They loved to ${verb} near the ${place}.`;
    event.preventDefault()
}

}
shuffle.addEventListener('click',letshuffle)
function letshuffle(event){
    let stories = [
        "Once upon a time, there was a brave ${noun} who lived in a ${place}. They were known for their ${adjective} personality and loved to ${verb} in their free time.",
        "In a ${place} far away, a ${adjective} ${noun} named ${person} lived. They had a unique talent for ${verb} and were often seen in the company of their friends.",
        "Imagine a world where ${adjective} ${noun} could ${verb}. In this world, ${person} was the most skilled ${noun} around, impressing everyone in the ${place}.",
        "Long ago, a mysterious ${noun} was discovered in a hidden ${place}. ${person} was chosen to ${verb} it and unleash its ${adjective} powers upon the world.",
        "At the edge of the ${place}, a ${adjective} ${noun} named ${person} built a sanctuary. They would often ${verb} and find solace in the quiet of nature.",
        "Legends spoke of a ${adjective} ${noun} who could ${verb} with the wind. ${person}, a traveler, embarked on a journey to find this unique ability and ended up in a magical ${place}."
    ]
    selected_story = stories[Math.floor(Math.random() * stories.length)];

    let noun = document.getElementById("noun").value
    let adjective = document.getElementById("adjective").value
    let person = document.getElementById("person").value
    let verb = document.getElementById("verb").value
    let place = document.getElementById("place").value

    function modify(selected_story){
        // "${noun}" = noun ,// "${adjective}" = adjective,// "${person}" = person,// "${verb}" = verb,// "${place}" = place// return selected_story
        selected_story = selected_story.replace(/\${noun}/g,noun)
        selected_story = selected_story.replace (/\${adjective}/g, adjective)
        selected_story = selected_story.replace(/\${person}/g, person)
        selected_story = selected_story.replace(/\${verb}/g, verb )
        selected_story = selected_story.replace(/\${place}/g, place)
        return selected_story
    }
    selected_story = modify(selected_story)
    story.textContent = selected_story
}
