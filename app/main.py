from flask import Flask, render_template, request, jsonify
from .stt import speech_to_text
from .gemini import ask_gemini

def create_app():
    app = Flask(__name__)

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

    return app
