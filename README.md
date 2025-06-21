# CISinterview
Speech recognition, transcription and translation, for interviews


# Requirements
- Python 3.10
- ffmpeg (required by whisper)

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
**IMPORTANT:** some dependencies in the requirement are linux specific, if any problem arises, try to install whisper directly and see if everything works.
# Usage
- Add the audio files inside the *dialogues_example* folder
- Run the main transcription script:
```bash
python transcribe.py
```

The transcribed outputs will be written inside the *transcriptions* folder