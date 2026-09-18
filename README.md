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
```

---

## Machine Learning

The emotion detection part uses **TF-IDF** for converting text into numerical features and a **Linear SVM** model for emotion classification.

The model classifies the user's text into six emotion categories:

- Sadness
- Joy
- Love
- Anger
- Fear
- Surprise

During development, three machine learning models were compared:

| Model | Accuracy |
|---|---:|
| Logistic Regression | 87.15% |
| Linear SVM | 88.00% |
| Multinomial Naive Bayes | 65.10% |

The Linear SVM model was selected as the final model because it gave the highest accuracy among the tested models.

The trained model is stored in the `models` folder and is loaded by the application when making predictions.

---

## Recommendation System

After the emotion is predicted, MoodTune maps it to a predefined mood profile.

The recommendation system compares the mood profile with song audio features.

The main audio features used are:

- Energy
- Valence
- Danceability
- Acousticness
- Tempo

The user can also select a preferred language and music style.

The system first filters the available songs according to these preferences. It then calculates a similarity score between the songs and the detected mood profile.

The songs are ranked using their match scores, while artist diversity is also considered. Finally, the top five recommendations are displayed.

---

## Supported Languages

The current version supports English and several Indian languages:

- English
- Hindi
- Telugu
- Tamil
- Kannada
- Malayalam
- Bengali
- Marathi
- Punjabi
- Gujarati
- Assamese
- Odia
- Urdu
- Bhojpuri
- Haryanvi
- Rajasthani

---

## Music Styles

The application provides the following music style options:

- Any Style
- Energetic
- Dance
- Feel Good
- Calm
- Acoustic
- Balanced

The styles are assigned using the audio characteristics of the songs.

---

## Datasets

### Emotion Dataset

The emotion classification model was trained using the **DAIR.AI Emotion dataset**.

The dataset contains text examples belonging to six emotion categories.

The data used in the project was divided into:

- Training dataset – 16,000 records
- Validation dataset – 2,000 records
- Test dataset – 2,000 records

The training dataset was used to train the models and the test dataset was used to evaluate their performance. The validation dataset was retained as a separate dataset for validation purposes.

### Music Dataset

The recommendation system uses Spotify-based music data along with Indian-language music datasets.

The Indian music collection contains separate datasets for languages such as Hindi, Telugu, Tamil, Kannada, Malayalam, Bengali, Marathi, Punjabi, Gujarati, Assamese, Odia, Urdu, Bhojpuri, Haryanvi and Rajasthani.

The music data contains information such as song name, artist, language, popularity, release information and audio features.

---

## Technologies Used

The project was developed using:

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

---

## Project Structure

```text
MoodTune/
│
├── data/
│   ├── emotion_train.csv
│   ├── emotion_validation.csv
│   ├── emotion_test.csv
│   ├── spotify_songs.csv
│   ├── spotify_tracks.csv
│   └── indian_songs/
│
├── models/
│   ├── emotion_classifier.pkl
│   ├── svm_emotion_classifier.pkl
│   └── naive_bayes_emotion_classifier.pkl
│
├── src/
│   ├── moodtune.py
│   ├── recommender.py
│   ├── train_model.py
│   ├── compare_models.py
│   ├── compare_naive_bayes.py
│   ├── analyze_dataset.py
│   └── download_emotion.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_moodtune.py
│
├── app.py
├── README.md
├── statement.md
└── .gitignore
```

---

## Testing

A separate test file called `tests/test_moodtune.py` was created to test important parts of the application.

The test suite contains six tests covering:

- Emotion prediction
- Hindi recommendations
- Telugu recommendations
- Bengali recommendations
- Match score validation
- Required recommendation columns

All six tests passed successfully during testing.

```text
Ran 6 tests in 4.631s

OK
```

---

## Example

For example, if the user enters:

```text
I am feeling happy and energetic today
```

MoodTune processes the text and predicts the emotion. Based on the detected emotion, selected language and music style, the recommendation system finds suitable songs and displays the top five results.

Each recommendation shows details such as:

- Song name
- Artist
- Language
- Music style
- Release information
- Popularity
- Match score

---

## Project Statement

A detailed description of the project, including the problem, proposed solution, main functionalities, machine learning approach and project scope, is available in:

[`statement.md`](statement.md)

---

## GitHub Repository

The complete source code and documentation for MoodTune are available here:

**MoodTune GitHub Repository:**

https://github.com/AryaJha003/MoodTune

---

## Future Improvements

Some improvements that can be added in future versions are:

- Adding more Indian languages and songs.
- Using larger and more updated music datasets.
- Using more advanced NLP models for better emotion detection.
- Adding personalized recommendations based on user history.
- Connecting the application with music streaming platforms.
- Supporting mixed or multiple emotions.
- Adding voice-based mood input.
- Adding user accounts, favorites and recommendation history.
- Improving the user interface.

---

## Conclusion

MoodTune combines Natural Language Processing, Machine Learning and a music recommendation system into one web application.

The project helped me understand how a machine learning model can be connected to a real web application and how different components such as text processing, emotion classification, filtering and recommendation can work together.

The current version works as a prototype and provides mood-based music recommendations through a simple web interface.
