function calculate() {
    // Prompt for three integers
    let num1 = parseInt(prompt("Syötä luku: ", "0"), 10);
    let num2 = parseInt(prompt("Syötä luku: ", "0"), 10);
    let num3 = parseInt(prompt("Syötä luku: ", "0"), 10);

    let summa = num1 + num2 + num3;
    let tulo = num1 * num2 * num3;
    let keskiarvo = summa / 3;

    // Display the results
    document.getElementById("result").innerHTML =
        "Summa: " + summa + "<br>" +
        "Tulo: " + tulo + "<br>" +
        "Keskiarvo: " + keskiarvo.toFixed(2);
}

