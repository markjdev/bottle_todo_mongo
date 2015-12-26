from bottle import Bottle ,redirect, get, debug, run, template
from bottle.ext.mongo import MongoPlugin

from bson.json_util import dumps

app = Bottle()
plugin = MongoPlugin(uri="mongodb://127.0.0.1", db="tododb", json_mongo=True)
app.install(plugin)


@app.route('/', method='GET')
def index(mongodb):
	items = mongodb['todo'].find({"status": 1})
	return template('templates/list.tpl', items=items)

debug(True)
run(app, reloader=True)
