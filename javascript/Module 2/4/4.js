let numbers = []

while (true) {
    let num = prompt("Anna numero:")
    num = parseInt(num)

    if (num === 0) {
        break
    }
    numbers.push(num)
}

numbers.sort((a, b) => b - a)

console.log("Numerot pienimmästä suurimpaan:", numbers)