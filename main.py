import json
import urllib3

from flask import Flask, request, make_response, jsonify

httpgetter = urllib3.PoolManager()
app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get("queryResult").get("action")
    except AttributeError:
        return 'json error'

    if action == 'joke':
        res = joke()
    else:
        log.error('Unexpected action.')

    print('Action: ' + action)
    print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': res}))


def joke():
    baseurl = "http://api.icndb.com/jokes/random"
    result = httpgetter.request('GET', baseurl).data
    data = json.loads(result)
    joke = data.get('value').get('joke')
    return joke



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
