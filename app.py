from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

# Load model and vectorizer
model = load("models/model.pkl")
vectorizer = load("models/vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        # Convert the entered URL into vector
        data = vectorizer.transform([url])
        prediction = model.predict(data)[0]
        if prediction == 1:
            result = "⚠️ This is a Phishing Website!"
        else:
            result = "✅ This is a Safe Website."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
