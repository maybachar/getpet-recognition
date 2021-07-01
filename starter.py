from flask import Flask
from flask import request
from flask import Response
import recognizer
from flask import jsonify

app = Flask(__name__)


@app.route('/api/recognize', methods=['POST'])
def get_regonation():
    request_data = request.form['pet_type']
    imagefile = request.files.get('imagefile', '')
    image = imagefile.read()
    response = recognizer.recognize(image, request_data)
    return jsonify(response)


@app.route("/api/health", methods=["GET"])
def login():
    status_code = Response(status=200)
    return status_code


if __name__ == '__main__':
    app.run()
