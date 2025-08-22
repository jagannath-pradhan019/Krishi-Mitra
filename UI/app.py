import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input
from PIL import Image
import traceback


from api import describe_disease
from data import treatments, diseases
from data_formatting import format_name, normalize_to_list

st.set_page_config(page_title="Plant Leaf Disease Detection", layout="centered")

# Modern Header: Local Image + Title
col1, col2 = st.columns([1, 7])
with col1:
    # Adjust the path if needed for your actual image file location
    st.image("logo.png", width=70)
with col2:
    st.markdown("""
    <span style="font-size:2.2rem; font-weight:700; color:#439211;">Krishi Mitra</span><br>
    <span style="font-size:1.1rem; color: #4B8BBE;">AI-powered Plant Disease Detection & Guidance</span>
    """, unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #4B8BBE;'>", unsafe_allow_html=True)

with st.expander("ℹ️ How to use Krishi Mitra"):
    st.write("""
    - 📸 Upload a clear image of a plant leaf (single leaf, plain background recommended).
    - ⏳ The AI will analyze and classify the leaf disease.
    - 🩺 If a disease is detected, you'll get up-to-date treatment advice from AI.
    - 🍃 Healthy leaves are recognized for peace of mind!
    """)


# Treatment suggestions for each disease
def get_treatments_for_disease(disease_name):
    return treatments.get(disease_name, ["No treatment data available. Please consult an expert."])

# Model and class names (from training dataset — 38 classes)
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('plant_disease_model.keras')
    return model

model = load_model()

st.write(
    "Upload a clear image of a plant leaf and the model will identify the disease (if any). "
    "For best results, upload a single leaf image. Images not containing leaves or unclear content will show a warning if confidence is low."
)

THRESHOLD = 0.4  

uploaded_file = st.file_uploader("📁 Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Show uploaded image
        image_pil = Image.open(uploaded_file).convert("RGB")
        st.image(image_pil, caption="Uploaded Leaf Image", use_column_width=True)

        # Preprocessing
        img = image_pil.resize((224, 224))
        img_array = np.array(img)
        if len(img_array.shape) == 2:  # Grayscale
            img_array = np.stack([img_array] * 3, axis=-1)
        if img_array.shape[-1] == 4:  # RGBA to RGB
            img_array = img_array[..., :3]
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Predict
        preds = model.predict(img_array)
        probabilities = tf.nn.softmax(preds[0]).numpy()
        pred_index = int(np.argmax(probabilities))
        confidence = float(np.max(probabilities))

        # Output with threshold logic
        if confidence >= THRESHOLD:
            #To format the disease name properly
            proper_name = format_name(diseases[pred_index])
            st.success(f"🧪 **Prediction:** {proper_name}")
            st.info(f"🔍 **Confidence:** {confidence * 100:.2f}%")

            st.markdown("### 🌱 Treatments")
            treatments = get_treatments_for_disease(diseases[pred_index])
            for i, treatment in enumerate(treatments, 1):
                st.markdown(f"{i}. {treatment}")

            # AI Model Reply
            st.markdown("-----")
            with st.spinner("Generating detailed advice..."):
                causes,treatments_out,precautions = describe_disease(proper_name,treatments)
                st.markdown("### ✨ AI Suggestions")
                #The data is kind of unpredictable so this is to ensure that the reply is a List
                causes_list = normalize_to_list(causes)
                treat_list = normalize_to_list(treatments_out)
                prec_list = normalize_to_list(precautions)
                st.markdown("#### ‼️ Potential Causes")
                for i, cause in enumerate(causes_list, 1):
                    st.markdown(f"{cause}")
                st.markdown("#### 😷 Treatments")
                for i, answer in enumerate(treat_list, 1):
                    st.markdown(f"{answer}")
                st.markdown("#### ⌚ Precautions for next time")
                for i, precaution in enumerate(prec_list, 1):
                    st.markdown(f"{precaution}")

        else:
            st.warning(
                "⚠️ This image does not appear to be a plant leaf or is not recognized by the model with sufficient confidence. "
                "Please upload a clear image of a single plant leaf."
            )
    except Exception as e:
        st.error("An error occurred when processing the image or making a prediction:")
        st.exception(e)
        st.text(traceback.format_exc())
else:
    st.info("Upload an image or take a live photo to get a prediction.")