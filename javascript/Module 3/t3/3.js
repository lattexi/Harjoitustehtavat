'use strict';
const names = ['John', 'Paul', 'Jones'];

let targetElement = document.getElementById("target")

let listItems = ''

for (let i = 0; i < names.length; i++) {
    listItems += `<li>${names[i]}</li>`
}

targetElement.innerHTML = listItems