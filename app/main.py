from flask import Flask, render_template, request, jsonify
from .stt import speech_to_text
from .gemini import ask_gemini
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

def create_app():
    app = Flask(
        __name__,
        static_url_path="/proxy/8000/static",
        static_folder="static",
        template_folder="templates"
    )

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/upload", methods=["POST"])
    def upload():
        if "audio" not in request.files:
            return jsonify({"error": "Dosya yok"}), 400

        text = speech_to_text(request.files["audio"])
        ai_response = ask_gemini(text)

        return jsonify({
            "transcript": text,
            "response": ai_response
        })
    @app.route("/ask", methods=["POST"])
    def ask():
        prompt = request.json.get("prompt")
        return jsonify({"response": ask_gemini(prompt)})

    return app
