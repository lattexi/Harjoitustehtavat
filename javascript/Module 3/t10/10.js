let form = document.getElementById('source')
form.addEventListener('submit', (event) => {

    event.preventDefault()

    let firstName = form.querySelector('[name="firstname"]').value
    let lastName = form.querySelector('[name="lastname"]').value

    let target = document.getElementById('target')
    target.textContent = `Your name is ${firstName} ${lastName}`
})
