#subprocess allows python to run commands in the terminal - 
#this is for the DropBox upload
import subprocess

#the picamera to take the snaps!
import picamera

#time will let us take photos at different times of the day
import time

#twython allows us to upload images to twitter
from twython import Twython

#load the config file
config = {}
execfile("PlatTweet_conf.py", config)

#create the twitter API object
#test
