let targetElement = document.getElementById("target")

let item1 = document.createElement("li")
item1.textContent = "First item"

let item2 = document.createElement("li")
item2.textContent = "Second item"

let item3 = document.createElement("li")
item3.textContent = "Third item"

item2.classList.add("my-item")

targetElement.appendChild(item1)
targetElement.appendChild(item2)
targetElement.appendChild(item3)