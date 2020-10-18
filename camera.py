from picamera import PiCamera
from time import sleep
import pyrebase
from datetime import datetime
#from firebase_admin import db
"""
#configuration for cloud storage-> project->copy config->change rules to read and write
 {
    apiKey: "APIKEY",
    authDomain: "xyz.firebaseapp.com",
    databaseURL: "https://imagerpitest.firebaseio.com",
    projectId: "xyz",
    storageBucket: "xyz.appspot.com",
    messagingSenderId: "76896579",
    appId: "1:563064811009:web:er08760-89076-980-67",
    measurementId: "G-857349867854"
  }
"""
dateTimeObj = datetime.now()
timestamp=datetime.timestamp(dateTimeObj)
#timestampstr=dateTimeObj.strftime("%d-%b-%Y(%H:%M:%S.%f)") #converting to string timestamp
timestampString=str(timestamp)+'.jpg'
index_value=timestamp
print(index_value)
camera = PiCamera()
camera.start_preview()
sleep(5)
path_local="/home/pi/Desktop/image_captured_recent_"+timestampString
camera.capture(path_local)
#camera.stop_preview()

config_cloud={
    "apiKey": "abc",
    "authDomain": "xyz.firebaseapp.com",
    "databaseURL": "https://xyz.firebaseio.com",
    "projectId": "xyz",
    "storageBucket": "xyz.appspot.com",
    "messagingSenderId": "7638756743865",
    "appId": "1:jhfgjnvhif:web:gfcbgvyu",
    "measurementId": "G-reheguvi"
  }
firebase = pyrebase.initialize_app(config_cloud)
storage = firebase.storage()
path_on_cloud = "images/image_captured_recent_cloud_"+timestampString

storage.child(path_on_cloud).put(path_local)
urlString=storage.child(path_on_cloud).get_url(None)
#print(urlString)
#urlString=storage.child(path_on_cloud).get_url()
#print(urlString)
#storage.child(path_on_cloud).download("test_download.jpg")#for download of image to whichever path


##sending data to realtime database
db=firebase.database()
ref = db.child("ImagesCapturedFromSource") #.child('Image'+str(timestamp))
#data ={'timestamp':str(timestamp),'imageurl':urlString,'feedback':'None','familiarity':'0'}
data ={'name':str(timestamp),'imageUrl':urlString,'familiarity':'None'}
db.child().push(data)






