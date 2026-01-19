from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(prompt: str) -> str:
    res = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return res.text
