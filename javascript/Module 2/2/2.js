let nimet = []
let count = prompt("Anna osallistujamäärä: ");

for (let i = 0; i < count; i++) {
    let nimi = prompt("Anna nimi: ");
    nimet.push(nimi)
}

let outputElement = document.getElementById("output");
outputElement.innerHTML = "Osallistujat:<br>";
for (let i = 0; i < nimet.length; i++) {
    outputElement.innerHTML += nimet[i] + "<br>";
}