import pickle
import numpy as np

class FakeNewsDetector:
    def __init__(self):
        with open('model.pkl', 'rb') as f:
            self.model, self.tfidf = pickle.load(f)
    
    def extract_features(self, text):
        # Convert to lowercase
        text = text.lower()
        
        # Count suspicious patterns
        suspicious_patterns = [
            'money tree', 'magical', 'secret', 'conspiracy',
            'government officials', 'shocking', 'miracle',
            'hidden', 'banned', 'censored', 'impossible'
        ]
        pattern_count = sum(1 for pattern in suspicious_patterns if pattern in text)
        
        # Count exclamation marks
        exclamation_count = text.count('!')
        
        return np.array([pattern_count, exclamation_count])
    
    def predict(self, text):
        # Extract features
        text_features = self.tfidf.transform([text])
        additional_features = self.extract_features(text)
        
        # Combine features
        X = np.hstack([
            text_features.toarray(),
            additional_features.reshape(1, -1)
        ])
        
        # Predict
        proba = self.model.predict_proba(X)[0]
        is_real = proba[1] > 0.4  # Lower threshold to be more sensitive to fake news
        confidence = float(proba[1] if is_real else proba[0])
        
        return {
            'label': 'Real' if is_real else 'Fake',
            'confidence': confidence * 100
        }