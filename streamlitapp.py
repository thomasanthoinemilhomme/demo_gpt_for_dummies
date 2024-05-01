import streamlit as st

# Set the page config to modify the page title and favicon
st.set_page_config(page_title="GPT for Dummies", layout="wide")

# Custom styles to mimic ChatGPT and apply the black & yellow theme
st.markdown("""
<style>
    /* Base layout and color styling */
    html, body, [data-testid="stAppViewContainer"], .css-1d391kg, .css-1q3eu8x, .css-15c0s9d, .css-16huue1, .css-1ojf920 {
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

# Title of the app
st.title("GPT for Dummies")

# Input prompt from the user
user_input = st.text_input("Please enter your prompt:")

# Button to process the input
if st.button("Submit"):
    # Initial response
    st.write("Response based on the user's input goes here.")

    # Ask user if they want detailed guide on obtaining OpenAI API
    detailed_guide = st.radio(
        "Do you want me to guide you through in detail about how to get API from OpenAI?",
        ('Yes', 'No, I\'m alright'),
        index=1  
         if detailed_guide=='Yes':
            st.write("""
                There isn't an official way to obtain a free API token for using OpenAI's ChatGPT as part of a service or product integration. OpenAI typically charges for API usage based on the number of tokens processed, which includes both the input and output characters.
                Here are a few possibilities you might explore depending on your needs:
                - Educational or Research Grants: Sometimes, companies like OpenAI offer special programs or grants for educational purposes or research. If your project is non-commercial and aligns with educational or research goals, you might consider applying for such a program if available.
                - Free Trials or Credits: Some services offer a limited number of free credits to new users who want to try out their APIs. You'd need to check OpenAI's current offerings to see if anything like this is available.
                - Competitions or Hackathons: Participating in hackathons or competitions sponsored by OpenAI or its partners can sometimes offer free API access as part of the event.
                - Personal Use or Small Scale Testing: If your usage is minimal, the cost might be low enough to be feasible within the free credit provided by OpenAI upon account creation, or the costs might be manageable for small-scale testing.
                For the most current and detailed information, I recommend checking OpenAI's official website or contacting their support directly. They may have the latest updates on any possible free access or trial offers.
            """)# Default to 'No, I'm alright'
    )

    # Display detailed guide if user selects "Yes"
   
