from fastapi import FastAPI, UploadFile, File
import shutil
import os

from src.inference.inference import inference

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "College ID Verification API is Running!"
    }


@app.post("/verify")
async def verify(file: UploadFile = File(...)):

    # Temporary file path
    temp_path = f"temp_{file.filename}"

    # Save uploaded image
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run AI model
    prediction, error = inference(temp_path)

    # Delete temporary image
    os.remove(temp_path)

    # Return JSON
    return {
        "prediction": prediction,
        "reconstruction_error": round(error, 6)
    }