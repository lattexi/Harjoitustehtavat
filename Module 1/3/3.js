function calculate() {
    // Prompt for three integers
    let num1 = parseInt(prompt("Enter the first integer: ", "0"), 10);
    let num2 = parseInt(prompt("Enter the second integer: ", "0"), 10);
    let num3 = parseInt(prompt("Enter the third integer: ", "0"), 10);

    let sum = num1 + num2 + num3;
    let product = num1 * num2 * num3;
    let average = sum / 3;

    // Display the results
    document.getElementById("result").innerHTML =
        "Sum: " + sum + "<br>" +
        "Product: " + product + "<br>" +
        "Average: " + average.toFixed(2);
}2