# Project Statement

## Project Title

MoodTune – An AI-Powered Mood Detection and Personalized Music Recommendation Web Application

## Problem

People often choose music based on how they are feeling, but finding suitable songs can require manually searching through songs, artists, or playlists.

MoodTune tries to make this process easier by allowing the user to describe their mood in normal text. The application analyses the text, detects the emotion and recommends songs that match the detected mood.

## Proposed Solution

MoodTune is a web-based application that combines Natural Language Processing, Machine Learning and a music recommendation system.

The user enters a description of their current mood. The text is converted into TF-IDF features and given to a trained Linear SVM classifier. The classifier predicts one of six emotions: sadness, joy, love, anger, fear or surprise.

After detecting the emotion, the recommendation system uses a corresponding mood profile and compares it with song audio features such as energy, valence, danceability, acousticness and tempo.

The user can also select a preferred language and music style before getting recommendations.

## Main Functionalities

1. Mood detection from free-form text.
2. Emotion classification using TF-IDF and Linear SVM.
3. Language-based song filtering.
4. Music style filtering.
5. Mood-based song recommendation.
6. Ranking of songs using audio-feature similarity.
7. Display of the top five recommendations.
8. Basic input validation and error handling.

## Machine Learning Approach

The emotion classification model was trained using the DAIR.AI Emotion dataset.

Three models were compared during development:

- Logistic Regression
- Linear SVM
- Multinomial Naive Bayes

The Linear SVM model was selected as the final classifier after comparing the evaluation results.

## Recommendation Approach

The recommendation system uses five main audio features:

- Energy
- Valence
- Danceability
- Acousticness
- Tempo

A mood profile is defined for each detected emotion. The system calculates the similarity between the mood profile and the audio features of available songs and uses the resulting score to rank recommendations.

Artist diversity is also considered while selecting the final recommendations.

## Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Git
- GitHub

## Expected Outcome

## Outcome

The completed project is a working web application where a user can describe their mood, select music preferences and receive a list of songs suitable for their detected mood.

## Project Scope

The current version focuses on mood detection from text and recommendation using existing song datasets. It is a prototype and can be extended later with more languages, larger datasets, user history and more advanced recommendation methods.
