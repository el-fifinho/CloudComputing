from flask import Flask, request, jsonify
from services.youtube import download_audio_from_youtube
from services.speech import transcribe_audio
from services.translate import translate_text
from models.db import fetch_translation, store_translation
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/process", methods=["POST"])
def process_video():
    data = request.get_json()
    youtube_url = data.get("url")
    target_lang = data.get("lang", "en")

    try:
        
        cached_translation = fetch_translation(youtube_url, target_lang)
        if cached_translation:
            return jsonify({
                "transcript": None,
                "translated": cached_translation,
                "cached": True
            })

        
        audio_path = download_audio_from_youtube(youtube_url)
        transcript = transcribe_audio(audio_path)
        translated = translate_text(transcript, target_lang)

        
        store_translation(youtube_url, transcript, translated, target_lang)

        return jsonify({
            "transcript": transcript,
            "translated": translated,
            "cached": False
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    #app.run(host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=port)
