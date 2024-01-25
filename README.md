# Sms_spam_checker
>The SMS Spam checker is Basically the project that checks whether the sms sent by third party is spam or ham.
>There are various steps involved in making the normal message to check .
>## Data Gathering
>Step one is taking dataset from any one source that is Kaggle,UCI etc
>## Data Cleaning
>Next step is to clean the data.Here I found many null Columns which I dropped,Renamed the  columns and deleted the duplicated values.
>### EDA
>Now we perform EDA so we get deeper understanding and relation between the attributes. We use **Matplotlib** library here for visualisations
>## Data Pre Processing
>After that we preprocessed the data i.e there were two columns Target and Text.Target Contains The Either mail is spam or not.So i coverted them to 0 or 1. After that The Text Column contains the Text Which is spam or not. So i counted number of words ,number of characters and number of sentences ,That is done with the help of library which is "nltk" their is one function i.e Tokenizer that converts each word into token and store it in list.Same for scent_tokenizer to convert each sentence into token and then find the length of each words and sentences respectively.
>we store each of length i.e(num_charcters,num_words,num_sentences) in different columns respectively here is feature engineering played the role.
>## Model Building
>Now to build model we have to choose the accurate model with great precision.Now we have  to take the apprpriate model.So we here with our analysis find that Naive Bayes is great model we can . It's a Probablistic Approach so you For each word which provide the weightage about the decision whether its Spam or not.
>For this we have to do the vectorization.That is Convert words to weighted numerical form.
>Some Methods are Bag Of Words, Tfidf..etc.
>We use Bag Of Words here for that we have to convert the text
>Steps Are
>  A. Convert the text into lower form
>  B. Then take out each punctuation marks and special characters.
>  C. Take out the stop words (These are the words that supports the sentences like are,of,on the...etc.) for this we have **nltk.corpus** from where we can take stop words and check if the words are not from these stop words we append to new_list.
> D. Then we do stemming (that is many forms of words are converted to single word) with the help of **nltk.stem.porter** _import Porter Stemmer_.Istantiate it and use for each word and store it in the list and join by space and make  a line .
> Now we apply this function to each text row.
>Now we make seperate word cloud(this is cloud of words which get highlighted more  if the intensity of words are more in the bag) for spam and ham.**from wordcloud**  _import WordCloud_
>From this we know which words are more frequntly used for spam as well as ham.
>Now we put all the mtext words in which spam Target has occured in a bag called as spam_corpus and simmilarly ham  words we put in ham_corpus.
>Now we use Count Vectorizer which convert the word into numerical matrix.This is taken by**Scikitlearn.feature_extraction.text** and store them in an array. And then we Put it as X
>For Y we put the value of Target in an Array.
>Now we Do Train Test Split with help of Scikit learn library  which comes under **sklearn.model_selection**
> Now we check which Naive Bayes Model fit best there are three models name Gaussain Naive Bayes, Multinomial Naive Bayes and Bernoulli Naive Bayes.
>We also check accuracy score,confusion matrix and precision score for each model although we put more focus on precision score but then also we find it to take out that we have **sklearn.metrics** we take accuracy score ,confusion matrix and precision score
>The conclusion we find is that the Multinomial Naive Bayes Binomial Performs well with an precision of 87% (in tfidf vectorizer it becomes 100%) _Precision= TP/(TP + FP)_.
>## Converting to Website
>Now we use pickle library to dump the vectorizer and model in pkl format using **pickle.dump()** and then we make a script _app.py_ where we load that pickle file **pickle.load()**.
>With the use of  **STREAMLIT** we made the website as you will see in the app.py script
>Where we use text area which take the text by us and then transform the text using the previously used transformation function. Then Vectorize it and then apply the model if the model output will be _**Zero**_ means **spam** other wise **not spam**.
>
>
![Not_spam Image](https://github.com/deepakgwalani1999/Sms_spam_checker/assets/47658896/eaeae636-76f9-4aef-b95d-b4d07f2c3b41)
![Spam Image](https://github.com/deepakgwalani1999/Sms_spam_checker/assets/47658896/7680477b-717e-49e3-a5ce-3a321499a4fe)
