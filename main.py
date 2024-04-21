from bs4 import BeautifulSoup
import requests

cnn_url = "https://www.cnn.com/"
fox_news_url = "https://www.foxnews.com/"

cnn = requests.get(cnn_url)
fox_news = requests.get(fox_news_url)

cnn_document = BeautifulSoup(cnn.text, "html.parser")
fox_news_document = BeautifulSoup(fox_news.text, "html.parser")

cnn_headlines = cnn_document.find_all(class_="container__headline-text")
fox_news_headlines = fox_news_document.find_all(class_="title")

while True:
    print("From which source would you like to view your news?")
    print("1. CNN")
    print("2. Fox News")
    print("Type \"quit\" to exit the program.")
    user_input = input()

    if user_input == "1":
        print("News from CNN:")
        for headline in cnn_headlines:
            print(headline.get_text())

    elif user_input == "2":
        print("News from Fox News:")
        for headline in fox_news_headlines:
            print(headline.get_text())

    elif user_input.lower() == "quit":
        break

    else:
        print("Sorry, what you've entered is invalid. Please try again.")
