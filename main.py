import json
import urllib3

from flask import Flask, request, make_response, jsonify

httpgetter = urllib3.PoolManager()
app = Flask(__name__)
log = app.logger


@app.route('/')
def hello():
    return "Hello World!"


def joke():
    baseurl = "http://api.icndb.com/jokes/random"
    result = httpgetter.request('GET', baseurl).data
    data = json.loads(result)
    valueString = data.get('value')
    joke = valueString.get('joke')
    return joke



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
