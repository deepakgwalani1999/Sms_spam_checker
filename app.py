import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

tfidf=pickle.load(open("Vectorizer.pkl","rb"))
model=pickle.load(open("Model.pkl","rb"))

st.title("SMS Spam Classifier")
input_sms=st. text_area("Enter the message:")

if st.button("Predict"):
    def transform_text (text) :
        text = text.lower()
        text = nltk.word_tokenize(text)
        y = []
        for i in text :
            if i.isalnum() :
                y.append(i)
        text = y[:]
        y.clear()
        for i in text :
            if i not in stopwords.words("english") and i not in string.punctuation :
                y.append(i)
        text = y[:]
        y.clear()
        for i in text :
            y.append(ps.stem(i))

        return " ".join(y)

    transformed_sms=transform_text(input_sms)
    vect_inp=tfidf.transform([transformed_sms])
    result=model.predict(vect_inp[0])

    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")