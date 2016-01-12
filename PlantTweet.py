#subprocess allows python to run commands in the terminal - 
import subprocess
import picamera
import time
from twython import Twython, TwythonError

camera = picamera.PiCamera()

filename = ""
#message = ""

list = [
	"Two in the hand is worth one in the bush",
	"A watched pot never boils"
	]

def image_Tweet(status_update):	#this function uploads a photo to twitter
        photo = open(filename, 'rb')
        response = twitter.upload_media(media = photo)
        try:
            twitter.update_status(status = status_update, media_ids=[response['media_id']])
        except TwythonError as e:
            print e

def snap_Photo():	#this function takes a photograph
	camera.capture(filename)
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
	filename = (time.strftime("%y-%m-%d-%H-%M-%S-") + "plant.jpg")		
	
	if hour % 1 == 0 and minute % 1 == 0 and second % 20 == 0:
		snap_Photo()
		image_Tweet(filename)
		print "Tweeted: ",				
		print filename
			
	#delete the file
		time.sleep(3)
		subprocess.check_call(["sudo","rm", filename])	
		print "Image deleted"
	#time.sleep(1)
