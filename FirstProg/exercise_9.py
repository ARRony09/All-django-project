import requests
import json
import time
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__=='__main__':
    speak("News for today ")
    url = "http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=be58d0b353d54967b1ed4fe91c74ef27"

    news = requests.get(url).text
    news_dict =json.loads(news)
    # print(news_dict["articles"])
    arts=news_dict["articles"]
    for article in arts:
        speak(article["title"])
        speak(article["description"])
        time.sleep(1)
        speak("moving on the next news.... Listen carefully")
