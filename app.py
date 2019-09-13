from flask import Flask, jsonify, request
from flask_caching import Cache
from scrapper import ScrapperSdk

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
def index():
    data = {
        "status": "running"
    }
    return jsonify(data)

@app.route('/nextday')
def otherday():
    room = request.args.get('room')
    if(room != None):
        url = 'https://sdk.semarangkota.go.id/komunitas/datapenggunaanruangan'+room+'.php?data=lainnya'
    else:
        url = 'https://sdk.semarangkota.go.id/komunitas/datapenggunaanruangan.php?data=lainnya'
    print(url)
    content = ScrapperSdk(url)
    result = content.get()
    return jsonify(result)

@app.route('/today')
def today():
    room = request.args.get('room')
    if(room != None):
        url = 'https://sdk.semarangkota.go.id/komunitas/datapenggunaanruangan'+room+'.php?data=lainnya'
    else:
        url = 'https://sdk.semarangkota.go.id/komunitas/datapenggunaanruangan.php?data=lainnya'
    content = ScrapperSdk(url)
    result = content.get()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)