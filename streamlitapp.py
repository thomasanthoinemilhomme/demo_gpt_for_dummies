import streamlit as st

# Custom styles to mimic ChatGPT and apply the black & yellow theme
st.markdown("""
<style>
    /* Base layout and color styling */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #333; /* Dark background */
        color: #ffcc00; /* Yellow text */
    }
    /* Styling the text input and button */
    .stTextInput > div > div > input {
        background-color: #000; /* Black input field */
        color: #ffcc00; /* Yellow text */
    }
    .stButton > button {
        background-color: #ffcc00; /* Yellow button */
        color: #333; /* Black text */
    }
</style>
""", unsafe_allow_html=True)

# Set the page config to modify the page title and favicon
st.set_page_config(page_title="GPT for Dummies", layout="wide")

# Title of the app
st.title("GPT for Dummies")

# Input prompt from the user
user_input = st.text_input("Please enter your prompt:")

# Button to process the input
if st.button("Submit"):
    # Response to be displayed after submission
    st.write("I'm broke I can't afford OpenAI API, please hire me ;)")

# To run the app, save this script as `app.py` and execute `streamlit run app.py` in your terminal.
