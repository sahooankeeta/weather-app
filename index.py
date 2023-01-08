
import flask 
from dotenv import load_dotenv
import os
import requests
load_dotenv()  # take environment variables from .env.

app = flask.Flask(__name__)
KEY=os.getenv("API_KEY")
@app.route("/",methods=['GET', 'POST'])

   
def main():
  #initital weather object
  weather={}
  
  if flask.request.method=="POST":
    #extracting query
    city=flask.request.form["input"]
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":city}
    headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': KEY
    }
    try:
      response = requests.request("GET", url, headers=headers, params=querystring).json()
      #print(response)
      #extracting data
      weather={
        'name':response['location']['name'],
        'region':response['location']['region'],
        'country':response['location']['country'],
        'lat':response['location']['lat'],
        'lon':response['location']['lon'],
        'date':response['location']['localtime'].split()[0],
        'time':response['location']['localtime'].split()[1],
        'last_updated':response['current']['last_updated'],
        'temp':response['current']['temp_f'],
        'text':response['current']['condition']['text'],
        'icon':'http:'+response['current']['condition']['icon'],
        'wind':response['current']['wind_kph'],
        'humidity':response['current']['humidity'],
        'precipitation':response['current']['precip_mm']
      }
      return flask.render_template("index.html",weather=weather,error="")
    except Exception as e:
      return flask.render_template("index.html",weather=weather,error="enter valid query")
  return flask.render_template("index.html",weather=weather)
