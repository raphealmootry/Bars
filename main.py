import streamlit as st
import google.generativeai as genai
import os

# 1. Setup Gemini API
# Store your key in Streamlit Secrets for security when deploying
# For local testing, you can use: os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')

st.title("🎤 16-Bar Rap Architect")
st.markdown("Reformat your thoughts into a 16-bar verse in the style of your favorite legends.")

# 2. Artist & Rhyme Scheme Logic
# In a real app, you'd store the 'logic' or 'analysis' from the screenshots here
artist_options = {
    
    "Kendrick Lamar (HUMBLE style)": "Uses extended AAAA multi-syllabic end rhymes with roughly 11 syllables per line. Employs internal rhymes on beats 2 and 3, and utilizes repetitive word anchors (tails) at the end of bars for rhythmic emphasis.",
    "MF DOOM": "Dense holorimes, unconventional word breaks, every word rhymes.",
    "Drake": "AABB or ABAB, conversational flow, emphasis on end-rhymes.",
    "Custom Artist": "Paste your own analysis or upload a screenshot."
    
}

artist_choice = st.selectbox("Choose an Artist's Rhyme Scheme:", list(artist_options.keys()))
user_text = st.text_area("Enter the text/story you want to turn into a rap:", height=200)

if st.button("Generate 16 Bars"):
    if user_text:
        with st.spinner(f"Channeling {artist_choice}..."):
            # The System Prompt is key here
            prompt = f"""
            You are an expert rap lyricist. 
            TASK: Transform the following text into a 16-bar rap verse.
            STYLE: Use the rhyme scheme and rhythmic flow characteristic of {artist_choice}.
            STYLE NOTES: {artist_options[artist_choice]}
            
            CONSTRAINTS:
            - Exactly 16 bars.
            - Fit the user's provided text into the verse logically.
            - You may add or change words to maintain the meter and rhyme scheme.
            - Mark the rhyme sounds (e.g., [A], [B]) at the end of lines for clarity.
            
            USER TEXT:
            {user_text}
            """
            
            response = model.generate_content(prompt)
            
            st.subheader(f"Your 16 Bars ({artist_choice} Style)")
            st.code(response.text, language="text")
    else:
        st.warning("Please enter some text first!")
