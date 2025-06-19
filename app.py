"""
Simple web application for fake news detection
"""
from flask import Flask, request, render_template, jsonify
import os
from fake_news_detector import FakeNewsDetector
import pickle
from scipy import sparse
from scipy.sparse import hstack
from text_processor import preprocess_text

app = Flask(__name__)

# Check if model exists
if not os.path.exists("model.pkl") or not os.path.exists("vectorizer.pkl"):
    print("Warning: Model or vectorizer not found.")
    print("Please run model_trainer.py first to train the model.")
    detector = None
else:
    # Initialize the detector
    detector = FakeNewsDetector()

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint for making predictions"""
    # Check if detector is initialized
    if detector is None:
        return jsonify({
            'error': 'Model not found. Please train the model first.'
        }), 500
    
    # Get the text from the request
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    # Make prediction
    result = detector.predict(data['text'])
    
    return jsonify(result)

def predict_fake_news(text):
    try:
        # Load model and vectorizer
        with open('model.pkl', 'rb') as f:
            model, vectorizer = pickle.load(f)
        
        # Preprocess text
        processed_text = preprocess_text(text)
        
        # Create features including sensational words score
        text_features = vectorizer.transform([processed_text])
        
        # Count sensational words
        sensational_words = ['magical', 'amazing', 'incredible', 'secret', 'miracle', 'unbelievable', 'shocking']
        sensational_score = sum(1 for word in text.lower().split() if word in sensational_words)
        
        # Create sparse matrix for additional features
        additional_features = sparse.csr_matrix([[sensational_score]])
        
        # Combine features
        X = hstack([text_features, additional_features])
        
        # Make prediction
        prediction = model.predict_proba(X)[0]
        is_real = prediction[1] > 0.5
        confidence = prediction[1] if is_real else prediction[0]
        
        return is_real, confidence * 100
        
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return None, None

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs("templates", exist_ok=True)
    
    # Check if index.html exists
    if not os.path.exists("templates/index.html"):
        print("Warning: templates/index.html not found.")
        print("Creating a basic template...")
        
        # Create a basic template
        with open("templates/index.html", "w") as f:
            f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Fake News Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .container {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        textarea {
            width: 100%;
            height: 200px;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 4px;
            display: none;
        }
        .real {
            background-color: #d4edda;
            color: #155724;
        }
        .fake {
            background-color: #f8d7da;
            color: #721c24;
        }
        .loading {
            display: none;
            text-align: center;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Fake News Detector</h1>
        <p>Enter a news article to check if it's real or fake:</p>
        
        <textarea id="news-text" placeholder="Paste the news article here..."></textarea>
        <button id="detect-button">Detect Fake News</button>
        
        <div class="loading" id="loading">
            Analyzing article...
        </div>
        
        <div class="result" id="result">
            <h2>Result:</h2>
            <p>This article is <span id="result-label"></span> with <span id="result-confidence"></span>% confidence.</p>
        </div>
    </div>
    
    <script>
        document.getElementById('detect-button').addEventListener('click', async function() {
            const newsText = document.getElementById('news-text').value.trim();
            
            if (!newsText) {
                alert('Please enter a news article');
                return;
            }
            
            // Show loading
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result').style.display = 'none';
            
            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: newsText })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    alert(data.error);
                    return;
                }
                
                // Update result
                const resultElement = document.getElementById('result');
                const labelElement = document.getElementById('result-label');
                const confidenceElement = document.getElementById('result-confidence');
                
                labelElement.textContent = data.label;
                confidenceElement.textContent = Math.round(data.confidence * 100);
                
                resultElement.className = 'result ' + data.label.toLowerCase();
                resultElement.style.display = 'block';
                
            } catch (error) {
                alert('An error occurred. Please try again.');
                console.error(error);
            } finally {
                document.getElementById('loading').style.display = 'none';
            }
        });
    </script>
</body>
</html>""")
    
    # Run the app
    app.run(debug=True)