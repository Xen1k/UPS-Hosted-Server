from flask import Flask
from flask_cors import CORS
from user import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix="/user")
cors = CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)