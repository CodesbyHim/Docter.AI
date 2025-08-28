from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr
from langdetect import detect

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts  # bilingual version

system_prompt = """You have to act as a professional doctor..."""  # shortened for clarity


def process_inputs(audio_filepath, image_filepath, lang_choice):
    # Speech-to-text
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    # Image + LLM
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = speech_to_text_output  # fallback to conversation only

    # 🛑 Prevent empty text for TTS
    if not doctor_response or not doctor_response.strip():
        if lang_choice == "hi":
            doctor_response = "माफ़ कीजिये, मुझे कोई जवाब नहीं मिला।"
        else:
            doctor_response = "Sorry, I did not catch that."

    # Always generate TTS
    voice_of_doctor = text_to_speech_with_gtts(
        input_text=doctor_response,
        output_filepath="final.mp3",
        lang_mode=lang_choice
    )

    return speech_to_text_output, doctor_response, voice_of_doctor


# 6. Gradio UI
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath"),
        gr.Dropdown(choices=["en", "hi", "auto"], label="Voice Language", value="en")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("final.mp3")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)
