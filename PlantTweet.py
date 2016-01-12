#Welcome to the Think Physics office plant twitter account code.
import subprocess		#Subprocess allows the programme to run command in the terminal
import picamera	
import time
from twython import Twython, TwythonError
import random
from random_tweets import *	#Import the list of quotes

camera = picamera.PiCamera()

filename = ""

def image_Tweet(status_update):	#this function uploads a photo to twitter
        photo = open(filename, 'rb')
        twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])
        response = twitter.upload_media(media = photo)
        toTweet = tweetList[random.randint(0,len(tweetList))-1]
        print toTweet
        try:
            twitter.update_status(status = toTweet, media_ids=[response['media_id']])
        except TwythonError as e:
            print e

def snap_Photo():	#this function takes a photograph
	camera.capture(filename)
	time.sleep(4)

#load the config file 
config = {}
execfile("PlantTweet_conf.py", config)

#Loop = True

#while Loop == True:
while True:
	hour = int(time.strftime("%H"))
	minute = int(time.strftime("%M"))
	second = int(time.strftime("%S"))	
	filename = (time.strftime("%y-%m-%d-%H-%M-%S-") + "plant.jpg")		
	
	#if hour in range(9, 18) and minute == 0 and second == 0:
	
	if hour % 1 == 0 and minute % 10 == 0 and second == 0:
		snap_Photo()
		image_Tweet(filename)
		print "Tweeted: ",				
		print filename
		if hour == 12:
			avatar = open(filename, 'rb')
			twitter.update_profile_image(image=avatar)
	#upload the file to dropbox		
		print "Uploading image to dropbox"
		subprocess.check_call(["/home/pi/DropBox/Dropbox-Uploader/dropbox_uploader.sh"," upload ", filename, "/"])
		print "Upload successful"
	#delete the file
		time.sleep(3)
		subprocess.check_call(["sudo","rm", filename])	
		print "Image deleted"
