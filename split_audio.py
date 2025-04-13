from pydub import AudioSegment
import os


def split_audio_file(input_file, output_dir, size_limit_mb=25, bitrate=128000, max_duration_sec=1500):
  """
  Splits an audio file into smaller parts based on a size limit and maximum duration.

  Args:
    input_file (str): Path to the input audio file.
    output_dir (str): Directory to save the split audio parts.
    size_limit_mb (int): Size limit for each part in MB. Default is 25MB.
    bitrate (int): Bitrate of the audio file in bits per second. Default is 128kbps.
    max_duration_sec (int): Maximum duration for each part in seconds. Default is 1500 seconds.
  """
  # Load the audio file
  audio = AudioSegment.from_file(input_file)

  # Define the size limit in bytes
  size_limit = size_limit_mb * 1024 * 1024

  # Calculate the duration of each part based on the size limit
  bytes_per_second = bitrate / 8
  duration_per_part_by_size = size_limit / bytes_per_second * 1000  # in milliseconds

  # Convert max duration to milliseconds
  max_duration_ms = max_duration_sec * 1000

  # Use the smaller of the two durations
  duration_per_part = min(duration_per_part_by_size, max_duration_ms)

  # Ensure the output directory exists
  os.makedirs(output_dir, exist_ok=True)

  # Split the audio into parts
  for i, start in enumerate(range(0, len(audio), int(duration_per_part))):
    part = audio[start : start + int(duration_per_part)]
    part.export(os.path.join(output_dir, f"audio-part-{i + 1}.mp3"), format="mp3")

  print("Audio split into parts successfully!")
