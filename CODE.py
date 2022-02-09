import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)





if __name__ == '__main__':
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=cc89dab11a08474ea137f88d77123b02"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict)
    art = news_dict["articles"]
    print("Let's starts today's news")
    speak("Let's start today's news")
    t = 0
    for i, article in enumerate(art):
        print(i + 1, article["title"])
        speak(article["title"].split('-')[0])
        t=t+1
        if(t>5):
            break

    print("Thanks for listening to the news")
    speak("Thanks for listening to the news.")
