import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_review(review):
    prompt = f"""
    Review: "{review}"

    Identify the sentiment as Positive, Negative, or Neutral, and give a very short reason (1 line).

    Respond ONLY in the following JSON format:
    {{
      "sentiment": "...",
      "reason": "..."
    }}
    """

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that analyzes sentiment in short text."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print("Groq Error Response:", response.text)
        response.raise_for_status()

    result = response.json()
    content = result['choices'][0]['message']['content']

    try:
        parsed = eval(content)  # Groq returns stringified dict
        return {
            "sentiment": parsed.get("sentiment", "").strip(),
            "reason": parsed.get("reason", "").strip()
        }
    except Exception as e:
        print("Parsing error:", e)
        return {
            "sentiment": "Unknown",
            "reason": "Could not parse Groq response."
        }