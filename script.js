function shortenURL() {
    const longUrl = document.getElementById('long-url').value.trim();
    const customUrl = document.getElementById('custom-url').value.trim();
    const resultDisplay = document.getElementById('short-url');

    // Validate input
    if (!longUrl) {
        resultDisplay.innerHTML = "❌ Please enter a valid URL.";
        return;
    }

    fetch('/shorten', {  // Relative URL (works locally & on deployment)
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ long_url: longUrl, custom_url: customUrl || null })
    })
    .then(response => response.json())
    .then(data => {
        if (data.short_url) {
            resultDisplay.innerHTML = `✅ Shortened URL: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
        } else {
            resultDisplay.innerHTML = `❌ Error: ${data.detail || "Something went wrong!"}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        resultDisplay.innerHTML = "❌ Failed to connect to the server. Try again later.";
    });
}