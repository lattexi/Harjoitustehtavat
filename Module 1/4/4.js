function karkausvuosi() {

    let year = parseInt(prompt("Syötä vuosi:"), 10);

    let isLeapYear = (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0));

    document.getElementById("result").innerHTML =
        isLeapYear ? year + " on karkausvuosi." : year + " ei ole karkausvuosi.";
}