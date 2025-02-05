# Solar charging tool
Connects to Domotics home automation software and controls a smartplug depending on current power usage.
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


## install pip on pi zero

sudo apt-get install python3-distutils

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py


[Unit]
Description=Solar charging service, requires Domoticz
After=network.target

[Service]
Environment="FLASK_APP=/home/pi/project_icarus/run.py"
Type=simple
ExecStart=/home/pi/.local/bin/flask run --host=0.0.0.0
Restart=on-failure
SyslogIdentifier=solarcharging.log
RestartSec=5
TimeoutStartSec=infinity

[Install]
WantedBy=multi-user.target


`/etc/systemd/system/` -> nano solar.service

sudo systemd-analyze verify yourname.service

systemctl enable <service file name without .service extension>

systemctl daemon-reload

systemctl start <service file name without .service extension>


nano ~/.bashrc

export PATH="$HOME/.local/bin/:$PATH"

source ~/.bashrc



## nedis wifi smart plug tuya

https://github.com/codetheweb/tuyapi
https://github.com/codetheweb/tuyapi/blob/master/docs/SETUP.md