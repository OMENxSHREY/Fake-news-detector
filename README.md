# 📰 Fake News Detection App — A Truth-Seeking Machine 🔍🧠

> “In the age of algorithms, truth shouldn't be the first casualty.”

This project is a complete, end-to-end **Fake News Detection Web App** built using **Machine Learning**, **Natural Language Processing**, and **Flask**. It simulates a real-time scenario where users can input any news text and instantly get feedback on whether it’s fake or real — all wrapped in a minimalist, newspaper-inspired UI.

This is more than just a model — it's a deployable, interactive system designed with **responsibility, performance, and usability** at its core.

---

## 🎬 Live Demo (GIF Preview)

Here's how the app works in real time:

![Fake News Detection Demo](assets/Demo.gif)

> *Instant feedback, visual confidence, and a classic newspaper feel — all in one.*

---

## 🚀 Key Highlights

- 🧠 **Logistic Regression** with TF-IDF Vectorization for robust classification  
- 📊 Confidence scores with **color-coded visual cues** (green for real, red for fake)  
- 🖥️ Flask-powered backend serving real-time predictions  
- ✨ Clean, responsive, and retro-themed front-end  
- 🛠️ Modular architecture — easy to update, scale, and extend  
- 🧪 Benchmarked against SVM, Naive Bayes, and Random Forest  

---

## 📈 Model Performance

| Metric     | Score |
|------------|-------|
| Accuracy   | 90%   |
| Precision  | 91%   |
| Recall     | 87%   |
| F1 Score   | 89%   |

Trained on the **IFND (Indian Fake News Dataset)** from Kaggle, Logistic Regression was selected for its balance of **speed**, **accuracy**, and **interpretability**, making it ideal for real-time inference in production.

---

## 🛠️ Tech Stack

| Layer       | Tools                                  |
|-------------|----------------------------------------|
| Language    | Python 3.10                            |
| Backend     | Flask (REST API)                       |
| Frontend    | HTML, CSS, JavaScript                  |
| ML & NLP    | Scikit-learn, NLTK, Pandas, NumPy      |
| Styling     | Font Awesome, Bootstrap, Custom CSS    |
| Serialization | Pickle for model saving             |

---

## 🧩 Features

- 🔍 Real-time prediction of news authenticity  
- 🧼 Text preprocessing (stopword removal, lemmatization, etc.)  
- 📑 Confidence-based visual feedback  
- 🎨 UI designed to mimic a traditional news site  
- 📱 Fully responsive on desktop & mobile  
- ⚡ Blazing fast predictions thanks to lightweight modeling  

---

## 📂 Project Structure

<details>
<summary>Click to expand</summary>

FakeNewsDetector/
├── app.py # Flask app
├── model_trainer.py # Model training script
├── text_processor.py # Preprocessing functions
├── model.pkl # Serialized ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html
├── static/
│ └── style.css
│ └── script.js
├── assets/
│ └── Demo.gif # 🎬 Demo GIF


## 💡 How to Run Locally

```bash
# Clone this repo
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
Visit http://127.0.0.1:5000/ in your browser to interact with the app.
```

🧠 Learning Outcomes
This project helped me grow in:

🔠 Text data preprocessing and TF-IDF vectorization
🎯 Model selection based on real-world tradeoffs
🔁 Flask routing and rendering dynamic content
🛠️ Building modular, full-stack ML applications
🎨 User-first design in ML-driven interfaces


🌍 Real-World Applications:
📡 News verification tools for journalists
🛡️ Browser plugins for fact-checking
📱 Filtering engines for social media platforms
🎓 Educational demos for machine learning students


🔮 Future Improvements
 -Add multilingual fake news detection
 -Integrate transformer-based models (BERT)
 -Add live URL/news scraping functionality


🌟 Bonus: Why I Built This
I didn’t just want to train another model — I wanted to build something that mirrors a real-world product.

This project combines engineering precision with human-centered design. It's my proof that I can not only build smart systems — but also make them usable, responsive, and scalable for real people.


🤝 Connect with Me
Let’s collaborate or geek out on AI, NLP, or product ideas:

🔗 LinkedIn: https://www.linkedin.com/in/shrey-raghuvanshi-6575a4348/

💌 Email: shreyraghuvanshi10@gmail.com

⭐ If You Liked This...
Give it a ⭐ on GitHub!
It motivates me to keep building open-source, creative tech like this.
