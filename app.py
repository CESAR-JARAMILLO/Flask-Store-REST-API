from flask import Flask

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
    pass

@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass

@app.route('/stores', methods=['GET'])
def get_stores():
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    pass


app.run(debug=True)


# Rest API's normally return strings
# Javascript applications display those strings nicely
