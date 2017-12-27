from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from textblob.sentiments import NaiveBayesAnalyzer


def print_prompt():
    print("\n------------------------------------------")
    print("Enter text to be analyzed")
    print("------------------------------------------\n")


def get_input():
    user_input = input()
    formatted_words = []
    return_text = ""

    porter_algorithm = PorterStemmer()
    stop_words = set(stopwords.words("English"))

    if len(user_input) != 0:
        for in_word in word_tokenize(user_input):
            if in_word not in stop_words:
                stemmed_word = porter_algorithm.stem(in_word)
                formatted_words.append(stemmed_word)

    for word in formatted_words:
        return_text += (" " + word)

    return formatted_words


def main():
    testimonial = TextBlob("I hate this movie!", analyzer=NaiveBayesAnalyzer())



