from faster_whisper import WhisperModel
from pydub import AudioSegment
import os
import uuid

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)

def speech_to_text(audio_file):
    webm_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.webm")
    wav_path = webm_path.replace(".webm", ".wav")

    audio_file.save(webm_path)

    AudioSegment.from_file(webm_path).export(
        wav_path,
        format="wav",
        parameters=["-ac", "1", "-ar", "16000"]
    )

    segments, _ = model.transcribe(
        wav_path,
        language="tr"
    )

    text = "".join(seg.text for seg in segments).strip()

    os.remove(webm_path)
    os.remove(wav_path)

    return text
