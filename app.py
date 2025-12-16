# ==============================
# Harassment Detection App - Streamlit Cloud
# ==============================
import streamlit as st
from datetime import datetime
from PIL import Image
import os

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="Harassment Detection App",
    layout="centered"
)

st.title("🚨 AI-based Harassment Detection App")

# ------------------- Text Harassment -------------------
st.header("📝 Text Harassment Detection")
text_input = st.text_area("Enter message for analysis:")

# Simple keywords dictionary for demo
harassment_keywords = {
    "bullying": ["idiot", "loosu", "stupid"],
    "sexual": ["punda", "bitch", "sexual"],
    "threat": ["kill", "hit", "threat"],
    "hate_speech": ["hate", "dumb", "fool"]
}

detected_categories = []
for category, words in harassment_keywords.items():
    if any(word in text_input.lower() for word in words):
        detected_categories.append(category)

if detected_categories:
    st.warning(f"⚠️ Harassment Detected! Categories: {', '.join(detected_categories)}")
    st.info("📖 Applicable Laws (Demo): IPC 294, 506, 509 | IT Act 66A")
else:
    st.success("✅ No Harassment Detected")

# ------------------- Image Detection -------------------
st.header("🖼️ Image Harassment Demo")
uploaded_image = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.warning("⚠️ Image-based harassment detected (Demo)")
    st.info("📖 Applicable Laws (Demo): IPC 509 | IT Act 67")

# ------------------- Audio Detection -------------------
st.header("🎧 Audio Harassment Demo")
uploaded_audio = st.file_uploader("Upload an audio file:", type=["mp3", "wav"])
if uploaded_audio is not None:
    st.audio(uploaded_audio, format='audio/mp3')
    st.warning("⚠️ Voice harassment detected (Demo)")
    st.info("📖 Applicable Laws (Demo): IPC 506 | IPC 509")

# ------------------- Panic Alert Demo -------------------
st.header("🚨 Panic Alert Demo")
phone_number = st.text_input("Enter trusted contact number (Demo):", "+91 9876543210")
if st.button("Send Panic Alert"):
    st.success(f"📞 Panic alert sent to {phone_number} (Demo)")

# ------------------- Evidence Saving -------------------
st.header("🗂️ Evidence Locker")
if st.button("Save Text Evidence"):
    if not os.path.exists("evidence.txt"):
        with open("evidence.txt", "w", encoding="utf-8") as f:
            f.write("Timestamp | Message\n")
    with open("evidence.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {text_input}\n")
    st.success("🗂️ Evidence saved successfully (Demo)")

# ------------------- NGO Links -------------------
st.header("🔗 NGO Helplines")
st.markdown("""
- [Cyber Crime Helpline](https://www.cybercrime.gov.in)  
- [Ishant NGO](https://www.ishant.org/help)  
- [SafeCity](https://www.safecity.in)
""")