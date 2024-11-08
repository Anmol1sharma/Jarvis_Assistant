# Voice Assistant "Jarvis"

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%20%7C%20GPT--4-red)

A personal voice-activated assistant, "Jarvis," built with Python, that performs tasks such as web searches, system commands, and responds conversationally using OpenAI’s ChatGPT API. Designed for hands-free interaction with an intuitive voice command interface.

---

## Features

- **Voice Activation**: Initiates on hearing the activation word, "Jarvis."
- **Web Commands**: Opens popular websites like Google, Facebook, YouTube, etc.
- **System Commands**: Performs basic OS tasks, such as opening Notepad and telling the time or date.
- **AI-Powered Responses**: Integrates ChatGPT for intelligent, conversational responses.
- **Text-to-Speech (TTS)**: Uses pyttsx3 for natural-sounding voice output.
- **Error Handling**: Reliable performance in varied acoustic conditions.

---

## Demo

![Jarvis Demo](demo.gif)

*This is a demo showing "Jarvis" performing web searches, executing system commands, and responding with AI-generated responses.*

---

## Installation

### Prerequisites

1. **Python 3.8+**
2. **OpenAI API Key**: [Get your API key from OpenAI](https://platform.openai.com/account/api-keys)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YourUsername/Jarvis-Voice-Assistant.git
    cd Jarvis-Voice-Assistant
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure API Key**:
   Replace `"YOUR_API_KEY"` in the code with your actual OpenAI API key in `main.py`.

4. **Run the assistant**:
    ```bash
    python main.py
    ```

---

## Usage

- **Activation**: Say "Jarvis" to wake the assistant.
- **Commands**:
  - **Web Commands**: "Open Google," "Open YouTube," "Search for {query}"
  - **System Commands**: "Open Notepad," "What time is it?" "What’s the date today?"
  - **AI Commands**: Unrecognized commands will be processed by ChatGPT for a response.

---

## Technologies Used

- **Python**: Core language.
- **Speech Recognition**: To recognize voice input.
- **OpenAI API**: Provides AI-powered responses.
- **pyttsx3**: For text-to-speech synthesis.
- **Web Automation**: Opens web pages via `webbrowser`.

---

## Project Structure

```plaintext
Jarvis-Voice-Assistant/
├── main.py             # Main script to run Jarvis
├── requirements.txt    # Dependencies for the project
├── README.md           # Project documentation
└── demo.gif            # (Optional) Demo animation for README
