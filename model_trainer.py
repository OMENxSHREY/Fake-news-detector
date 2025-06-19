import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle

def train_model():
    print("Loading dataset...")
    df = pd.read_csv('IFND.csv', encoding='latin1')
    
    # Feature engineering
    def extract_features(text):
        text = text.lower()
        suspicious_patterns = [
            'money tree', 'magical', 'secret', 'conspiracy',
            'government officials', 'shocking', 'miracle',
            'hidden', 'banned', 'censored', 'impossible'
        ]
        pattern_count = sum(1 for pattern in suspicious_patterns if pattern in text)
        exclamation_count = text.count('!')
        return pd.Series([pattern_count, exclamation_count])
    
    print("Extracting features...")
    X_text = df['Statement']
    additional_features = df['Statement'].apply(extract_features)
    
    # TF-IDF Vectorization with reduced features
    tfidf = TfidfVectorizer(
        max_features=3000,  # Reduced features for logistic regression
        ngram_range=(1, 2),  # Using bigrams
        stop_words='english'
    )
    X_tfidf = tfidf.fit_transform(X_text)
    
    # Combine features
    X = np.hstack([
        X_tfidf.toarray(),
        additional_features.values
    ])
    
    # Prepare labels
    y = (df['Label'].str.upper() == 'TRUE').astype(int)
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Train Logistic Regression model
    print("Training model...")
    model = LogisticRegression(
        C=1.0,
        max_iter=1000,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluate model
    print("\nModel Performance:")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Save model and vectorizer
    print("Saving model...")
    with open('model.pkl', 'wb') as f:
        pickle.dump((model, tfidf), f)
    
    print("Training completed!")

if __name__ == "__main__":
    train_model()