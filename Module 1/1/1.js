function print(text) {
    console.log(text);

    var element = document.createElement('p');
    element.textContent = text;

    document.querySelector('#console-log').appendChild(element);
}

document.addEventListener('DOMContentLoaded', function() {
    print("I'm printing to console!");
});