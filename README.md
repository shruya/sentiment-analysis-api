# Sentiment Analysis API

This project is a FastAPI-based API that uses the Groq API for sentiment analysis of customer reviews from CSV or XLSX files.  
It classifies reviews into **Positive**, **Negative**, or **Neutral**, and returns structured JSON results with sentiment scores.

---

## Features
- Upload **CSV/XLSX** files containing customer reviews.
- Process reviews using the **Groq API**.
- Get sentiment results in JSON format with scores.
- Supports batch processing for multiple reviews.
- Well-structured and easy to extend.

---

## Requirements
- Python 3.9+
- Groq API key (get it from [https://groq.com](https://groq.com))

---

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/<shruya>/<sentiment-analysis-api

2. **Move into the project folder**

   cd sentiment-analysis-api

3. **Install the required dependencies**

   pip install -r requirements.txt

4. **Set up your Groq API key as an environment variable**

   **For macOS/Linux:**

     export GROQ_API_KEY="your_api_key_here"

   **For Windows (Command Prompt):**

     setx GROQ_API_KEY "your_api_key_here"

5. **Run the FastAPI server**

   uvicorn app.app:app --reload
Once the server is running, open your browser and visit:
http://127.0.0.1:8000/docs

6. **(Optional) Test the API with the sample script**

   python test_api.py
**API Endpoints**
**POST** /analyze
Upload a CSV/XLSX file and get sentiment analysis results.

   **Example using curl:**

     curl -X POST "http://127.0.0.1:8000/analyze" \
     -F "file=@reviews.csv"

 ## Project Structure

 sentiment-analysis-api/
 │
 ├── app/
 │ ├── app.py # Main FastAPI application
 │ ├── utils.py # Helper functions
 │ └── init.py
 │
 ├── test_data/
 │ ├── reviews.csv # Sample reviews CSV for testing
 │
 ├── test_api.py # Script to test the API locally
 ├── requirements.txt # Python dependencies
 ├── README.md # Project documentation
 └── .gitignore


