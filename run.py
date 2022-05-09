#from wsgiref import headers
from flask import Flask, request
import logging
import requests, time, logging

plugUrl = "http://192.168.1.20/api/luPYdWuR4ZXizpsNJek6yefQLYNUprF5zkZ1BxCS/lights/18/state"
previousTime = time.time()
wattage = 0

app = Flask(__name__)

@app.post("/solar")
def handle_solar_data():
    # Have to use this when using globaly defined vars within another scope
    global wattage
    global previousTime

    # data is a weird form of json where the key is the value we need
    # data is not formated as propper json
    obj = request.form.to_dict(flat=False)
    #convert to int before assigning
    wattage = int(float(list(obj.keys())[0]))
    print(list(obj.keys())[0])

    if (time.time() > previousTime):
        # time is in seconds
        previousTime = time.time() + 60 * 15

        if(wattage > 100):
            # python doesn't have lowercase true as a boolean,
            # had to escape and send data as raw data instead of formated json
            data = '{"on": true}'
            r = requests.put(plugUrl, headers= {}, data = data)
            print(r, r.content)
        else:
            data = '{"on": false}'
            r = requests.put(plugUrl, headers= {}, data = data)
            print(r, r.content)

    return ('', 200)

@app.get("/solar")
def solar_client():
    print(time.time())
    return ("Solar energy charging page. \r\n Current wattage: "+str(wattage), 200)