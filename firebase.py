import pyrebase
import os
import base64
from io import BytesIO
import PIL as Image

# userID={"username": "UOa2", "password": "abc", "key":"1234"}
# path = userID["username"]+"/"

firebaseConfig = {
  "apiKey": "AIzaSyCrE2-NwCRX_aYNqWLO2vccndLsjFKpI6k",
  "authDomain": "cryptoimagesystem.firebaseapp.com",
  "projectId": "cryptoimagesystem",
  "storageBucket": "cryptoimagesystem.appspot.com",
  "databaseURL": "cryptoimagesystem.appspot.com",
  "messagingSenderId": "116703538213",
  "appId": "1:116703538213:web:0f4e675d3d7ed62133a3cc",
  "measurementId": "G-4RQGMEBKYV",
  "serviceAccount": "serviceKey.json"
};

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage=firebase_storage.storage()

def uploadImage(username, image_name):
  storage.child(username+"/"+image_name).put(image_name)

def downloadImage(username, image_name):
  # if(os.path.exists(username + '/')==False):
  #   os.mkdir(username + '/')
  storage.child(username+"/"+image_name).download(username+'/'+image_name)

def encodeImage(filename):
    with open(filename, "rb") as image_file:
        byte_string = base64.b64encode(image_file.read())
    # return byte_string
    f = open(filename.split('.',1)[0] + '.txt', 'wb')
    f.write(byte_string)

def decodeImage(imagename, bytestring):
    # with open(filename, "rb") as image_file:
    #     byte_string = image_file.read()

    decoded = base64.b64decode(bytestring)
    # return decoded
    # filename = imagename.split('.',1)[0]
    fh = open(imagename, 'wb')
    fh.write(decoded)

# uploadImage("abc.png")

# allFiles=storage.list_files()
# print(str(allFiles))
# for file in allFiles:
#     print(file.name, type(file.name))

downloadImage("suir2","abc.png")

# for file in allFiles:
#     print(file.name)
#     if file.name == 'UOa2/abc.png':
#         print('downloading')
#         if(os.path.exists(path)==False):
#             os.mkdir(path)
#         storage.child(file.name).download(file.name)