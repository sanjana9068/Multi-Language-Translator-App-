import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Multi-Language Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------- 🎨 COLORFUL UI ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ffecd2, #fcb69f);
}

h1 {
    color: #4b0082;
    text-align: center;
}

textarea {
    font-size: 16px !important;
    border-radius: 10px !important;
}

.stButton>button {
    background-color: #6a5acd;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Multi-Language Translator")

# ---------- LANGUAGE LIST ----------
languages = {
    "Auto Detect": "auto",

    # Indian Languages
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Odia": "or",
    "Assamese": "as",

    # World Languages
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Italian": "it",
    "Turkish": "tr",
    "Dutch": "nl"
}

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("✏️ Source")

    source_lang = st.selectbox(
        "Select Source Language",
        list(languages.keys())
    )

    source_text = st.text_area(
        "Enter text",
        height=200,
        placeholder="Type any language text..."
    )

with col2:
    st.subheader("🌐 Target")

    target_lang = st.selectbox(
        "Select Target Language",
        list(languages.keys())[1:]  # auto remove
    )

# ---------- TRANSLATE ----------
if st.button("✨ Translate"):
    clean_text = source_text.strip()

    if clean_text == "":
        st.warning("⚠️ Please enter some text")
    else:
        try:
            translated_text = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(clean_text)

            st.success("✅ Translation Successful")

            st.text_area(
                "Translated Output",
                value=translated_text,
                height=200,
                disabled=True
            )

            st.code(translated_text)

        except Exception as e:
            st.error("❌ Translation failed. Try again.")