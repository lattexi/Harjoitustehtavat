function Tervehdys() {
    let nimi = prompt("Anna nimesi:");

    if (nimi) {
        let tervehdys = `Hei, ${nimi}!`;

        document.getElementById('result').textContent = tervehdys;
    }
}

Tervehdys()
