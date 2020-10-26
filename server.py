from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)

env = {
    "zoom_client_id" : "6oLQjCTuRrYhkUauO9grQ",
    "zoom_client_secret": "iUkad80JIpE2nIQLrfCH6h1oieCYe1SS",
    "zoom_bot_jid" : "v1kxiu0tqiqvso37p8upuo4g@xmpp.zoom.us",
    "zoom_verification_token" : "0gT83fbXSoG__dtwJDxhPg",
}


def sendChat(chatbotToken, request_params={}):
    url = 'https://api.zoom.us/v2/im/chat/messages'
    body = {
      'robot_jid': env["zoom_bot_jid"],
      'to_jid': request_params["toJid"],
      'account_id': request_params["accountId"],
      'content': {
        'head': {
          'text': 'Unsplash'
        },
        'body': [{
          'type': 'message',
          'text': 'You sent ' + request_params["cmd"]
        }]
      }
    }

    headers={
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + chatbotToken
    }
    requests.post(url, headers=headers)

def getChatbotToken():
    url = "https://zoom.us/oauth/token?grant_type=client_credentials"
    requests.post(url, headers={'Authorization': 'Basic ' + env["zoom_client_id"] + ':' + str(env["zoom_client_secret"])})
    body = json.dumps(request.data)
    #sendChat(body.access_token, json_data)


@app.route('/', methods=["GET", "POST"])
def handle_main():
    if request.method == 'POST':
        message = request.form["foo2"]
        print(message)
        json_data = json.loads(message)
        return message
        
    if request.method == "GET":
        return "You're connected to the chatbot. Yay"


@app.route('/support', methods=["GET", "POST"])
def handle_support():
    if request.method == 'GET':
        return ("Contact tommy.gaessler@zoom.us for support.")

@app.route('/privacy', methods=["GET", "POST"])
def handle_privacy():
    if request.method == 'GET':
        return ('The Unsplash Chatbot for Zoom does not store any user data.')

@app.route('/terms', methods=["GET", "POST"])
def handle_terms():
    if request.method == 'GET':
        return ('By installing the Unsplash Chatbot for Zoom, you are accept and agree to these terms...')

@app.route('/documentation', methods=["GET", "POST"])
def handle_privacy_2():
    if request.method == 'GET':
        return ('Try typing "island" to see a photo of an island, or anything else you have in mind!')

@app.route('/zoomverify/verifyzoom.html', methods=["GET", "POST"])
def handle_verification():
    if request.method == 'GET':
        return (env["zoom_verification_token"])

@app.route('/unsplash', methods=["GET", "POST"])
def handle_verification2():
    if request.method == 'POST':
        return ('Chat received')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)