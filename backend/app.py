from flask import Flask, jsonify
from flask_cors import CORS
from flask import send_from_directory
from brands_bp import brands_bp
from hopper_routes import hopper_bp
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins':'*'}})
app.register_blueprint(brands_bp)
app.register_blueprint(hopper_bp)
@app.route("/", defaults={"path":""})
@app.route("/<path:path>")
def index(path):
	print("hitting index()")
	return send_from_directory(app.static_folder,"index.html")

    
@app.route('/api/testMattAPI',methods=['GET','POST'])
def homeAPI():
    return jsonify('homeAPI!')

@app.route('/ping',methods=['GET','POST'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
