from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from textblob.sentiments import NaiveBayesAnalyzer


def print_prompt():
    print("\n------------------------------------------")
    print("       Sentiment Analysis Program")
    print("------------------------------------------\n")


def get_input():
    user_input = input("Enter text to be analyzed: ")
    formatted_words = []
    return_text = ""

    porter_algorithm = PorterStemmer()
    stop_words = set(stopwords.words("English"))

    # Tokenize the text by word and remove punctuation.
    words = word_tokenize(user_input)
    tokenized_words = [word.lower() for word in words if word.isalpha()]

    if len(user_input) != 0:
        for in_word in tokenized_words:
            if in_word not in stop_words:
                stemmed_word = porter_algorithm.stem(in_word)
                formatted_words.append(stemmed_word)

    for word in formatted_words:
        return_text += (word + " ")

    return return_text


def get_sentiment(argued_text):
    formatted_argued_text = TextBlob(argued_text, analyzer=NaiveBayesAnalyzer())
    return formatted_argued_text.sentiment


def print_sentiment_data(sentiment_data):
    if sentiment_data is not None:
        if sentiment_data.classification is "pos":
            print("\nClassification: Positive")
        else:
            print("\nClassification: Negative")

        print("P_Pos: " + str(sentiment_data.p_pos))
        print("P_Neg: " + str(sentiment_data.p_neg))


def main():
    print_prompt()
    entered_text = get_input()
    sentiment_data = get_sentiment(entered_text)
    print_sentiment_data(sentiment_data)


main()
