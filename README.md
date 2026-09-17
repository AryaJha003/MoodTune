# MoodTune 🎵

## AI-Powered Mood Detection and Music Recommendation

MoodTune is a web application that recommends songs according to the mood of the user.

The main idea behind this project is simple. Instead of searching for a song or playlist manually, the user can just type how they are feeling. MoodTune reads the text, predicts the emotion, and then suggests songs that are suitable for that mood.

The application also allows the user to select a language and a music style so that the recommendations can be more specific.

---

## Why I Made This Project

Many times, we want to listen to music according to our mood, but we may not know exactly what song or playlist to search for.

For example, if someone types:

> I am feeling happy and energetic today.

the system should understand the mood and suggest songs that have characteristics suitable for that feeling.

This project was made to combine NLP, Machine Learning and a music recommendation system into one web application.

---

## Main Objectives

The main objectives of MoodTune are:

- Take the user's mood as normal text.
- Understand the emotion from the text.
- Use a Machine Learning model to classify the emotion.
- Recommend songs based on the detected emotion.
- Allow the user to select a preferred language.
- Support English and different Indian languages.
- Allow the user to select a music style.
- Use song audio features for recommendation.
- Show the top recommended songs in a simple web interface.

---

## How MoodTune Works

The basic working of the project is:

```text
User enters how they feel
          ↓
Text is processed
          ↓
TF-IDF converts the text into features
          ↓
Linear SVM predicts the emotion
          ↓
Mood profile is selected
          ↓
Songs are filtered by language/style
          ↓
Audio features are compared
          ↓
Songs are ranked
          ↓
Top 5 songs are shown
