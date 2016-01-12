#subprocess allows python to run commands in the terminal - 
import subprocess
import picamera
import time
from twython import Twython, TwythonError
import random
from random_tweets import *

camera = picamera.PiCamera()

filename = ""
#message = ""

"""
tweetList = [
	"Two in the hand is worth one in the bush",
	"A watched pot never boils",
	"Destroy the seed of evil, or it will grow up to your ruin.",
	"A small fire is soon quenched.",
	"The Changjiang River waves behind drive the waves ahead.",
	"Trial often exhibits truly wonderful results.",
	"When baffled in one direction a man of energy will not despair, but will find another way to his object.",
	"A good opportunity is seldom presented, and is easily lost.",
	"Father's debt, son to give back."
	]
"""

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

#load the config file and create the API object
config = {}
execfile("PlantTweet_conf.py", config)
#twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

Loop = True

# safe code below
while Loop == True:
	hour = int(time.strftime("%H"))
	minute = int(time.strftime("%M"))
	second = int(time.strftime("%S"))	
	filename = (time.strftime("%y-%m-%d-%H-%M-%S-") + "plant.jpg")		
	
	if hour % 1 == 0 and minute % 1 == 0 and second % 20 == 0:
		snap_Photo()
		image_Tweet(filename)
		print "Tweeted: ",				
		print filename
		
		print "Uploading image to dropbox"
		subprocess.check_call(["/home/pi/DropBox/Dropbox-Uploader/dropbox_uploader.sh"," upload ", filename, "/"])
		print "Upload successful"
	#delete the file
		time.sleep(3)
		subprocess.check_call(["sudo","rm", filename])	
		print "Image deleted"
	#time.sleep(1)
