// var section = document.querySelector('./listPlanets');
// var div = document.createElement('div');
// div.textContent = 'A planet';
// section.appendChild(div);

const planets ={
    mercury: { color: "#1a1a1a " ,moons : 0},
    venus: { color: "#e6e6e6", moons : 0},
    earth: { color: "#2f6a69", moons : 1 },
    mars: { color: "#993d00", moons: 2 }, 
    jupiter: { color: "#b07f35", moons: 95 },
    saturn: { color: "#b08f36", moons: 146 },
    uranus: { color: "#5580aa", moons: 27 },
    neptune: { color: "#366896", moons: 14 }
}

for (let planet in planets) {
    console.log(planet)
    let planetDiv = document.createElement("div");
    //let moonDiv = document.createElement("div");
    planetDiv.className = "planet " + planet;
    //moonDiv.className = "moon " + planet;
    planetDiv.style.backgroundColor = planets[planet]["color"]
    //--moonDiv.style.left = planets[planet]["moons"]
    let section = document.querySelector('.listPlanets');
    section.appendChild(planetDiv);

        z = planets[planet]["moons"]
        for (let i= 0; i < z; i++){
            let moonDiv = document.createElement("div");
            moonDiv.className = "moon " + planet; 
            moonDiv.style.left = i * 15 + "px";
            planetDiv.appendChild(moonDiv);
        }

}
 
