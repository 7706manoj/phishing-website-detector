import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

# Load data
data = pd.read_csv("data/urls.csv")

# Split into input (X) and output (y)
X = data["url"]
y = data["label"]

# Convert URLs into numbers using CountVectorizer
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split data for training
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Create and train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save both model and vectorizer
dump(model, "models/model.pkl")
dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model training complete! Model saved in 'models/' folder.")


