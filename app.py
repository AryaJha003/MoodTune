from flask import Flask, render_template, request, jsonify
from src.moodtune import analyze_mood

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json() or {}

        text = str(data.get("text", "")).strip()
        language = data.get("language", "Any Language")
        genre = data.get("genre", "Any Style")

        # Validate mood input
        if not text:
            return jsonify({
                "success": False,
                "error": "Please tell us how you are feeling."
            }), 400

        # Analyze mood and generate recommendations
        emotion, recommendations = analyze_mood(
            text=text,
            language=language,
            genre=genre,
            number_of_songs=5
        )

        # Handle no recommendations
        if recommendations.empty:
            return jsonify({
                "success": False,
                "error": "No songs were found for the selected language and style."
            }), 404

        songs = []

        for _, song in recommendations.iterrows():
            songs.append({
    "track_name": str(song["track_name"]),
    "artist": str(song["artists"]),
    "style": str(song["style"]),
    "language": str(song["language"]),
    "popularity": int(song["popularity"]),
    "release_date": str(song["release_date"]),
    "match_score": round(
        float(song["match_score"]) * 100, 1
    )
})

        return jsonify({
            "success": True,
            "emotion": emotion,
            "songs": songs
        })

    except Exception as error:
        print("ERROR:", error)

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )