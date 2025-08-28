# 🩺 Doctor.AI – AI-Powered Virtual Medical Assistant

**Doctor.AI** is an AI-powered virtual medical assistant that enables voice + text interactions between patients and doctors.
It leverages Speech Recognition, Large Language Models (LLMs), and Text-to-Speech to simulate realistic doctor-patient conversations, with support for multimodal queries (text + image).

⚠️ **Disclaimer:** This project is for educational and research purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

# 🚀 Features

- 🎙️ **Voice Input & Output:** Patients can speak naturally, and the doctor replies back with synthesized voice.
- 🤖 **AI-Powered Responses:** Uses Groq-hosted LLaMA models for generating medical advice.
- 🖼️ **Multimodal Support:** Accepts images + text queries (e.g., skin issues, scans).
- 🔊 **Text-to-Speech Conversion:**
  - gTTS – Lightweight, supports English + Hindi
  - ElevenLabs API – Realistic AI voices (eleven_turbo_v2)
- 💬 **Interactive UI:** Built with Gradio for seamless interaction.
- 📂 **Lightweight Setup:** Only requires dependencies from requirements.txt.


#  📂 Project Structure
```
Doctor.AI/
│
├── app.py                    # Main entry point for running the app, Gradio UI for interactions with language choice 
├── gradio_app.py             # another Gradio UI for interactions  
├── brain_of_the_doctor.py    # Core AI logic (LLM + image analysis)  
├── voice_of_the_doctor.py    # Text-to-Speech (gTTS + ElevenLabs)  
├── voice_of_the_patient.py   # Speech-to-Text (Groq Whisper API)  
├── requirements.txt          # Python dependencies  
├── presentation.pdf          # Project presentation slides  
└── README.md                 # Project documentation
```

# ⚙️ Technical Details

- Speech-to-Text (STT):
  - Model: Whisper-large-v3
  - API: Groq API

- Text-to-Speech (TTS):
  - gTTS (Google TTS) → Lightweight, bilingual (EN/HI)
  - ElevenLabs API → Natural AI voices (eleven_turbo_v2)

- Core AI Model (Doctor’s Brain):
  - Model: Meta-LLaMA 4 Scout 17B Instruct
  - API: Groq API

- Multimodal Support:
  - Image queries are base64-encoded and analyzed alongside text prompts

- Frameworks/Libraries Used:
  - Gradio – Web UI
  - speech_recognition + pydub – Audio recording & processing
  - gtts, elevenlabs – TTS engines
  - langdetect – Language detection
  - dotenv – Environment management

- Environment Variables (from .env):
```
GROQ_API_KEY=your_groq_api_key_here
ELEVEN_API_KEY=your_elevenlabs_api_key_here
```

# ⚙️ Installation

Clone the Repository
```
git clone https://github.com/your-username/Doctor.AI.git
cd Doctor.AI
```

Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

Install Dependencies
```
pip install -r requirements.txt
```

▶️ Usage
Run the app locally:
```
python app.py
```

The app will start a Gradio server at:
👉 http://127.0.0.1:7860

To create a public share link, modify launch() in gradio_app.py:
```
interface.launch(share=True)
```

# 📖 Workflow

- 🗣️ Patient speaks → converted into text via Groq Whisper-large-v3
- 🧠 AI model (LLaMA) processes query + optional image → generates doctor’s response
- 🩺 Doctor’s response → converted into speech using gTTS or ElevenLabs API
- 🎧 Output displayed in Gradio UI as text + audio playback

# 📊 Presentation

📑 See [Project Presentation](./presentation.pdf)
 for a detailed project walkthrough.

# 🤝 Contributing

Contributions are welcome! 🎉
Fork the repo, create a new branch, and submit a pull request.

# 📜 License

This project is licensed under the MIT License.
