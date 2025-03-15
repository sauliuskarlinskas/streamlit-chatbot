

import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
import streamlit as st

st.title("ChatGPT klonas")

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

# Display chat messages from history in a bordered container
with st.container():
    # Using a scrollable expander for chat messages
    with st.expander("Pokalbių istorija", expanded=True):
        for message in st.session_state.messages:
            # Skip displaying the specific system message content
            if message["content"] == "Tu esi pokalbių asistentas, atsakyk lietuviškai.":
                continue  # Skip this message
             # Assign color based on the role
            if message["role"] == "user":
                message_color = "color: blue;"  # Blue for User
            else:
                message_color = "color: green;"  # Green for Assistant

            # Display messages with the assigned color
            st.markdown(f'<p style="{message_color}"><strong>{message["role"].capitalize()}:</strong> {message["content"]}</p>', unsafe_allow_html=True)

           # role = "User" if message["role"] == "Aš" else "Gudruolis"
            #st.markdown(f"**{role}:** {message['content']}")
   

# Chat input
if prompt := st.chat_input("Kas gero ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

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
    st.session_state.messages.append({"role": "assistant", "content": response})
