
# 🎬 Movie Recommendation App
A machine learning-powered web application that recommends movies based on user preferences using collaborative filtering, content-based filtering, or hybrid models.

# 🔍 Features
🎥 Personalized movie recommendations

🔎 Search movies by title or genre

🧠 Machine learning model for predicting user preferences

📊 Uses content-based, collaborative, or hybrid filtering

🌐 Web interface built with Flask / Django / Streamlit

🔗 Optional integration with TMDb or IMDb API for additional data

🛠️ Tech Stack
Frontend: HTML/CSS, Bootstrap / Streamlit

Backend: Python, Flask / Django

ML Models: scikit-learn, Surprise, LightFM, or custom-built recommender

Data: MovieLens dataset / TMDb API

Deployment: Heroku / Render / AWS / Streamlit Cloud

🚀 Getting Started
Prerequisites
Python 3.8+

pip package manager

Clone the repository
bash
Copy code
git clone https://github.com/MandalSusant/Movie_Recommendation_App.git
cd movie-recommender
Install dependencies
bash
Copy code
pip install -r requirements.txt
Run the app locally
bash
Copy code
python app.py
Or with Streamlit
bash
Copy code
streamlit run app.py
🧠 ML Approach
The recommendation engine supports:

Content-Based Filtering: Uses movie metadata (genres, keywords, etc.)

Collaborative Filtering: Based on user-item interaction matrix

Hybrid Model: Combines both approaches for better accuracy

# 📁 Project Structure

movie-recommender/
│
├── data/                # Raw and processed datasets
├── model/               # ML models and training scripts
├── app.py               # Main app script
├── recommender.py       # Recommendation logic
├── templates/           # HTML templates (for Flask)
├── static/              # CSS/JS/image assets
├── requirements.txt     # Project dependencies
└── README.md            # You're here!
📊 Example Screenshot

# 📦 Dataset
MovieLens Dataset (GroupLens)

# 📸 Screenshot
![Screenshot 2025-05-17 144052](https://github.com/user-attachments/assets/34e72e01-b1ca-4bd6-a5fd-7c43b2abdd1c)


The Movie Database API (TMDb)
