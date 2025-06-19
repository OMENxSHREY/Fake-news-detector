document.getElementById('detectButton').addEventListener('click', function() {
    const text = document.getElementById('newsText').value;
    if (!text.trim()) {
        alert('Please enter a news article');
        return;
    }

    // Show loading animation
    this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
    this.disabled = true;
    
    // Add typewriter effect for results
    function typeWriter(element, text, speed = 50) {
        let i = 0;
        element.textContent = '';
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        type();
    }

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        const resultText = document.getElementById('resultText');
        const confidenceBar = document.getElementById('confidenceBar');
        
        resultDiv.style.display = 'block';
        
        const confidence = parseFloat(data.confidence);
        const resultString = `This article appears to be ${data.label.toUpperCase()} with ${confidence.toFixed(1)}% confidence`;
        
        // Apply typewriter effect to result
        typeWriter(resultText, resultString);
        resultText.className = data.label.toLowerCase();
        
        // Animate confidence bar
        confidenceBar.style.width = '0%';
        confidenceBar.style.backgroundColor = data.label === 'Real' ? '#4caf50' : '#f44336';
        setTimeout(() => {
            confidenceBar.style.width = `${confidence}%`;
        }, 100);
        
        resultDiv.scrollIntoView({ behavior: 'smooth' });
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while analyzing the article');
    })
    .finally(() => {
        // Reset button with icon
        this.innerHTML = '<i class="fas fa-search"></i> Analyze Article';
        this.disabled = false;
    });
});