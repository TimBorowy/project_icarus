# Solar charging tool
Conncts to Domotics home automation software and controls a smartplug depending on current power usage.
When power usage is low and solar power is being returned to the net, the smartplus get's activated and can turn on chargers or other equiptment to only use them while the sun is shining.

## Node app
Install packages first:
`npm install`

Then run
`npm run start`


## Python app
Install py packages:

`pip install flask, requests`

Set Py local env:

`export FLASK_APP=app.py`

## Start Python app:
`flask run --host=0.0.0.0`
