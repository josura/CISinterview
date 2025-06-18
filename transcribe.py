import whisper

# Define input and output directories
input_dir = "dialogues_example"
output_dir = "transcriptions"

# TODO: Read the audio files from the "dialogues_example" directory

# Load the Whisper model and transcribe an audio file
filename = "dialogues_example/audio-1.mp3"
model = whisper.load_model("turbo")
result = model.transcribe("audio.mp3")
print(result["text"])

#TODO: Save the transcribed texts to some files inside a "transcriptions" directory