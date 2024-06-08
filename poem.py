import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI with your API key
genai.configure(api_key="AIzaSyDl2nIaYT9ef8vJ6NDhXnIOUj-Z_UmYfXU")  # Replace with your actual API key

# Function to load the Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.0-pro")
chat = model.start_chat(history=[])

def get_gemini_response(user_input):
    try:
        question = f"Write a poem about {user_input}.. generate it in the form of stanzas to visually make it look as poem and also give the heading as ' A POEM ON {user_input}'"
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"Error: {e}")

def set_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Initialize Streamlit app
st.set_page_config(page_title="poem.AI")
st.header("POEM.AI")

# Set the background image
set_background_image("poembg.png")  # Ensure the image is in the same directory as the app

# Add custom CSS for fancy elements
st.markdown(
    """
    <style>
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
