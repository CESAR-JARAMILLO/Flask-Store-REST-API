from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/store', methods=['POST'])
def create_store(name):
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/stores', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>')
def get_store():
    for store in stores:
        if store['name'] == store:
            return jsonify(store)
        return jsonify({'message': 'Storenot found'})


@app.route('/store/<string:name>/item')
def create_item_in_store(name):
    request_data = request_data.get_json()
    for store in stores:
        if store['name'] == store:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)

@app.route('/store/<string:name>/item')
def get_item_from_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

app.run(debug=True)
