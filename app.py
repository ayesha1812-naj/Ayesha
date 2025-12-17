import streamlit as st
from PIL import Image
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="SafeChat", layout="centered")

# ---------------- CUSTOM CSS (WhatsApp UI) ----------------
st.markdown("""
<style>
.chat-you {
    background-color:#DCF8C6;
    padding:10px;
    border-radius:10px;
    margin:5px;
}
.chat-friend {
    background-color:#FFFFFF;
    padding:10px;
    border-radius:10px;
    margin:5px;
}
</style>
""", unsafe_allow_html=True)

st.title("💬 SafeChat – WhatsApp Style Messenger")
st.caption("AI Harassment Detection | Tamil | Hindi | FIR PDF")

# ---------------- SESSION ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------- HARASSMENT DATA ----------------
HARASSMENT = {
    "Sexual Harassment": {
        "keywords": ["nude", "sex", "body"],
        "law": "IPC 354A",
        "ta": "பாலியல் தொல்லை கண்டறியப்பட்டது",
        "hi": "यौन उत्पीड़न पाया गया"
    },
    "Threat": {
        "keywords": ["kill", "die"],
        "law": "IPC 506",
        "ta": "அச்சுறுத்தல் கண்டறியப்பட்டது",
        "hi": "धमकी पाई गई"
    },
    "Bullying": {
        "keywords": ["idiot", "stupid"],
        "law": "IPC 507",
        "ta": "புல்லிங் கண்டறியப்பட்டது",
        "hi": "बदमाशी पाई गई"
    }
}

# ---------------- FUNCTIONS ----------------
def detect(text):
    text = text.lower()
    for cat, data in HARASSMENT.items():
        for w in data["keywords"]:
            if w in text:
                return cat, data
    return None, None

def add_msg(sender, content):
    st.session_state.chat.append({
        "sender": sender,
        "content": content,
        "time": datetime.now().strftime("%H:%M")
    })

def generate_fir_pdf(details):
    file_name = "FIR_Report.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)
    text = c.beginText(40, 800)
    text.setFont("Helvetica", 11)

    text.textLine("FIRST INFORMATION REPORT (FIR)")
    text.textLine("------------------------------------")
    for d in details:
        text.textLine(d)

    c.drawText(text)
    c.save()
    return file_name

# ---------------- CHAT DISPLAY ----------------
st.subheader("📱 Chat")

for m in st.session_state.chat:
    if m["sender"] == "You":
        st.markdown(f"<div class='chat-you'><b>You ({m['time']}):</b> {m['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-friend'><b>Friend ({m['time']}):</b> {m['content']}</div>", unsafe_allow_html=True)

st.divider()

# ---------------- TEXT MESSAGE ----------------
msg = st.text_input("Type a message")

if st.button("📩 Send"):
    if msg:
        add_msg("You", msg)
        cat, data = detect(msg)

        if cat:
            reply = f"""🚨 {cat} Detected  
⚖ Law: {data['law']}  
🗣 Tamil: {data['ta']}  
🗣 Hindi: {data['hi']}"""
            add_msg("Friend", reply)
        else:
            add_msg("Friend", "✅ Message received safely")

        rerun()

# ---------------- IMAGE ----------------
st.divider()
st.subheader("🖼️ Send Image")

img = st.file_uploader("Upload image", type=["jpg","png"])

if img:
    image = Image.open(img)
    st.image(image)
    add_msg("You", "[Image Sent]")
    add_msg("Friend", "🚨 Obscene image detected | IT Act 67")
    rerun()

# ---------------- AUDIO ----------------
st.divider()
st.subheader("🎤 Send Audio")

audio = st.file_uploader("Upload audio", type=["mp3","wav"])

if audio:
    st.audio(audio)
    add_msg("You", "[Audio Sent]")
    add_msg("Friend", "🚨 Abusive voice detected | IPC 506")
    rerun()

# ---------------- FIR PDF ----------------
st.divider()
st.subheader("📄 FIR PDF Generator")

name = st.text_input("Victim Name")
incident = st.text_area("Incident Description")

if st.button("Generate FIR PDF"):
    details = [
        f"Victim Name: {name}",
        f"Date: {datetime.now()}",
        f"Incident: {incident}",
        "Action Requested: Legal action under IPC & IT Act"
    ]
    pdf = generate_fir_pdf(details)
    with open(pdf, "rb") as f:
        st.download_button("⬇️ Download FIR PDF", f, file_name=pdf)

# ---------------- PANIC ----------------
st.divider()
st.subheader("🚨 Panic Alert")

num = st.text_input("Emergency Contact Number")

if st.button("Send Panic Alert"):
    st.success(f"Panic alert sent to {num} (Demo)")

# ---------------- HELP ----------------
st.divider()
st.subheader("📞 Legal Help")

st.markdown("- Cyber Crime: https://cybercrime.gov.in")
st.markdown("- Women Helpline: 1091")