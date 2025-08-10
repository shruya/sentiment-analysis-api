from fastapi import FastAPI, UploadFile, File
import pandas as pd
from app.groq_client import analyze_review
from app.utils import save_upload_file

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Sentiment Analysis API"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        file_path = await save_upload_file(file)
        df = pd.read_csv(file_path)

        if "review" not in df.columns:
            return {"error": "Missing 'review' column in uploaded file"}

        results = []
        for review in df["review"]:
            try:
                sentiment = analyze_review(review)
                results.append({"review": review, "analysis": sentiment})
            except Exception as e:
                results.append({"review": review, "analysis": f"Error: {str(e)}"})

        return results
    except Exception as e:
        return {"error": str(e)}