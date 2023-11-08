import tkinter as tk
from tkinter import filedialog
from openai import OpenAI

def synthesize_speech():
    # Provide your OpenAI API key here
    client = OpenAI(api_key="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")

    # Get the text from the entry widget
    text_to_speak = text_entry.get()

    # Call the OpenAI API to synthesize the speech
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text_to_speak,
    )

    # Save the audio file
    audio_file = filedialog.asksaveasfilename(defaultextension=".mp3",
                                              filetypes=[("MP3 files", "*.mp3")])
    if audio_file:
        response.stream_to_file(audio_file)

# Create the main window
root = tk.Tk()
root.title("Speech Synthesis")

# Create a text entry widget
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=20)

# Create a button to trigger speech synthesis
synthesize_button = tk.Button(root, text="Synthesize Speech", command=synthesize_speech)
synthesize_button.pack(pady=10)

# Start the GUI loop
root.mainloop()

