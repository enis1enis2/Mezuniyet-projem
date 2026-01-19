from faster_whisper import WhisperModel
from pydub import AudioSegment
import os, uuid

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

AudioSegment.converter = "/usr/bin/ffmpeg"

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)

def speech_to_text(uploaded_file):
    webm = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.webm")
    wav = webm.replace(".webm", ".wav")

    uploaded_file.save(webm)

    AudioSegment.from_file(webm).export(
        wav,
        format="wav",
        parameters=["-ac", "1", "-ar", "16000"]
    )

    segments, _ = model.transcribe(
        wav,
        language="tr"
    )

    text = "".join(s.text for s in segments).strip()

    os.remove(webm)
    os.remove(wav)

    return text
