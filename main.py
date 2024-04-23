from bs4 import BeautifulSoup
import requests

ap_news_url = "https://apnews.com/"
cbs_news_url = "https://www.cbsnews.com/"
cnn_url = "https://www.cnn.com/"
fox_news_url = "https://www.foxnews.com/"

ap_news = requests.get(ap_news_url)
cbs_news = requests.get(cbs_news_url)
cnn = requests.get(cnn_url)
fox_news = requests.get(fox_news_url)

ap_news_document = BeautifulSoup(ap_news.text, "html.parser")
cbs_news_document = BeautifulSoup(cbs_news.text, "html.parser")
cnn_document = BeautifulSoup(cnn.text, "html.parser")
fox_news_document = BeautifulSoup(fox_news.text, "html.parser")

ap_news_headlines = ap_news_document.find_all(class_="PagePromoContentIcons-text")
cbs_news_headlines = cbs_news_document.find_all(class_="item__hed")
cnn_headlines = cnn_document.find_all(class_="container__headline-text")
fox_news_headlines = fox_news_document.find_all(class_="title")

while True:
    print("From which source would you like to view your news?")
    print("1. AP News")
    print("2. CBS News")
    print("3. CNN")
    print("4. Fox News")
    print("Type \"quit\" to exit the program.")
    user_input = input()

    if user_input == "1":
        print("News from AP News:")
        for headline in ap_news_headlines:
            if headline.get_text() == "The Associated Press is an independent global news organization dedicated to factual reporting. Founded in 1846, AP today remains the most trusted source of fast, accurate, unbiased news in all formats and the essential provider of the technology and services vital to the news business. More than half the world’s population sees AP journalism every day.":
                continue
            print(headline.get_text())

    elif user_input == "2":
        print("News from CBS News:")
        for headline in cbs_news_headlines:
            print(headline.get_text())
    
    elif user_input == "3":
        print("News from CNN:")
        for headline in cnn_headlines:
            print(headline.get_text())
    
    elif user_input == "4":
        print("News from Fox News:")
        for headline in fox_news_headlines:
            print(headline.get_text())
    
    elif user_input.lower() == "quit":
        break

    else:
        print("Sorry, what you've entered is invalid. Please try again.")
