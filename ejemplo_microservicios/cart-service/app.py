from flask import Flask, Blueprint
from blueprints import blueprints
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

for blueprint in blueprints:
    app.register_blueprint(blueprint, url_prefix="/" + str(blueprint.name))

if __name__ == "__main__":
    app.run('0.0.0.0', port=9000)