import unittest

from src.moodtune import predict_emotion
from src.recommender import recommend_songs


class TestMoodTune(unittest.TestCase):

    def test_emotion_prediction(self):
        emotion = predict_emotion(
            "I am extremely happy and excited today!"
        )

        self.assertIn(
            emotion,
            ["joy", "sadness", "love", "anger", "fear", "surprise"]
        )

    def test_hindi_recommendations(self):
        recommendations = recommend_songs(
            emotion="joy",
            language="Hindi",
            genre="Any Style",
            number_of_songs=5
        )

        self.assertEqual(len(recommendations), 5)

        for language in recommendations["language"]:
            self.assertEqual(language, "Hindi")

    def test_telugu_recommendations(self):
        recommendations = recommend_songs(
            emotion="joy",
            language="Telugu",
            genre="Any Style",
            number_of_songs=5
        )

        self.assertEqual(len(recommendations), 5)

        for language in recommendations["language"]:
            self.assertEqual(language, "Telugu")

    def test_bengali_recommendations(self):
        recommendations = recommend_songs(
            emotion="sadness",
            language="Bengali",
            genre="Any Style",
            number_of_songs=5
        )

        self.assertEqual(len(recommendations), 5)

        for language in recommendations["language"]:
            self.assertEqual(language, "Bengali")

    def test_match_score(self):
        recommendations = recommend_songs(
            emotion="joy",
            language="Hindi",
            genre="Any Style",
            number_of_songs=5
        )

        for score in recommendations["match_score"]:
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 1)

    def test_required_columns(self):
        recommendations = recommend_songs(
            emotion="joy",
            language="Hindi",
            genre="Any Style",
            number_of_songs=5
        )

        required_columns = [
            "track_name",
            "artists",
            "language",
            "release_date",
            "popularity",
            "style",
            "match_score"
        ]

        for column in required_columns:
            self.assertIn(column, recommendations.columns)


if __name__ == "__main__":
    unittest.main()