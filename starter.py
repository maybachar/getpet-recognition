from flask import Flask
from flask import request
from flask import Response
import recognizer
from flask import jsonify


app = Flask(__name__)


@app.route('/api/recognize', methods=['POST'])
def pet_recognition():
    # get pet type and image file from request.
    pet_type = request.form['pet_type']
    imagefile = request.files.get('imagefile', '')
    image = imagefile.read()
    # predict breed for this image by suitable model according to pet type.
    response = recognizer.recognize(image, pet_type)
    return jsonify(response)


@app.route("/api/health", methods=["GET"])
def login():
    # if server is alive return status code 200.
    status_code = Response(status=200)
    return status_code


@app.route('/api/recognize_multiply_images', methods=['POST'])
def recognition_multiply_images():
    # all unique result we got from all images.
    map_result = {}
    sum_values = 0
    sum_round = 0
    # the highest result from all images.
    three_highest = {}
    # get pet type and list of images from request.
    pet_type = request.form['pet_type']
    image_list = request.files.getlist("image_list")
    for image_file in image_list:
        image = image_file.read()
        # predict for current image in list.
        response = recognizer.recognize(image, pet_type)
        # for each breed we got in current image-add to map if unique.
        for breed in response:
            # new breed-add as key.
            if breed not in map_result.keys():
                map_result[breed] = list()
            # add new value to list of key breed.
            val = float(response[breed])
            map_result[breed].append(val)
    # for each key in map calculate average percent in all images it preformed.
    for key in map_result:
        sum_list = sum(map_result[key])
        length = len(map_result[key])
        map_result[key] = float("{0:.3f}".format(sum_list/length))
    # get 3 highest keys.
    most_common = sorted(map_result, key=map_result.get, reverse=True)[:3]
    # sum of values of most common.
    for i in most_common:
        sum_values += map_result[i]
    # calculate percent for each breed from most common.
    for i in most_common:
        value = (map_result[i] / sum_values) * 100
        rounded_val = round(value, 3)
        sum_round += rounded_val
        three_highest[i] = str(rounded_val)
    # complete to 100 percent and add to the highest value.
    reminder = 100-sum_round
    three_highest[most_common[0]] = str(float(three_highest[most_common[0]])+reminder)
    return jsonify(three_highest)


if __name__ == '__main__':
    app.run()
