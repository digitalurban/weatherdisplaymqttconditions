
#Script to read the MQTT feed from Weather Display and
#Convert/Publish to a text string based on conditions
#Useful for Scrolling Displays/eink Devices/Home Assistant or Headers on Web Pages
#The text output can be expanded/edited accordingly, based on adding other elements   
#From the ClientRaw Feed. 



import paho.mqtt.client as mqtt

# MQTT Set Up

print("Setting up MQTT Connection")
client = mqtt.Client("WeathertoText") #  create new instance
print("Connecting to the Server")

# MQTT Username/Password  - Edit out with a # if not required
client.username_pw_set("YourMQTTUserName, "YourMQTTPassword")

# Your MQTT Connection/Port - Edit as required

client.connect("MQTTIP/Address", 1883) #  connect to broker


def on_connect(mosq, obj, rc, properties=None):
    print("connect rc: "+str(rc))

# The location of your Weather Display MQTT Feed - using the default values
    
    client.subscribe("wdwf/#")
   
def on_message(mosq, obj, msg):
    contents = str(msg.payload)
    print (contents)

     # Read MQTT Feed

    # Split Based on Spaces

    data = contents.split()

    # Get Conditions Code from ClientRaw

    conditions = (data[48])

    # Get Temperature Code from ClientRaw

    temp = str(data[4])

    # Get Temperature Trend and Convert Code from ClientRaw

    temptrend = int(data[143])

    if temptrend == 1:
        temptrend = "& Rising"
    if temptrend == -1:
        temptrend = "& Falling"

    # Get Pressure Code from ClientRaw

    press = str(data[6])


    # Get Pressure Trend and Convert Code from ClientRaw

    presstrend = float(data[50])

    if presstrend > +0.1:
        presstrend = "& Rising"
    elif presstrend < -0.1:
        presstrend = "& Falling"
    else: presstrend = "& Steady"

    # Get Rain Code from ClientRaw

    rainday = str(data[7])


    # Get Rain Rate Code from ClientRaw - to Trigger Show Rain on MQTT Feed

    rainrate = float(data[10])

    # Get Wind Gust (Av Last 10 Min) Code from ClientRaw

    wind = str(data[158])

    # Get Wind Direction and Convert Code to Readable Direction from ClientRaw

    windir = int(data[3])

    if windir >=  11.25 and windir <  33.75:
        windir = "North North East"
    elif windir >=  33.75 and windir <  56.25:
        windir = "North East"
    elif windir >=  56.25 and windir <  78.75:
        windir = "East North East"
    elif windir >=  78.75 and windir < 101.25:
        windir ="Easterly"
    elif windir >= 101.25 and windir < 123.75:
        windir = "East South East"
    elif windir >= 123.75 and windir < 146.25: 
        windir = "South East"
    elif windir >= 146.25 and windir < 168.75:
        windr = "South South East"
    elif windir >= 168.75 and windir < 191.25:
        windir = "Southerly"
    elif windir >= 191.25 and windir < 213.75:
        windir = "South South West"
    elif windir >= 213.75 and windir < 236.25:
        windir = "South West"
    elif windir >= 236.25 and windir < 258.75:
        windir = "West South West"
    elif windir >= 258.75 and windir < 281.25:
        windir = "Westerly"
    elif windir >= 281.25 and windir < 303.75:
        windir = "West North West"
    elif windir >= 303.75 and windir < 326.25:
        windir = "North West"
    elif windir >= 326.25 and windir < 348.75:
        windir = "North North West"
    else: windir = "Northerly"


    # Remap Conditions Code to Text

    # Sunny

    if conditions == '0':
        conditions = 'Sunny'

    # Mainly cloudy
        
    if conditions == '18':
        conditions = 'Dry, Mainly Cloudy'

    # Partly cloudy
        
    if conditions == '19':
        conditions = 'Partly Cloudy'

    if conditions == '2':
        conditions = 'Partly Cloudy'

    if conditions == '3':
        conditions = 'Partly Cloudy'

    # Sunny Spells
        
    if conditions == '5':
        conditions = 'Sunny Spells'


    # Light Rain

    if conditions == '21':
        conditions = 'Light Rain'
        
    if conditions == '22':
        conditions = 'Light Rain'
        

    if conditions == '23':
        conditions = 'Light Rain'

    # Night Light Rain

    if conditions == '15':
        conditions = 'Light Rain'

    # Rain

    if conditions == '20':
        conditions = 'Rain'

    # Night Rain

    if conditions == '14':
        conditions = 'Night Time: Rain'

    # Stopped raining - Day or Night

    if conditions == '34':
        conditions = 'Stopped Raining'

    # Night Clear
        
    if conditions == '1':
        conditions = 'Night Time, Clear'

    # Night Fog
        
    if conditions == '11':
        conditions = 'Night Time, Mist/Fog'

    # Sleet

    if conditions == '16':
        conditions = 'Sleet'
        
    # Print and Publish Output - Two Outputs - one if raining and one if dry - Edit according to Preference

    output_string = "The Weather is " + conditions + ", " + temp + " Degrees Centigrade " + temptrend + "," + " " + "Pressure: " + press + " Mb " + presstrend + ", Wind "+ windir + " " + wind + " Mph" 

    output_string_rain = "The Weather is " + conditions + temp + " Degrees Centigrade " + temptrend + "," + ", with " + rainday + " mm" + " of rain, " + "Pressure: " + press + " Mb " + presstrend + ", Wind "+ windir + " " + wind + " Mph" 


    print (output_string)

    # Publish to MQTT - edit topic as required
        
    print("Publishing message to topic")
    if rainrate > 0:
       client.publish("weatherdisplay/text", output_string_rain)
       
    else:
         client.publish("weatherdisplay/text", output_string)
         client.publish("weatherdisplay/text", output_string)
    
    
    print (output_string)
    
    # The script runs once and then disconnects - to is made to be run via a Cron Job - 
    # Every set period of time - ie every 5 minutes.

    client.disconnect() #disconnect
 

# Loops for the Connect and Subscribe 

client.on_message = on_message
client.on_connect = on_connect

 
client.loop_forever()
