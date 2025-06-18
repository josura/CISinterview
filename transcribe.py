import whisper

# Load the Whisper model and transcribe an audio file
filename = "dialogues_example/audio-1.mp3"
model = whisper.load_model("turbo")
result = model.transcribe("audio.mp3")
print(result["text"])