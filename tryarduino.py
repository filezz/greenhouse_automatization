import serial
import datetime

data_arduino = { #dictionary for arduino
    'Humidity' : [] ,
    'Temperature' : [],
    'Light' : [],
    'sensorsID' : 548382 ,
    'dateTime' : datetime.datetime.now().strftime("%m.%d.%Y,%H:%M:%S")

}

stats= {#dict that contains the avg values  random 15 sensors, makes and avg 
    'avg_temp': 0,
    'avg_humid': 0,
    'avg_lightlvl' :0,
    'sensorsID' : 548382 ,
    'dateTime' : datetime.datetime.now().strftime("%m.%d.%Y,%H:%M:%S")

}

def get_avg(dict):
    avg_temp = sum(data_arduino['Temperature'])/len(data_arduino['Temperature'])
    avg_humid = sum(data_arduino['Humidity'])/len(data_arduino['Humidity'])
    avg_lightlvl = sum(data_arduino['Light'])/len(data_arduino['Light'])
    dict['avg_temp'] = round(avg_temp,2)
    dict['avg_humid'] = round(avg_humid,2)
    dict['avg_lightlvl'] = round(avg_lightlvl,2)


def get_values():
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
            
        
get_values()
get_avg(stats)
print(data_arduino)
print("-------------------")
print(stats)

