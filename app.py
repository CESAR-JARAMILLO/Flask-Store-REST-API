from flask import Flask

# Created Flask object with unique name
app = Flask(__name__)

# Created route for application
# Assigned method o route that returns something
@app.route('/')
def home():
    return "Hello, world!"

app.run(debug=True)


# Rest API's normally return strings
# Javascript applications display those strings nicely
