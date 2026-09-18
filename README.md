# MoodTune 🎵

## AI-Powered Mood Detection and Music Recommendation

MoodTune is a web application that recommends songs based on the mood of the user.

The idea behind this project is simple. Instead of searching for a song or playlist manually, the user can type how they are feeling in normal text. MoodTune analyses the text, predicts the emotion and then recommends songs that match the detected mood.

The application also allows the user to select a preferred language and music style so that the recommendations can be more specific.

---

## Why I Made This Project

Music is often connected with how we feel. Sometimes we want to listen to happy music, sometimes something calm, and sometimes music that matches a particular feeling.

Finding suitable songs manually can take time. I wanted to build a system where the user could simply describe their mood and get some music recommendations based on it.

This project also gave me an opportunity to use Natural Language Processing, Machine Learning and a recommendation system together in one web application.

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
- Display the top five recommendations in a simple web interface.

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
Songs are filtered by language and style
          ↓
Audio features are compared
          ↓
Songs are ranked
          ↓
Top 5 songs are shown
