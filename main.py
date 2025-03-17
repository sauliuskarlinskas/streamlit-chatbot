

import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
import streamlit as st
import pandas as pd
import fitz  # PyMuPDF for PDF processing
from PIL import Image

st.title("ChatGPT klonas su failų analize")

# Load environment variables from .env file
load_dotenv()

# Access the secret
secret_key = os.getenv("GITHUB_TOKEN")

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Tu esi pokalbių asistentas, atsakyk lietuviškai."}]

# Role mapping
role_mapping = {"user": "Aš", "assistant": "Gudruolis"}

# Display chat messages from history in a bordered container
with st.container():

    # Using a scrollable expander for chat messages
    with st.expander("Pokalbių istorija", expanded=True):
        for message in st.session_state.messages:

            # Skip displaying the specific system message content
            if message["content"] == "Tu esi pokalbių asistentas, atsakyk lietuviškai.":
                continue  # Skip this message

             # Assign role display names
            role_display = role_mapping.get(message["role"], message["role"].capitalize())

             # Assign color based on the role
            message_color = "color: blue;" if message["role"] == "user" else "color: green;"

            # Display messages with the assigned color
            st.markdown(f'<p style="{message_color}"><strong>{role_display}:</strong> {message["content"]}</p>', unsafe_allow_html=True)

# File Upload Section
uploaded_file = st.file_uploader("Įkelkite failą analizei", type=["txt", "csv", "pdf", "jpg", "jpeg"], accept_multiple_files=False)
file_content = ""

def process_file(file):
    if file is not None:
        if file.type == "text/plain":
            return file.read().decode("utf-8")
        elif file.type == "text/csv":
            df = pd.read_csv(file)
            return df.to_string()
        elif file.type == "application/pdf":
            pdf_reader = fitz.open(stream=file.read(), filetype="pdf")
            text = "\n".join([page.get_text("text") for page in pdf_reader])
            return text
        elif file.type in ["image/jpeg", "image/jpg"]:
            img = Image.open(file)
            st.image(img, caption="Įkelta nuotrauka", use_column_width=True)
            return "JPG nuotrauka įkelta."
    return None

if uploaded_file:
    file_content = process_file(uploaded_file)
    if file_content:
        st.text_area("Failo turinys:", file_content, height=200)
        st.session_state.messages.append({"role": "user", "content": f"Analizuok šį failą: {file_content}"})


# Chat input
if prompt := st.chat_input("Kas gero?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(f"**{role_mapping['user']}**: {prompt}")  

    # Generate assistant response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    # Append assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
