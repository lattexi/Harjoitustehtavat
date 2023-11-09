function getUserGreeting() {
    let userName = prompt("Please enter your name:");

    if (userName) {
        let greetingMessage = `Hello, ${userName}!`;

        document.getElementById('greeting').textContent = greetingMessage;
    }
}

document.addEventListener('DOMContentLoaded', getUserGreeting);
