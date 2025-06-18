import whisper
import os

# Define input and output directories
input_dir = "dialogues_example"
output_dir = "transcriptions"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load the Whisper model
model = whisper.load_model("turbo")
# TODO : Load the Whisper model with the appropriate size, depending on available resources, turbo model requires 6GB of VRAM

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".mp3"):
        input_path = os.path.join(input_dir, filename)
        print(f"Transcribing {input_path}...")

        # Transcribe audio
        result = model.transcribe(input_path)

        # Prepare output path (same name, .txt extension)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, f"{base_name}.txt")

        # Write transcription to output file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"Saved transcription to {output_path}")
