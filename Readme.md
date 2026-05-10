# Zara AI Voice Assistant

A Python-based AI Voice Assistant inspired by Alexa and Google Assistant.
Zara can open websites/apps, search the web, play music, tell news, check weather, and answer questions using OpenAI.

---

# Features

* Voice Wake Word Detection (`"Zara"`)
* Open Websites
* Open Windows Applications
* Play Songs from Custom Music Library
* YouTube Search Support
* Google Search
* Live Weather Information
* Latest News Headlines
* AI Responses using OpenAI API
* Text-to-Speech Responses

---

# Technologies Used

* Python
* SpeechRecognition
* Pyttsx3
* OpenAI API
* Requests
* Regex

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/zara-ai-assistant.git
cd zara-ai-assistant
```

---

## 2. Install Requirements

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install speechrecognition pyttsx3 requests openai regex pyaudio
```

---

# API Setup

Add your API keys inside the script:

```python
newsapi = "YOUR_NEWS_API"
weatherapi = "YOUR_WEATHER_API"
open_api = "YOUR_OPENAI_API"
```

---

# How to Run

```bash
python main.py
```

---

# Example Commands

## Websites

* "Open Google"
* "Open YouTube"
* "Open GitHub"

## Applications

* "Open Calculator"
* "Open CMD"
* "Open Notepad"

## Music

```text
Play Shape of You
```

## Search

```text
Search Python tutorials
```

## Weather

```text
What's the weather in Lahore
```

## News

```text
Tell me the news
```

---

# Project Structure

```text
├── main.py
├── musicLibrary.py
├── README.md
└── requirements.txt
```

---

# Future Improvements

* GUI Interface
* Better Wake Word Detection
* AI Memory
* WhatsApp Automation
* Spotify Integration
* Smart Home Controls

---

# Author

Wahab Saafdar

---

# License

This project is open-source and free to use.
