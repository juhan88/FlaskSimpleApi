# FlaskSimpleApi
Simple Python Flask Api Services


#Getting Started
Download get-pip.py --> https://bootstrap.pypa.io/get-pip.py

#Tools
Run ```pip get-pip.py```
Run ```pip install virtualenv```

#Create Virtual Enviornment
Create a virtualenv with the following commands
```
cd PROJECT_FOLDER
virtualenv NAME_OF_VIRTUAL_ENVIORNMENT
```

#Starting Simple Flask Api Application Inside Virtual Enviornment
Run ```source NAME_OF_VIRTUAL_ENVIORNMENT/bin/activate```


#Install dependencies within the virtual env
Run ```pip install flask```
Run ```pip install flask-restful```


#Running Application
```
export FLASK_APP=main.py
python main.py
```
You should see the following:
```
(NAME_OF_VIRTUAL_ENVIORNMENT)sswalker:FlaskSimpleApi yamashita$ python main.py
 * Running on http://0.0.0.0:9191/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 971-410-973
 ```
