# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with Himanshu!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

#Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

### This version is for autoplaying the audio right after generation for my own system
# import subprocess
# import platform
# from gtts import gTTS
# import os

# def text_to_speech_with_gtts(input_text, output_filepath="final.mp3"):
#     language = "en"

#     # Generate audio file (always mp3 from gTTS)
#     audioobj = gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)

#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             # Use default media player to play mp3
#             os.startfile(output_filepath)
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['xdg-open', output_filepath])  # opens default player
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

#### This version is for mixed language input (English + Hindi) and autoplaying the audio right after generation for my own system
# import subprocess
# import platform
# from gtts import gTTS
# import os
# import re

# def text_to_speech_with_gtts(input_text, output_filepath="final.mp3"):
#     """
#     Converts mixed English + Hindi text into speech.
#     Uses only gTTS + os.startfile (no ffmpeg/pydub).
#     """

#     # Split Hindi (Devanagari) vs English using regex
#     segments = re.findall(r'[\u0900-\u097F]+|[a-zA-Z0-9\s.,!?]+', input_text)

#     # Create/open final mp3 file in write-binary mode
#     with open(output_filepath, "wb") as final_file:
#         for i, seg in enumerate(segments):
#             seg = seg.strip()
#             if not seg:
#                 continue

#             # Detect language (Devanagari → hi, else en)
#             lang = "hi" if re.search(r'[\u0900-\u097F]', seg) else "en"

#             # Save each segment to temp file
#             temp_file = f"temp_{i}.mp3"
#             gTTS(text=seg, lang=lang, slow=False).save(temp_file)

#             # Append raw bytes into final file
#             with open(temp_file, "rb") as tf:
#                 final_file.write(tf.read())

#             os.remove(temp_file)  # cleanup

#     # Autoplay final audio
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             os.startfile(output_filepath)  # plays with default media player
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['xdg-open', output_filepath])
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

# This version is having billingual support with dropdown selection in Gradio app

from gtts import gTTS
import os

def text_to_speech_with_gtts(input_text, output_filepath="final.mp3", lang_mode="en"):
    from gtts import gTTS
    import os, tempfile

    # 🛑 Safety check for empty text
    if not input_text or not input_text.strip():
        input_text = "Sorry, I did not catch that." if lang_mode == "en" else "माफ़ कीजिये, मुझे कोई जवाब नहीं मिला।"

    tts = gTTS(text=input_text, lang=lang_mode, slow=False)

    # Save to a temporary file first
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        temp_path = tmp.name
    tts.save(temp_path)

    # ✅ Delete old file if it exists (Windows safe overwrite)
    if os.path.exists(output_filepath):
        os.remove(output_filepath)

    os.rename(temp_path, output_filepath)
    return output_filepath




input_text="Hi this is Ai with Himanshu, autoplay testing!"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")