
import subprocess
from openai import OpenAI

def synthesize_speech(text_to_speak, audio_file_path):
    # Provide your OpenAI API key here
    client = OpenAI(api_key="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")

    # Call the OpenAI API to synthesize the speech
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text_to_speak,
    )

    # Save the audio file
    with open(audio_file_path, "wb") as f:
        f.write(response.content)

    return audio_file_path

def play_audio(file_path):
    # Check for 'play' command (sox) or find another suitable player
    try:
        subprocess.run(["play", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to play the audio: {e}")
    except FileNotFoundError:
        print("The 'play' command is not found. Please ensure 'sox' is installed or use another audio player.")

if __name__ == "__main__":
    # Get the text from the user
    text_to_speak = input("Enter the text you want to convert to speech: ")

    # Specify the audio file path
    audio_file_path = input("Enter the filename to save the audio (e.g., speech.mp3): ")

    # Synthesize speech and get the file path
    file_path = synthesize_speech(text_to_speak, audio_file_path)

    # Play the audio file
    print(f"Playing the synthesized speech from {file_path}...")
    play_audio(file_path)
