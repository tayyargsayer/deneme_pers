import streamlit as st
import google.generativeai as genai
import os

GEMINI_ANAHTARI = "AIzaSyC5_ActnFp7AW2P2r05nZVwHEP7wa8JN5A"

genai.configure(api_key=GEMINI_ANAHTARI)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_plant_care_recommendations(plant_type, environment, issues, language):
    prompt = f"""
    Act as a plant care expert and provide recommendations in {language} for:
    Plant Type: {plant_type}
    Environment: {environment}
    Issues: {issues}

    Please provide:
    1. General care tips
    2. Watering schedule
    3. Light requirements
    4. Common issues and solutions
    
    Output Language: {language}
    """
    response = model.generate_content(prompt)
    return response.text

st.title("🌿 Smart Plant Care Assistant")
st.write("Let me help you take care of your plants!")

languages = {
    "Azeri ": "Azerbaycan",
    "Spanish": "Spanish",
    "French": "French",
    "German": "German",
    "Italian": "Italian",
    "Turkish": "Turkish"
}
selected_language = st.sidebar.selectbox("Select Output Language", list(languages.keys()))

plant_type = st.text_input("What type of plant do you have?")
environment = st.text_input("Describe the environment (e.g., indoor, outdoor, humid, dry)")
issues = st.multiselect(
    "What issues are you facing?",
    ["Yellow leaves", "Wilting", "Pests", "Fungal infections", "Slow growth", "Other"]
)

if st.button("Get Recommendations") and plant_type and environment:
    issues_str = ", ".join(issues)
    with st.spinner("Generating recommendations..."):
        recommendations = get_plant_care_recommendations(plant_type, environment, issues_str, languages[selected_language])
        st.markdown(recommendations)

st.sidebar.markdown("""
## About
This Smart Plant Care Assistant uses Google's Gemini AI to provide personalized plant care recommendations.
Just input your plant type, environment, and issues to get started!
""")