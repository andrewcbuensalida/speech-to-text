from openai import OpenAI
import os
from loguru import logger
from dotenv import load_dotenv
from split_audio import split_audio_file

# Load environment variables from a .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
audio_file = open("audio_files/audio-3.mp3", "rb")

# Split the audio file into parts with the specified size limit, bitrate, and maximum duration
split_audio_file(
  input_file="audio_files/audio-3.mp3",
  output_dir="audio_files/parts",
  size_limit_mb=25,
  bitrate=128000,
  max_duration_sec=1500
)

transcription_text = ""

# Loop through the parts and transcribe each
for part in sorted(os.listdir("audio_files/parts")):
    part_path = os.path.join("audio_files/parts", part)
    with open(part_path, "rb") as audio_part:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe", file=audio_part
        )
        transcription_text += transcription.text + "\n"

# Write the combined transcription to a single file
with open("transcripts/transcription-3.txt", "w", encoding="utf-8") as file:
    file.write(transcription_text)
