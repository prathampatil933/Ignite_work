document.getElementById('submit-button').addEventListener('click', async () => {
    const selectedLanguage = document.getElementById('language').value;
    const response = await fetch(`/hello?language=${selectedLanguage}`);
    const data = await response.json();

    if (selectedLanguage === "Error") {
        document.getElementById('result').innerHTML = data.error_message;
    } else {
        document.getElementById('result').innerHTML = data.msgText;
    }
});
