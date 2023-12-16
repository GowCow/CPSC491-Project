from flask import Flask
from Homepage import Homepage



app = Flask(__name__)
app.register_blueprint(Homepage, url_prefix="/Homepage")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

