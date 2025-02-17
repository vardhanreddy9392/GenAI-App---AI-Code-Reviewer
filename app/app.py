import streamlit as st
import google.generativeai as genai
import configparser

# Load API key from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

api_key = "AIzaSyBzzz-k6aJrkPuutNiU_LGh8_SXVNyxnSM"  # Directly assigning the API key

genai.configure(api_key=api_key)

def review_code(code_snippet: str) -> str:
    """Calls Gemini AI model to review the provided code."""
    prompt = f"Review the following code and suggest improvements:\n\n{code_snippet}"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text if response else "No response from AI."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🔍 AI Code Reviewer (Powered by Gemini AI)")
st.markdown("Paste your code below, and AI will provide a review with suggestions.")

code_input = st.text_area("Paste your code here:", height=300)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing code..."):
            review_result = review_code(code_input)
        st.subheader("AI Review & Suggestions:")
        st.write(review_result)
    else:
        st.warning("Please enter some code for review.")
