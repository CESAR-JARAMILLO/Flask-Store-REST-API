from flask import Flask, jsonify, request

# Created Flask object with unique name
app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
            'name': 'My item',
            'price': 15.99
            }
        ]
    }
]


# Created route for application
# Assigned method a route that returns something
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message': 'Store not found.'})


@app.route('/stores', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
        return jsonify({'message': 'Store not found.'})

@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == 'name':
            return jsonify({'items': store['items']})
        else:
            return jsonify({'message': 'Store not found.'})


app.run(debug=True)


# Rest API's normally return strings
# Javascript applications display those strings nicely
