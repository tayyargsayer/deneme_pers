import streamlit as st
import google.generativeai as genai
import os

GEMINI_ANAHTARI = "AIzaSyC5_ActnFp7AW2P2r05nZVwHEP7wa8JN5A"

genai.configure(api_key=GEMINI_ANAHTARI)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_travel_recommendations(destination, duration, interests, language):
    prompt = f"""
    Act as a travel expert and provide recommendations in {language} for:
    Destination: {destination}
    Duration: {duration} days
    Interests: {interests}

    Please provide:
    1. Must-visit places
    2. Suggested itinerary
    3. Local food recommendations
    4. Travel tips
    """
    response = model.generate_content(prompt)
    return response.text

st.title("🌍 Smart Travel Assistant")
st.write("Let me help you plan your perfect trip!")

languages = {
    "English": "English",
    "Spanish": "Spanish",
    "French": "French",
    "German": "German",
    "Italian": "Italian",
    "Turkish": "Turkish"
}
selected_language = st.sidebar.selectbox("Select Output Language", list(languages.keys()))

destination = st.text_input("Where would you like to go?")
duration = st.slider("How many days will you stay?", 1, 30, 7)
interests = st.multiselect(
    "What are your interests?",
    ["History & Culture", "Nature & Adventure", "Food & Cuisine", "Shopping", "Art & Museums", "Relaxation"]
)

if st.button("Get Recommendations") and destination and interests:
    interests_str = ", ".join(interests)
    with st.spinner("Generating recommendations..."):
        recommendations = get_travel_recommendations(destination, duration, interests_str, languages[selected_language])
        st.markdown(recommendations)

st.sidebar.markdown("""
## About
This Smart Travel Assistant uses Google's Gemini AI to provide personalized travel recommendations.
Just input your destination, duration, and interests to get started!
""")