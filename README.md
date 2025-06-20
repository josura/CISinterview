# CISinterview
Speech recognition, transcription and translation, for interviews


# Requirements
- Python 3.10

# Build
- Create the environment (Linux commands)
```bash
python3.10 -m venv venv
```
- Source the environment (Linux commands)
```bash
source venv/bin/activate
```
- Install the requirements:
```bash
pip install -r requirements.txt
```
# Usage
- Add the audio files inside the *dialogues_example* folder
- Run the main transcription script:
```bash
python transcribe.py
```

The transcribed outputs will be written inside the *transcriptions* folder