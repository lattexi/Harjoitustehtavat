function print(text) {
    console.log(text);

    let element = document.createElement('p');
    element.textContent = text;

    document.querySelector('#console-log').appendChild(element);
}

print("I'm printing to console!")