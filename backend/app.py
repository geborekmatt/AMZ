from flask import Flask, jsonify
from flask_cors import CORS
from flask import send_from_directory
from brands_routes import brands_bp
from products_routes import products_bp
from celery import Celery
import redis
import task_config

from hopper_routes import hopper_bp
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

redis_cache = redis.from_url(task_config.redis_cache_url,decode_responses=True)

def make_celery(app) :
    celery = Celery(app.import_name, broker=task_config.celery_broker_url)
    celery.conf.update(result_backend=task_config.celery_result_backend)
    TaskBase= celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

@celery.task(name='api_task', bind=True)
def api_task(self):
    print("executing task")
    return {"results":"executed"}


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60, api_task.s()
    )

CORS(app, resources={r'/*': {'origins':'*'}})
app.register_blueprint(brands_bp)
app.register_blueprint(hopper_bp)
app.register_blueprint(products_bp)
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
