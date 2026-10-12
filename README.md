# Sentiment Analysis Using NLP and Machine Learning

A beginner-friendly machine learning project that analyses text comments and classifies them into **Positive, Negative, or Neutral** sentiments using Natural Language Processing (NLP) and Logistic Regression.

## Project Overview

This project uses Natural Language Processing and Machine Learning to identify the sentiment expressed in text. A labelled dataset from Hugging Face Datasets is used to train and evaluate the model.

The project converts text into numerical features using TF-IDF and trains a Logistic Regression classifier to predict sentiment. Users can also enter their own sentences to obtain a predicted sentiment and estimated probabilities for each sentiment category.

## Objectives

- Understand the basics of Natural Language Processing (NLP).
- Preprocess and convert text data into numerical features.
- Train a machine learning model for sentiment classification.
- Evaluate model performance using standard classification metrics.
- Predict sentiment for new user-provided text.

## Technologies Used

- **Python** — Programming language
- **Pandas** — Data handling and organisation
- **Hugging Face Datasets** — Dataset loading
- **Scikit-learn** — Feature extraction, model training, prediction, and evaluation
- **TF-IDF** — Text feature extraction
- **Logistic Regression** — Sentiment classification
- **Google Colab** — Development and execution environment

## Dataset

The project uses the `syedkhalid0/Sentiment-Analysis` dataset from Hugging Face.

**Dataset:** [Sentiment Analysis on Hugging Face](https://huggingface.co/datasets/syedkhalid0/Sentiment-Analysis)

The training dataset contains text samples and their corresponding sentiment labels.

| Label | Sentiment |
|---|---|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

## How It Works

1. **Load the dataset:** Load labelled text data using Hugging Face Datasets and organise it using Pandas.
2. **Split the data:** Divide the dataset into training and testing sets using an 80:20 ratio.
3. **Extract features:** Use TF-IDF (Term Frequency–Inverse Document Frequency) to convert text into numerical feature vectors.
4. **Train the model:** Train a Logistic Regression classifier on the extracted text features.
5. **Evaluate performance:** Measure accuracy, precision, recall, and F1-score on the test dataset.
6. **Predict sentiment:** Accept a new sentence, predict its sentiment, and display estimated probabilities for all three classes.

## Model Performance

The model achieved the following results on the test dataset:

**Accuracy: 78.49%**

| Sentiment | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Negative | 0.80 | 0.79 | 0.80 |
| Neutral | 0.58 | 0.43 | 0.50 |
| Positive | 0.81 | 0.87 | 0.84 |
| **Overall Accuracy** | | | **78.49%** |

The model performs relatively well at identifying positive and negative text. Neutral sentiment is more challenging to classify, as reflected in its lower recall and F1-score.

*Note: These results are from one train-test split and may vary with changes to the dataset or model configuration.*

## Example Prediction

**Input:**
```text
I hate this phone's battery life but its camera is pretty good.
```

**Output:**
```text
Sentiment probabilities:
Negative: 42.66%
Neutral: 3.23%
Positive: 54.11%

Predicted sentiment: Positive
```

The model predicts a positive overall sentiment because the estimated positive probability is the highest. However, the sentence contains both positive and negative opinions, which a basic three-class classifier may not fully capture.

## Installation

Install the required Python libraries:

```bash
pip install datasets pandas scikit-learn matplotlib
```

## How to Run

### Prerequisites

- Python 3.9 or later
- Git
- An active internet connection to download the dataset

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Install Dependencies

```bash
pip install datasets pandas scikit-learn matplotlib
```

### 3. Run the Project

```bash
python sentiment_analysis.py
```

### 4. Enter Your Text

When prompted, enter a sentence to analyse its sentiment.

Example:

```text
Enter a sentence: This phone has an amazing camera!
```

The program displays the estimated probabilities for Negative, Neutral, and Positive sentiments, followed by the predicted sentiment.

### Alternative: Download from GitHub

1. Open the repository on GitHub.
2. Click **Code → Download ZIP**.
3. Extract the ZIP file.
4. Open a terminal in the extracted project folder.
5. Install the dependencies and run the Python script using the commands above.

**Note:** GitHub is used to host the project files. The Python script runs locally on your computer, not on GitHub's website.

## Limitations

- The model predicts only one overall sentiment per sentence.
- Mixed sentiments may not be classified accurately.
- Neutral sentiment has lower recall than positive and negative sentiment.
- TF-IDF relies on word-based statistical features and does not fully understand context, sarcasm, or complex language.
- Prediction probabilities are model estimates and should not be interpreted as guaranteed confidence.

## Future Improvements

- Improve neutral sentiment classification.
- Experiment with alternative machine learning algorithms.
- Add text preprocessing and hyperparameter tuning.
- Develop a simple web interface using Streamlit or Flask.
- Explore transformer-based models such as BERT for improved contextual understanding.
- Extend the project to aspect-based sentiment analysis.

## Author

**Fathema Nehla**  
S3 Instrumentation and Control Engineering (ICE)

## Acknowledgements

- [Hugging Face Datasets](https://huggingface.co/docs/datasets)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

*This project was developed for educational purposes to demonstrate the application of NLP and machine learning in sentiment classification.*
