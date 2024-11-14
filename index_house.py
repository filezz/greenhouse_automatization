from flask import Flask,render_template,request,redirect 
import random
import datetime
import serial

information = {#the initial values radnom 
    'list_temp' : [],
    'list_humidity':[] ,
    'list_lightlvl' : [],
    'sensorsID' : 548382,
    'dateTime' : datetime.datetime.now().strftime("%m.%d.%Y,%H:%M:%S")
}

stats= {#dict that contains the avg values  random 15 sensors, makes and avg 
    'avg_temp': 0,
    'avg_humid': 0,
    'avg_lightlvl' :0,
    'sensorsID' : 548382 ,
    'dateTime' : datetime.datetime.now().strftime("%m.%d.%Y,%H:%M:%S")

}
data_arduino = { #dictionary for arduino
    'Humidity' : [] ,
    'Temperature' : [],
    'Light' : [],
    'sensorsID' : 548382 ,
    'dateTime' : datetime.datetime.now().strftime("%m.%d.%Y,%H:%M:%S")

}
            
#def generate_data():
    #append data to the empty list dict maxim 15 measurements
 #   for i in range(0,15):
  #      value_temp = random.uniform(15.0,30.0)
   #     value_humidity = random.uniform(10,100)    
    #    value_light = random.uniform(0,1000) 
     #   information['list_temp'].append(value_temp)
      #  information['list_humidity'].append(value_humidity)
       # information['list_lightlvl'].append(value_light)

def get_values():# get values from arduino 
    cnt = 0
    try :
            arduino = serial.Serial("/dev/ttyUSB0",timeout = 1)
    except:
        print("Watch for Port") 
    cnt = 0;
    
    while True and cnt < 5  :
        bytes_read = arduino.inWaiting()
        if bytes_read > 0:
            data = arduino.readline().decode().strip()
            values  = data.split(",")
            data_arduino['Humidity'].append(float(values[0]))
            data_arduino['Temperature'].append(float(values[1]))
            data_arduino['Light'].append(float(values[2]))
            cnt += 1
            

def get_avg(dict):
    avg_temp = sum(data_arduino['Temperature'])/len(data_arduino['Temperature'])
    avg_humid = sum(data_arduino['Humidity'])/len(data_arduino['Humidity'])
    avg_lightlvl = sum(data_arduino['Light'])/len(data_arduino['Light'])
    dict['avg_temp'] = round(avg_temp,2)
    dict['avg_humid'] = round(avg_humid,2)
    dict['avg_lightlvl'] = round(avg_lightlvl,2)
    

def verify_log(username,password,datab):
        password = password +"\n"
        with open(datab,'r') as file : 
            lines_data = file.readlines()
            for line in lines_data: 
                fields = line.split(",")
                if(fields[0] == username and fields[1] == password):
                    return True
        return False


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/dashboard.html')
def dash():
    get_values()
    #generate_data()
    get_avg(stats)
    return render_template('dashboard.html',**stats)
@app.route('/signup.html')
def sign():
    return render_template('signup.html')


@app.route('/login',methods=['POST'])
def submit():
    name = request.form['username']
    password = request.form['password']

    isLogin = verify_log(name,password,"accounts.txt")
    if isLogin is True : 
        return redirect('dashboard.html')

    else: 
        return redirect('login.html')


if __name__ == '__main__':
    app.run(debug=True)