import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.makedirs(UPLOAD_DIR, exist_ok=True)
