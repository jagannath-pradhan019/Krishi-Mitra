# Krishi Mitra: Plant Leaf Disease Detection

<p align="center">
  <img src="Screenshots/logo.png" width="300" />
</p>


**Krishi Mitra** is an AI-powered web application for rapid detection of plant leaf diseases from images, with actionable guidance for crop management. It leverages deep learning and a local LLM (large language model) for natural language treatment advice.

---

## Overview

Krishi Mitra streamlines crop disease identification through a simple, menu-driven web interface built with Python and Streamlit. Users can upload a plant leaf image, and the system detects the disease and instantly suggests causes, treatments, and precautions.

The backend uses a pretrained ResNet CNN model for image classification. For each detected disease, the app calls a local LLM via an API to generate advice based on the data provided for treatments and best practices.

---

## Features

- **AI-powered disease prediction** from plant leaf images
- **Treatment and prevention guidance** generated via local LLM API
- **Comprehensive disease coverage** for crops like apple, corn, grape, tomato, and more
- **Clean and modern interface** with custom logo
- **Extensible dataset** for new crops and diseases

---

## Technologies Used

- Python (TensorFlow, NumPy, PIL)
- Streamlit (web UI)
- Custom API for LLM-based recommendations (`api.py`)
- Dataset of plant diseases and treatments (`data.py`)
- ResNet50 model pretrained for leaf disease classification

---

## File Structure

- `app.py` — Main Streamlit app (user interface & ML inference)
- `api.py` — Handles requests to local LLM for natural language disease reporting
- `data.py` — Store known diseases & treatment recommendations
- `data_formatting.py` — Utility functions for formatting and normalization
- `logo.jpg` — App logo displayed in UI

---

## Installation

1. **Clone the repository:**
git clone https://github.com/yourusername/krishi-mitra.git
cd krishi-mitra


2. **Install dependencies:**
pip install -r requirements.txt



3. **Set up the local LLM API**  
– The backend needs access to your local LLM server, set by default to `http://localhost:11434/api/generate` in `api.py`.  
– Make sure the model name and endpoint match your LLM installation.

---

## Usage

1. **Launch the app:**
streamlit run app.py


2. **Navigate to the provided local URL (e.g., http://localhost:8501)**

3. **Upload a clear leaf image**  
– The app will automatically predict the disease and display:
  - Disease name
  - Causes and biological context
  - Treatments
  - Precautions

4. **Review AI-generated advice** and implement preventive or curative steps on your crops.

---

## Supported Diseases

- Apple: Apple Scab, Black Rot, Cedar Apple Rust, Healthy
- Blueberry: Healthy
- Cherry: Powdery Mildew, Healthy
- Corn(maize): Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
- Grape: Black Rot, Esca (Black Measles), Leaf Blight, Healthy
- Orange: Haunglongbing (Citrus greening)
- Peach: Bacterial Spot, Healthy
- Pepper(bell): Bacterial Spot, Healthy
- Potato: Early Blight, Late Blight, Healthy
- Raspberry: Healthy
- Soybean: Healthy
- Squash: Powdery Mildew
- Strawberry: Leaf Scorch, Healthy
- Tomato: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy

(**See `data.py` for the full list and recommended treatments.**)

---

## Customization & Extensibility

- **Add new diseases:**  
– Edit the `diseases` list and `treatments` dictionary within `data.py`.

- **Update model or backend:**  
– Replace ResNet50 or edit `api.py` to connect with any local or hosted LLM.

- **Change logo:**  
– Replace `logo.jpg` in the project folder.

---

## Troubleshooting

- **API errors:**  
Ensure your local LLM server is running and the endpoint/server configuration matches your environment.
- **Image not processed:**  
Double check file type (JPG, PNG) and image clarity. Images must show the full leaf for accurate diagnosis.
- **Model or library issues:**  
Ensure all Python libraries and model weights are correctly installed.

---

## Requirements

- Python 3.x
- Streamlit
- TensorFlow
- Requests
- PIL
- NumPy
- Local LLM API compatible with prompt and response structure shown in `api.py`

---

## Screenshot

<p align="center">
  <img src="Screenshots/Screenshot_1.png" width="700" />
</p>
<p align="center" style="margin-top: 20px;">
  <img src="Screenshots/Screenshot_2.png" width="700" />
</p>
<p align="center" style="margin-top: 20px;">
  <img src="Screenshots/Screenshot_3.png" width="700" />
</p>
<p align="center" style="margin-top: 20px;">
  <img src="Screenshots/Screenshot_4.png" width="700" />
</p>
<p align="center" style="margin-top: 20px;">
  <img src="Screenshots/Screenshot_5.png" width="700" />
</p>
<p align="center" style="margin-top: 20px;">
  <img src="Screenshots/Screenshot_6.png" width="700" />
</p>

---

## Thank You!

Thank you for exploring **Krishi Mitra**!  
We hope this tool empowers you to protect your crops effectively and contribute to sustainable agriculture.  
Your feedback and contributions are always welcome to help us grow and improve—together we can make farming smarter and healthier!

Happy farming! 🌱🌿🚜






















