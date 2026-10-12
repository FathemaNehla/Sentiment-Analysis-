def analyse_sentiment():
    sentence = input("Enter a sentence: ")

    sentence_tfidf = vectorizer.transform([sentence])

    probabilities = model.predict_proba(sentence_tfidf)[0]
    predicted_label = model.predict(sentence_tfidf)[0]

    print("\nSentiment probabilities:")

    for label, probability in zip(model.classes_, probabilities):
        print(f"{sentiments[int(label)]}: {probability * 100:.2f}%")

    print("\nPredicted sentiment:", sentiments[int(predicted_label)])


analyse_sentiment()
