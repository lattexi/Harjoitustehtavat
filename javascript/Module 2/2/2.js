let nimet = []
let count = prompt("Anna osallistujamäärä: ")

for (let i = 0; i < count; i++) {
    let nimi = prompt("Anna nimi: ")
    nimet.push(nimi)
}

nimet.sort()

let outputElement = document.getElementById("output")
outputElement.innerHTML = "<ol>"

for (let i = 0; i < nimet.length; i++) {
    outputElement.innerHTML += "<li>" + nimet[i] + "</li>"
}
