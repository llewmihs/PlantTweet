#subprocess allows python to run commands in the terminal - 
import subprocess
import picamera
import time
from twython import Twython, TwythonError

camera = picamera.PiCamera()

filename = ""
message = ""

def image_Tweet(status_update):	#this function uploads a photo to twitter
        photo = open(message, 'rb')
        response = twitter.upload_media(media = photo)
        try:
            twitter.update_status(status = status_update, media_ids=[response['media_id']])
        except TwythonError as e:
            print e

def snap_Photo():	#this function takes a photograph
	camera.capture(message)
	time.sleep(4)

#load the config file and create the API object
config = {}
execfile("PlantTweet_conf.py", config)
twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

Loop = True

# safe code below
while Loop == True:
	hour = int(time.strftime("%H"))
	minute = int(time.strftime("%M"))
	second = int(time.strftime("%S"))	
	message = (time.strftime("%d-%m-%y %H:%M:%S ") + "plant.jpg")		
	
	if hour % 1 == 0 and minute % 1 == 0 and second % 20 == 0:
		snap_Photo()
		image_Tweet(message)
		print "Tweeted: ",				
		print message
			
	#delete the file
		time.sleep(3)
		subprocess.check_call(["sudo","rm", message])	
		print "Image deleted"
	#time.sleep(1)
