# imports
import requests
import tweepy
import os
from datetime import datetime

class get_temp:

    #api key and location
    APIKEY = os.environ.get("OPENWEATHERMAP_API_KEY")
    location = "Ottawa"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+APIKEY

    #getting api weather info
    api_link = requests.get(complete_api_link)#using http requests to retrieve the info
    api_data = api_link.json()#storing it into a json format

    #getting info from the api data into variables
    current_real_temp = '{:.2f}'.format(((api_data["main"]["temp"] - 273.15)))#current temp
    current_feels_like = '{:.2f}'.format(((api_data["main"]["feels_like"] - 273.15)))#current feels like
    current_windspeed = (api_data["wind"]["speed"])#current windspeed
    current_humidity = ((api_data["main"]["humidity"]))#current humidity

    daily_description = ((api_data["weather"][0]["main"]) + " - " + (api_data["weather"][0]["description"]))#description of the weather
    daily_date = datetime.now().strftime('%d %b %Y')#date

    daily_max = '{:.2f}'.format(((api_data["main"]["temp_max"] - 273.15)))#max temperature for the day
    daily_min = '{:.2f}'.format(((api_data["main"]["temp_min"] - 273.15)))#min temperature for the day

def tweet_out():

    #calling method to get the temperature from the class above
    temp = get_temp()

    tweet = ("OTTAWA WEATHER FOR " + temp.daily_date + "\n\nCurrent weather conditions: " + (temp.daily_description) +
    "\nCurrent temperature: \n" + str(temp.current_real_temp) + "°C.; feels like: " + str(temp.current_feels_like) + "°C.; high of: " + str(temp.daily_max)
    + "°C.; low of: " + str(temp.daily_min) + "°C.\nHumidity: "+ str(temp.current_humidity) + "%\nWind Speed: " + str(temp.current_windspeed) + "kmph"
    + "\n\nHave a great day Ottawa!"+ "\n #ottawa #weather #news #communityBot")

    #auth keys for twitter api
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')#api key
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')#api key secret

    key = os.environ.get('TWITTER_ACCESS_KEY')#access key
    secret = os.environ.get('TWITTER_ACCESS_KEY_SECRET')#access key secret

    #accessing the api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    #declaring an easy variable for the tweepy/twitter api
    api = tweepy.API(auth, wait_on_rate_limit=True)

    #"; \ntoday's high: %.2f°C." %(temp.daily_max),"; today's low: %.2f°C." %(temp.daily_min),

    #outputting the tweet
    api.update_status(tweet)

#tweeting the message by calling the method
tweet_out()