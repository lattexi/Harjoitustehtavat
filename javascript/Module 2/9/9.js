function even(numbers) {
    return numbers.filter(num => num % 2 === 0)
}
let originalArray = [2, 7, 4]
let evenNumbersArray = even(originalArray)

console.log("Parilliset luvut:", evenNumbersArray)