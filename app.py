from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "audio field missing"}), 400

        file = request.files["audio"]

        if file.filename == "":
            return jsonify({"error": "empty filename"}), 400

        ext = os.path.splitext(file.filename)[1]
        filename = f"{uuid.uuid4()}{ext}"
        path = os.path.join(UPLOAD_DIR, filename)

        file.save(path)

        print("Saved:", path)

        # ⛔ ŞİMDİLİK STT YOK
        return jsonify({
            "text": "Ses başarıyla alındı",
            "response": "Dosya kaydedildi"
        })

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return jsonify({"error": str(e)}), 500
