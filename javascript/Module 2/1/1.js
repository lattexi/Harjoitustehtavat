let numbers = [];
for (let i = 0; i < 5; i++) {
    let num = prompt(`Enter number ${i + 1}:`);
    numbers.push(num);
}

let outputElement = document.getElementById("output");
outputElement.innerHTML = "Numerot:<br>";
for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
    outputElement.innerHTML += numbers[i];
}
