# ChatGPT Clone with Streamlit and UV Pack Manager

This project is a simple **ChatGPT clone** built using Python and **Streamlit**. It provides an interactive chat interface powered by OpenAI's GPT model.

---

## 🚀 Features
- **Interactive chat interface**
- **Chat history display**
- **Seamless interaction with OpenAI API**
- **Secure authentication using environment variables**
- **Enhanced package management with UV Pack Manager**

---

## 📌 Prerequisites
Ensure you have the following installed on your system:
- **Python 3.8+**
- **pip (Python package manager)**
- **uv (UV Pack Manager)**

---

## 🛠 Installation

### 1️⃣ Clone the repository:
```sh
git clone https://github.com/your-repository/chatgpt-clone.git
cd chatgpt-clone
```
### 2️⃣ Initiate the project:
```sh
uv init
```

### 3️⃣ Create and activate a virtual environment:
```sh
uv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 4️⃣ Install the required dependencies:
```sh
uv add openai
uv add python-dotenv
uv rich
uv add streamlit
uv add pandas
uv add pandas Pillow PyMuPDF
```

### 5️⃣ Set up environment variables:
Create a `.env` file in the project directory and add your API key:
```env
GITHUB_TOKEN=your_personal_access_token_here
```
*You can generate a personal access token (PAT) by following [GitHub's instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).*

---

## ▶️ Usage
Run the Streamlit app:
```sh
streamlit run app.py
```
This will start a local web server where you can interact with the ChatGPT model.

---

## 📁 Project Structure
```
chatgpt-clone/
│-- app.py               # Main application file
│-- requirements.txt     # Required dependencies
│-- .env                 # Environment variables (not included in the repository)
│-- README.md            # Project documentation
```

---

## 📦 Dependencies
This project uses the following libraries:
- **streamlit** - For the chat UI
- **openai** - To interact with OpenAI models
- **python-dotenv** - To manage environment variables
- **rich** - For better console output formatting
- **uv** - For efficient package management

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your proposal.

---

## 📬 Contact
For any issues, please reach out via **[GitHub](https://github.com/your-repository/chatgpt-clone/issues)** or email at **sauliuskarlinskas@gmail.com**.

---

✨ **Happy Coding!** ✨

