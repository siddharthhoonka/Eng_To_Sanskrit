import streamlit as st
import requests
import json

# Set up Groq API key (replace with your actual key)
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Function to translate using Groq API directly
def translate_with_groq(text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",  # Updated to the current production model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate this English text to Sanskrit:\n\n{text}"}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        translated_text = result['choices'][0]['message']['content']
        return translated_text
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit UI
st.title("English to Sanskrit Translator")
st.write("Enter English text below and get the Sanskrit translation.")

text = st.text_area("Enter English text:")

if st.button("Translate"):
    if text.strip():
        with st.spinner("Translating..."):
            translation = translate_with_groq(text)
        st.subheader("Sanskrit Translation:")
        st.write(translation)
    else:
        st.warning("Please enter text to translate.")
