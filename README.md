# 🔐 Phishing Website Detection

A Machine Learning–based web application that detects whether a given website URL is **Safe** or **Phishing**.  
The application uses a trained ML model and provides real-time predictions through a Flask web interface.

---

## 🚀 Features
- Detects phishing websites using Machine Learning
- Simple and user-friendly Flask web interface
- Real-time URL classification
- Easy to run locally for testing and learning

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Web Framework:** Flask  
- **Machine Learning:** Scikit-learn  
- **Model Serialization:** Joblib  
- **Frontend:** HTML, CSS  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure
phishing-website-detector/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── models/ # Machine learning models
│ ├── model.pkl # Trained ML model
│ └── vectorizer.pkl # URL vectorizer
│
├── templates/ # HTML templates
│ └── index.html # Main web page
│
├── static/ # Static files (CSS, JS) 
│
├── venv/ # Virtual environment (ignored by Git)
└── pycache/ # Python cache files (ignored by Git)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/7706manoj/phishing-website-detector.git
cd phishing-website-detector
2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

Activate the Environment

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
python app.py


Open your browser and visit:

http://127.0.0.1:5000

🧠 How the System Works

User enters a website URL

The URL is converted into numerical features using a vectorizer

The trained Machine Learning model predicts the result

The system displays whether the URL is Safe or Phishing

📌 Use Case

This project is useful for:

Academic mini and major projects

Understanding Flask + Machine Learning integration

Cybersecurity awareness

Placement and technical interviews

🔮 Future Enhancements

Cloud deployment (AWS / Render / Railway)

Improved accuracy using advanced ML algorithms

URL feature extraction techniques

Better UI/UX design

👨‍💻 Author

Manoj (7706manoj)
BTech – Computer Science & Engineering (AI & ML)
Aspiring Frontend & Machine Learning Developer
