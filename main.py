import json
import urllib3

from flask import Flask, request, make_response, jsonify

httpgetter = urllib3.PoolManager()
app = Flask(__name__)
log = app.logger


@app.route('/', methods=['GET', 'POST'])
def webhook():
    req = request.get_json()
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return "wrong json"
        
    if action == 'joke.get':
        res = joke()
        res = '<speak><audio src="https://actions.google.com/sounds/v1/cartoon/slide_whistle.ogg">did not get your audio file</audio></speak>'
    else:
        res = "action not found"
    return make_response(jsonify({'fulfillmentText': res}))


def joke():
    baseurl = "http://api.icndb.com/jokes/random"
    result = httpgetter.request('GET', baseurl).data
    data = json.loads(result)
    joke = data.get('value').get('joke')
    return joke



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
