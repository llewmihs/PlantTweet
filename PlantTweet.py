#subprocess allows python to run commands in the terminal - 
import subprocess
import picamera
import time
from twython import Twython, TwythonError

camera = picamera.PiCamera()


def image_Tweet(status_update):	#this function uploads a photo to twitter
        photo = open('image.jpg', 'rb')
        response = twitter.upload_media(media = photo)
        try:
            twitter.update_status(status = status_update, media_ids=[response['media_id']])
        except TwythonError as e:
            print e

def snap_Photo():	#this function takes a photograph
	camera.capture('image.jpg')
	
#load the config file and create the API object
config = {}
execfile("PlantTweet_conf.py", config)
twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

Loop = True

while Loop == True:
	hour = int(time.strftime("%H"))
	minute = int(time.strftime("%M"))
	second = int(time.strftime("%S"))	
	
	if hour % 1 == 0 and minute == 0 and second == 0:
		snap_Photo()
		message = "The %d o'clock image" % hour
		image_Tweet(message)
	
	#time.sleep(1)
#	Loop = False


#snap_Photo()
#image_Tweet()
