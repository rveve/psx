#!flask/bin/python
from flask import Flask, jsonify, request, make_response, abort

import hashlib

app = Flask(__name__)

hash_dict = dict()

@app.route('/')
def index():
    return "Paxos message digest generator!\n"

@app.route('/messages', methods=['POST'])
def generate_hash():
        message=request.json['message']
        hash_object = hashlib.sha256(message.encode('utf-8'))
        mess_digest = hash_object.hexdigest()
        hash_dict[mess_digest] = message
        return jsonify({'digest': mess_digest}), 201

@app.route('/messages/<string:mess_digest>', methods=['GET'])
def get_message(mess_digest):
        if not mess_digest in hash_dict:
                 abort(make_response(jsonify(err_msg="Message digest {} not found".format(mess_digest)), 404))
        return jsonify({'message': hash_dict[mess_digest]})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True)
