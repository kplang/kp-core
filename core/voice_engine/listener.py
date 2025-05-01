# core/voice_engine/listener.py

import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile

model = whisper.load_model("base")  # You can use "tiny", "small", "medium", "large"

def record_audio(duration=5, samplerate=44100):
    print(f"\n🎙️ [KP Voice Engine] Listening for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    return samplerate, recording

def listen_for_voice_command():
    samplerate, audio = record_audio()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        scipy.io.wavfile.write(f.name, samplerate, (audio * 32767).astype(np.int16))
        print("🧠 Transcribing with Whisper...")
        result = model.transcribe(f.name)

    text = result["text"].strip().lower()
    print(f"🗣️ You said: {text}")

    return {
        "raw_voice": text,
        "intent": "process_command",
        "parameters": {},
        "kp_code": text
    }

