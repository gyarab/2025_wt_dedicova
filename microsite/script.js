const button = document.getElementById('sendForm');
const emailInput = document.getElementById('exampleFormControlInput1');
const textArea = document.getElementById('exampleFormControlTextarea1');
button.addEventListener('click', function () {
    emailInput.value = "";
    textArea.value = "";
});
emailInput.addEventListener('keydown', function () {
    if (event.key === "Enter") {
        emailInput.value = "";
        textArea.value = "";
    }
});
textArea.addEventListener('keydown', function () {
    if (event.key === "Enter" && event.shiftKey) {
        emailInput.value = "";
        textArea.value = "";
    }
});