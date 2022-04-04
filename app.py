from flask import Flask, jsonify, request, Response
import pickle, requests
import sys

app = Flask(__name__)

# Modification of https://flask.palletsprojects.com/en/2.1.x/errorhandling/#generic-exception-handlers
from flask import json
from werkzeug.exceptions import HTTPException
import logging # <-- added

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

#Routes--------------------------------------------------------
# Route 1
@app.route('/ping', methods=['GET'])
def ping_pong():
    """ ping should return pong """
    return jsonify('pong!')

# Route 2
@app.route('/word', methods=[ 'GET'])
def wordz():
    word1 = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    word1 = word1.text.upper()
    word = word1[::-1]
    return jsonify(word)

# Route 3
@app.route('/string-count', methods=[ 'POST'])
def length():
    string = request.get_json()
    leng = len(string)
    return jsonify(leng)
