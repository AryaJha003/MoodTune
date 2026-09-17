import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler


# ============================================================
# MOODTUNE MUSIC RECOMMENDER
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
INDIAN_DATA_DIR = PROJECT_DIR / "data" / "indian_songs"
ENGLISH_DATA_PATH = PROJECT_DIR / "data" / "spotify_songs.csv"


# Audio features used for recommendation
FEATURES = [
    "energy",
    "valence",
    "danceability",
    "acousticness",
    "tempo"
]

# Importance of each feature
FEATURE_WEIGHTS = np.array([
    0.30,   # energy
    0.30,   # valence
    0.20,   # danceability
    0.10,   # acousticness
    0.10    # tempo
])


# ============================================================
# MOOD PROFILES
# ============================================================

MOOD_PROFILES = {

    "joy": {
        "energy": 0.80,
        "valence": 0.90,
        "danceability": 0.80,
        "acousticness": 0.30,
        "tempo": 0.70
    },

    "sadness": {
        "energy": 0.30,
        "valence": 0.20,
        "danceability": 0.30,
        "acousticness": 0.60,
        "tempo": 0.35
    },

    "anger": {
        "energy": 0.90,
        "valence": 0.30,
        "danceability": 0.60,
        "acousticness": 0.20,
        "tempo": 0.80
    },

    "fear": {
        "energy": 0.40,
        "valence": 0.20,
        "danceability": 0.30,
        "acousticness": 0.50,
        "tempo": 0.40
    },

    "love": {
        "energy": 0.50,
        "valence": 0.80,
        "danceability": 0.60,
        "acousticness": 0.50,
        "tempo": 0.50
    },

    "surprise": {
        "energy": 0.80,
        "valence": 0.70,
        "danceability": 0.75,
        "acousticness": 0.30,
        "tempo": 0.75
    }
}


# ============================================================
# LANGUAGE NAMES
# ============================================================

SUPPORTED_LANGUAGES = {
    "Any Language": None,

    "English": "English",

    "Hindi": "Hindi",
    "Telugu": "Telugu",
    "Tamil": "Tamil",
    "Kannada": "Kannada",
    "Malayalam": "Malayalam",
    "Bengali": "Bengali",
    "Marathi": "Marathi",
    "Punjabi": "Punjabi",
    "Gujarati": "Gujarati",
    "Assamese": "Assamese",
    "Odia": "Odia",
    "Urdu": "Urdu",
    "Bhojpuri": "Bhojpuri",
    "Haryanvi": "Haryanvi",
    "Rajasthani": "Rajasthani"
}


# ============================================================
# LOAD INDIAN MUSIC DATA
# ============================================================

def load_indian_music():
    """
    Loads all Indian-language CSV files from data/indian_songs.
    Each CSV contains songs from one Indian language.
    """

    files = list(INDIAN_DATA_DIR.glob("*_songs.csv"))
    dataframes = []

    for file in files:

        try:
            df = pd.read_csv(file)

            # Standardize column names
            df.columns = [
                str(column).strip().lower()
                for column in df.columns
            ]

            # Rename columns to common format
            rename_map = {
                "song_name": "track_name",
                "singer": "artists",
                "stream": "streams"
            }

            df = df.rename(columns=rename_map)

            required_columns = [
                "track_name",
                "artists",
                "language",
                "energy",
                "valence",
                "danceability",
                "acousticness",
                "tempo",
                "popularity"
            ]

            missing = [
                column
                for column in required_columns
                if column not in df.columns
            ]

            if missing:
                print(
                    f"Skipping {file.name}: "
                    f"missing columns {missing}"
                )
                continue

            # Add release date
            if "released_date" in df.columns:
                df["release_date"] = df["released_date"]
            else:
                df["release_date"] = ""

            df["source"] = "Indian Music Dataset"

            dataframes.append(
                df[
                    [
                        "track_name",
                        "artists",
                        "language",
                        "release_date",
                        "energy",
                        "valence",
                        "danceability",
                        "acousticness",
                        "tempo",
                        "popularity",
                        "source"
                    ]
                ]
            )

        except Exception as error:
            print(f"Could not load {file.name}: {error}")

    if not dataframes:
        raise FileNotFoundError(
            "No valid Indian music CSV files were found."
        )

    return pd.concat(
        dataframes,
        ignore_index=True
    )

# ============================================================
# LOAD ENGLISH MUSIC
# ============================================================

def load_english_music():
    """
    Loads the existing Spotify dataset for English songs.
    """

    if not ENGLISH_DATA_PATH.exists():
        return pd.DataFrame()

    df = pd.read_csv(ENGLISH_DATA_PATH)

    df.columns = [
        str(column).strip().lower()
        for column in df.columns
    ]

    rename_map = {
        "track_artist": "artists",
        "track_popularity": "popularity"
    }

    df = df.rename(columns=rename_map)

    required = [
        "track_name",
        "artists",
        "energy",
        "valence",
        "danceability",
        "acousticness",
        "tempo",
        "popularity"
    ]

    missing = [
        column
        for column in required
        if column not in df.columns
    ]

    if missing:
        return pd.DataFrame()

    # Add release date
    if "track_album_release_date" in df.columns:
        df["release_date"] = df["track_album_release_date"]
    else:
        df["release_date"] = ""

    df["language"] = "English"
    df["source"] = "Spotify Music Dataset"

    return df[
        [
            "track_name",
            "artists",
            "language",
            "release_date",
            "energy",
            "valence",
            "danceability",
            "acousticness",
            "tempo",
            "popularity",
            "source"
        ]
    ]

# ============================================================
# LOAD COMPLETE MUSIC DATABASE
# ============================================================

def load_music_data():

    indian_df = load_indian_music()

    english_df = load_english_music()

    frames = [indian_df]

    if not english_df.empty:
        frames.append(english_df)

    df = pd.concat(
        frames,
        ignore_index=True
    )

    # Convert numerical columns
    for feature in FEATURES + ["popularity"]:
        df[feature] = pd.to_numeric(
            df[feature],
            errors="coerce"
        )

    # Remove incomplete records
    df = df.dropna(
        subset=[
            "track_name",
            "artists",
            "language"
        ] + FEATURES
    )

    # --------------------------------------------------------
    # Remove duplicate songs
    # --------------------------------------------------------

    df["clean_track"] = (
        df["track_name"]
        .astype(str)
        .str.lower()
        .str.replace(
            r"\s*[\(\[].*?[\)\]]",
            "",
            regex=True
        )
        .str.strip()
    )

    df["clean_artist"] = (
        df["artists"]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    df = df.drop_duplicates(
        subset=[
            "clean_track",
            "clean_artist",
            "language"
        ]
    )

    return df.reset_index(drop=True)


# ============================================================
# STYLE CLASSIFICATION
# ============================================================

def classify_style(row):
    """
    Creates a simple style label from audio characteristics.

    These are inferred recommendation categories,
    NOT official dataset genres.
    """

    energy = row["energy"]
    valence = row["valence"]
    danceability = row["danceability"]
    acousticness = row["acousticness"]

    if energy >= 0.70 and danceability >= 0.65:
        return "Energetic"

    if acousticness >= 0.70 and energy <= 0.55:
        return "Acoustic"

    if valence >= 0.70 and danceability >= 0.60:
        return "Dance"

    if energy <= 0.40 and valence <= 0.45:
        return "Calm"

    if valence >= 0.65:
        return "Feel Good"

    return "Balanced"


# ============================================================
# RECOMMEND SONGS
# ============================================================

def recommend_songs(
    emotion,
    language="Any Language",
    genre="Any Style",
    number_of_songs=5
):

    df = load_music_data()

    # --------------------------------------------------------
    # Language filtering
    # --------------------------------------------------------

    if language != "Any Language":

        selected_language = SUPPORTED_LANGUAGES.get(
            language
        )

        if selected_language is not None:

            df = df[
                df["language"].str.lower()
                == selected_language.lower()
            ]

    # --------------------------------------------------------
    # Safety check
    # --------------------------------------------------------

    if df.empty:

        return pd.DataFrame(
            columns=[
                "track_name",
                "artists",
                "language",
                "popularity",
                "match_score",
                "style"
            ]
        )

    # --------------------------------------------------------
    # Generate style
    # --------------------------------------------------------

    df["style"] = df.apply(
        classify_style,
        axis=1
    )

    # --------------------------------------------------------
    # Style filtering
    # --------------------------------------------------------

    if genre not in [
        "Any Style",
        "Any Genre",
        "",
        None
    ]:

        if genre in df["style"].unique():

            df = df[
                df["style"] == genre
            ]

    # --------------------------------------------------------
    # Normalize audio features
    # --------------------------------------------------------

    scaler = MinMaxScaler()

    feature_matrix = scaler.fit_transform(
        df[FEATURES]
    )

    # --------------------------------------------------------
    # Create mood target
    # --------------------------------------------------------

    mood = emotion.lower()

    if mood not in MOOD_PROFILES:
        mood = "joy"

    mood_vector = np.array([
        MOOD_PROFILES[mood][feature]
        for feature in FEATURES
    ])

    # --------------------------------------------------------
    # Weighted distance
    # --------------------------------------------------------

    differences = (
        feature_matrix - mood_vector
    ) ** 2

    weighted_distance = np.sqrt(
        np.sum(
            differences * FEATURE_WEIGHTS,
            axis=1
        )
    )

    df["distance"] = weighted_distance

    # Convert distance into understandable percentage
    df["match_score"] = (
        1 / (1 + df["distance"])
    )

    # --------------------------------------------------------
    # Sort by mood similarity + popularity
    # --------------------------------------------------------

    df = df.sort_values(
        by=[
            "match_score",
            "popularity"
        ],
        ascending=[
            False,
            False
        ]
    )

    # --------------------------------------------------------
    # Artist diversity
    # --------------------------------------------------------

    candidate_pool = df.head(
        max(number_of_songs * 8, 40)
    )

    recommendations = []

    used_artists = set()

    # First pass:
    # Try to give different artists
    for _, row in candidate_pool.iterrows():

        artist = str(row["artists"])

        if artist not in used_artists:

            recommendations.append(row)
            used_artists.add(artist)

        if len(recommendations) == number_of_songs:
            break

    # Second pass:
    # Fill remaining positions if necessary
    if len(recommendations) < number_of_songs:

        for _, row in candidate_pool.iterrows():

            if len(recommendations) == number_of_songs:
                break

            if row["track_name"] not in [
                x["track_name"]
                for x in recommendations
            ]:

                recommendations.append(row)

    # --------------------------------------------------------
    # Final dataframe
    # --------------------------------------------------------

    result = pd.DataFrame(
        recommendations
    )

    if result.empty:
        return result

    return result[
        [
            "track_name",
            "artists",
            "language",
            "release_date",
            "popularity",
            "style",
            "energy",
            "valence",
            "danceability",
            "acousticness",
            "tempo",
            "match_score"
        ]
    ].reset_index(drop=True)
