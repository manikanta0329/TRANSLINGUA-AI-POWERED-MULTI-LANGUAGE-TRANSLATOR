import streamlit as st

st.set_page_config(page_title="TransLingua", layout="centered")

st.title("🌍 TransLingua - Language Translator")

text = st.text_area("Enter text to translate")

source_lang = st.selectbox(
    "Source Language",
    ["English", "Telugu", "Hindi", "Tamil"]
)

target_lang = st.selectbox(
    "Target Language",
    ["English", "Telugu", "Hindi", "Tamil"]
)

if st.button("Translate"):
    st.info("Translation feature will be added next step 🚀")