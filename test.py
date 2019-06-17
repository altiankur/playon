from flask import Flask,jsonify,request,redirect, url_for
import requests
import simplejson 
import json
import time

# coding=utf-8
app = Flask(__name__)

@app.route("/home/<name>")
def home(name):
    #uri = "https://api.stackexchange.com/2.0/users?   order=desc&sort=reputation&inname=fuchida&site=stackoverflow"
    uri= "http://api.openweathermap.org/data/2.5/forecast/daily?q="+name+",US&cnt=16&APPID=ae3723984918e29156906ffa2182bf02&units=metric"
    #http://api.openweathermap.org/data/2.5/forecast/daily?q=dublin,US&cnt=10
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    #Jresponse = uResponse.text
    #data = json.loads(Jresponse)
    #result = json.loads(content.decode("utf-8"))
    data1= uResponse.json()
    date = data1['list']
    #for item in data1['city']['coord']['lat']:
    #    print (item)

    city=(data1['city']['name'])
    country=(data1['city']['country'])
    date1=date[0]['dt']
    print (date1)
    date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date1))
    #date=(data1[''][''])
    #lat = data."city".["lat"]
    #print (data['list']['temp']['day'])
    #day=data['list']['temp']['day']
    #print wjdata['data']['current_condition'][0]['temp_C']
    #displayName = data['items'][0]['display_name']# <-- The display name
    #reputation = data['items'][0]['reputation']# <-- The reputation
    #return '''country name is: {}'''.format(lat)
    #return (jsonify(data))
    #return item
    return '''city name is: {} <br> country name is:{} <br> date is: {}'''.format(city,country,date)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('home',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('home',name=user))

if __name__ == "__main__":
    app.run(debug = True)