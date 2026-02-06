import streamlit as st
import requests
import uuid

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Doctor–Patient Translator", layout="centered")

st.title("🩺 Doctor–Patient Translation App")

# ---- Session State ----
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

# ---- Role Selection ----
role = st.selectbox("Select your role", ["doctor", "patient"])
target_lang = st.text_input("Translate to language (e.g. Hindi, French)", "Hindi")

# ---- Text Translation ----
st.subheader("💬 Text Translation")

text = st.text_area("Enter message")

if st.button("Translate"):
    payload = {
        "conversation_id": st.session_state.conversation_id,
        "sender_role": role,
        "text": text,
        "to_lang": target_lang
    }

    res = requests.post(f"{BACKEND_URL}/translate", json=payload)

    if res.status_code == 200:
        st.success("Translated Text")
        st.write(res.json()["translated_text"])
    else:
        st.error("Translation failed")

# ---- Audio Upload ----
st.subheader("🎙️ Record Audio (Microphone)")

audio_data = st.audio_input("Record your voice")

if audio_data:
    st.audio(audio_data)

    files = {
        "file": ("recording.wav", audio_data, "audio/wav")
    }

    res = requests.post(
        f"{BACKEND_URL}/audio/upload",
        files=files
    )

    if res.status_code == 200:
        st.success("Transcription")
        st.write(res.json()["text"])
    else:
        st.error("Audio transcription failed")


# ---- Conversation Summary ----
st.subheader("🧠 AI Medical Summary")

if st.button("Generate Summary"):
    res = requests.post(
        f"{BACKEND_URL}/summary/{st.session_state.conversation_id}"
    )

    if res.status_code == 200:
        st.success("Conversation Summary")
        st.write(res.json()["summary"])
    else:
        st.error("Summary generation failed")
