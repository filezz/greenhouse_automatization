import datetime 
import random
import serial
####move this to fucking index_house for random then check 

information = {#the initial values
    'list_temp' : [],
    'list_humidity':[] ,
    'list_lightlvl' : [],
    'sensorsID' : 548382,
    'dateTime' : datetime.datetime.now().strftime("%m.%d.%Y,%H:%M:%S")
}
stats= {#dict that contains the avg values 
    'avg_temp': 0,
    'avg_humid': 0,
    'avg_lightlvl' :0,
    'sensorsID' : 548382 ,
    'dateTime' : datetime.datetime.now().strftime("%m.%d.%Y,%H:%M:%S")

}
def generate_data():
    #append data to the empty list dict maxim 10 measurements
    for i in range(0,15):
        value_temp = random.uniform(15.0,30.0)
        value_humidity = random.uniform(10,100)
        value_light = random.uniform(0,1000) 
        information['list_temp'].append(value_temp)
        information['list_humidity'].append(value_humidity)
        information['list_lightlvl'].append(value_light)
def get_avg():
    avg_temp = sum(information['list_temp'])/len(information['list_temp'])
    avg_humid = sum(information['list_humidity'])/len(information['list_humidity'])
    avg_lightlvl = sum(information['list_lightlvl'])/len(information['list_lightlvl'])
    stats['avg_temp'] = round(avg_temp,2)
    stats['avg_humid'] = round(avg_humid,2)
    stats['avg_lightlvl'] = round(avg_lightlvl,2)

def reset(dict):
    for key in dict: 
       name = key.split("_")
       if(name[0] == 'list'):
           dict[key].clear()
    
generate_data()
get_avg()

print(information)
print("-----------------------------------------------")
print(stats)
print("-------------------------------after reset")
reset(information)
print(information)



