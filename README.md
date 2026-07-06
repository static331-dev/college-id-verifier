# 🎓 College ID Verification using Deep Learning

## 📖 Project Overview

This project is an AI-powered College ID Verification System that detects whether a college ID card is genuine or suspicious using a Convolutional Autoencoder built with PyTorch.

The system reconstructs the uploaded ID image and calculates the reconstruction error. If the error is below a predefined threshold, the ID is classified as Genuine; otherwise, it is classified as Suspicious/Fake.

The project also includes a FastAPI backend and a simple HTML, CSS, and JavaScript frontend for real-time verification.

---

## ✨ Features

- Upload College ID Images
- AI-based Verification using Autoencoder
- Reconstruction Error Calculation
- Threshold-based Decision Logic
- FastAPI REST API
- Interactive Frontend
- Image Preview Before Verification
- Real-time Prediction Results

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI

### Deep Learning

- PyTorch
- TorchVision

### Frontend

- HTML
- CSS
- JavaScript

### Other Libraries

- Pillow
- Matplotlib
- NumPy

---

## 📂 Project Structure

```
college-id-verifier/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   └── autoencoder.pth
│
├── src/
│   ├── api/
│   ├── dataset/
│   ├── inference/
│   ├── model/
│   ├── preprocessing/
│   └── training/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/college-id-verifier.git
```

Move into the project

```bash
cd college-id-verifier
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

Start the FastAPI server

```bash
uvicorn src.api.main:app --reload
```

Open the frontend

```
frontend/index.html
```

or

Open using VS Code Live Server.

---

## 🌐 API Endpoints

### Home

```
GET /
```

Returns:

```json
{
  "message": "College ID Verification API is Running!"
}
```

---

### Verify ID

```
POST /verify
```

Input:

- Image File

Returns:

```json
{
    "prediction": "Genuine ID",
    "reconstruction_error": 0.032652
}
```

---

## 🧠 Model Pipeline

```
Upload Image
       │
       ▼
Image Preprocessing
       │
       ▼
Autoencoder
       │
       ▼
Reconstruction Error
       │
       ▼
Threshold Decision
       │
       ▼
Prediction
```

---

## 🔮 Future Scope

- Train on larger datasets
- Support multiple colleges
- Improve model accuracy
- Deploy the application to the cloud
- Mobile application integration

---

## 👨‍💻 Author

**Aadit Bhutani**

College ID Verification using Deep Learning with PyTorch and FastAPI.