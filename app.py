from flask import Flask
from flask_cors import CORS
from user import user_blueprint
from periphery import periphery_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(periphery_blueprint, url_prefix="/periphery")
cors = CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)