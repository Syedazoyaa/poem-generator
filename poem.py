import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI with your API key
genai.configure(api_key="AIzaSyDl2nIaYT9ef8vJ6NDhXnIOUj-Z_UmYfXU")  # Replace with your actual API key

# Function to load the Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.0-pro")
chat = model.start_chat(history=[])

def get_gemini_response(user_input):
    try:
        question = f"Write a poem about {user_input}.. generate it in the form of stanzas to visually make it look as poem an also give the heading as ' A POEM ON {user_input}'"
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"Error: {e}")

# Initialize Streamlit app
st.set_page_config(page_title="poem.AI")
st.header("POEM.AI")

# Add custom CSS for background image and fancy elements
st.markdown(
    """
    <style>
    .stApp {
        background: url('poembg.png');
        background-size: cover;
    }
    .stTextInput > div > div > input {
        border: 2px solid #00ADB5;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        color: #393E46;
    }
    .stButton > button {
        background-color: #00ADB5;
        color: #FFFFFF;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #393E46;
        color: #FFFFFF;
    }
    .stMarkdown > div > h2 {
        color: #00ADB5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# User input for the content topic
user_input = st.text_input("Enter a topic for your poem:", key="user_input")
submit = st.button("Generate Poem")

if submit and user_input:
    response = get_gemini_response(user_input)
    if response:
        st.subheader("Generated Poem")
        for chunk in response:
            st.write(chunk.text)
    else:
        st.error("Failed to get a response. Please try again later.")
elif submit and not user_input:
    st.warning("Please input a topic before submitting.")
