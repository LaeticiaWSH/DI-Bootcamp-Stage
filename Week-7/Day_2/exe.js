i = 1
function insertRow() {
    let table = document.getElementById("sampleTable");
    let row = table.insertRow(table.rows.length);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    cell1.innerHTML = "New Cell" + i++;
    cell2.innerHTML = "New Cell";
}

function Responseonclick(event){
    if (event.type == "click")
        event.target.style.backgroundColor = "yellow"
        
        
    if (event.type == "dblclick")
        event.target.style.backgroundColor = "red"
}
document.getElementById("jsstyle").addEventListener("click", Responseonclick);
document.getElementById("jsstyle").addEventListener("dblclick", Responseonclick);
document.getElementById("div").addEventListener("click", Responseonclick);
