import joblib
from pathlib import Path

from src.recommender import recommend_songs 


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    PROJECT_DIR
    / "models"
    / "svm_emotion_classifier.pkl"
)


# --------------------------------------------------
# Load trained emotion model
# --------------------------------------------------

emotion_model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Emotion labels
# --------------------------------------------------

EMOTION_NAMES = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}


# --------------------------------------------------
# Predict emotion from text
# --------------------------------------------------

def predict_emotion(text):

    if not text or not text.strip():

        raise ValueError(
            "Please enter how you are feeling."
        )

    prediction = emotion_model.predict(
        [text]
    )[0]

    return EMOTION_NAMES[prediction]


# --------------------------------------------------
# Complete MoodTune analysis
# --------------------------------------------------

def analyze_mood(
    text,
    language="Any Language",
    genre="Any Genre",
    number_of_songs=5
):

    emotion = predict_emotion(text)

    recommendations = recommend_songs(
        emotion=emotion,
        language=language,
        genre=genre,
        number_of_songs=number_of_songs
    )

    return emotion, recommendations


# --------------------------------------------------
# Test MoodTune
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("MOODTUNE - AI MOOD ANALYSIS")
    print("=" * 60)

    user_text = input(
        "\nTell MoodTune how you feel: "
    )

    language = input(
        "Language (press Enter for Any Language): "
    ).strip()

    if not language:
        language = "Any Language"

    genre = input(
        "Genre (press Enter for Any Genre): "
    ).strip()

    if not genre:
        genre = "Any Genre"

    try:

        emotion, recommendations = analyze_mood(
            text=user_text,
            language=language,
            genre=genre,
            number_of_songs=5
        )

        print(
            f"\nAI detected mood: "
            f"{emotion.upper()}"
        )

        print(
            f"Language: {language}"
        )

        print(
            f"Genre: {genre}"
        )

        print("\nRecommended songs:\n")

        if recommendations.empty:

            print(
                "No songs found for these filters."
            )

        else:

            for _, song in recommendations.iterrows():

                print(
                    f"{song['track_name']} - "
                    f"{song['artists']}"
                )

                print(
                    f"Language: "
                    f"{song['language_name']} | "
                    f"Genre: "
                    f"{song['track_genre']} | "
                    f"Match: "
                    f"{song['match_score']:.3f}"
                )

                print()

    except ValueError as error:

        print(f"\nError: {error}")