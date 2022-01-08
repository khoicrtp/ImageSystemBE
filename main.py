from logging import debug
from flask.json import jsonify
from firebase import decodeImage, downloadImage, encodeImage, uploadImage
from query import *
import flask
from flask_restful import Api, Resource, reqparse, abort
import json
import zipfile
import os

app = flask.Flask(__name__)
api = Api(app)

def abort_register(user, password, confirm_password):
    if password != confirm_password:
        abort(404, message='Confirm password does not match')
    if user:
        abort(404, message='Username existed')

def abort_login(user):
    if not user:
        abort(404, message='Username does not exist or password is wrong')

# @app.route("/<string:username>", methods=["GET"])
# def login(username):
#     user = selectUser(username)
#     abort_login(user)
#     if user[0][1] == password:
#         return ''
#     else: return '', 404

@app.route("/users/login/", methods=["GET"])
def login():
    json_data = json.loads(flask.request.get_json())
    username = json_data["username"]
    password = json_data["password"]
    user = selectUser(username)
    abort_login(user)
    if user[0][1] == password:
        return ''
    else: return '', 404

@app.route("/users/register/", methods=["POST"])
def register():
    json_data = json.loads(flask.request.get_json())
    username = json_data["username"]
    password = json_data["password"]
    confirm_password = json_data["confirm_password"]
    publickey = json_data["publickey"]
    user = selectUser(username)
    abort_register(user, password, confirm_password)
    insertUser(username, password, publickey)
    return ''

@app.route("/<string:username>/<string:image_name>/", methods=["POST"])
def postImage(username, image_name):
    file = flask.request.files['file']
    bytestring = file.read()
    decodeImage(image_name, bytestring)
    uploadImage(username, image_name)
    insertImage(username, image_name)
    # print(flask.request.get_json())
    # json_data = json.loads(flask.request.get_json())
    # username = json_data["username"]
    # print(username)
    # image_name = json_data["image_name"]
    return ''

@app.route("/<string:username>/<string:image_name>/", methods=["GET"])
def getImage(username, image_name):
    downloadImage(username, image_name)
    encodeImage(username+'/'+image_name)
    return flask.send_from_directory(username, image_name.split('.',1)[0] + '.txt', as_attachment=True)

@app.route("/<string:username>/images/", methods=["GET"])
def getImages(username):
    images = selectAllImage(username)
    list_images = []
    list_txt = []
    for i in range(len(images)):
        image_name = images[i][0]
        list_images.append(image_name)
        list_txt.append(image_name.split('.',1)[0]+'.txt')

    zipf = zipfile.ZipFile('Name.zip','w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk(username+'/'):
        for file in files:
            if file in list_images:
                encodeImage(username+'/'+file)
                zipf.write(username+'/'+file.split('.',1)[0]+'.txt')
    zipf.close()
    return flask.send_file('Name.zip',
            mimetype = 'zip',
            attachment_filename= 'Name.zip',
            as_attachment = True)


# api.add_resource(UsersLogin, "/users/login")
# api.add_resource(UsersRegister, "users/register")

if __name__ == "__main__":
    app.run() # debug=True to log all output/debug