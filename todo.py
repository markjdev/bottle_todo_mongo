from bottle import Bottle ,redirect, get, debug, run, template, request, abort
from bottle.ext.mongo import MongoPlugin

from bson.objectid import ObjectId
from bson.json_util import dumps

app = Bottle()
plugin = MongoPlugin(uri="mongodb://127.0.0.1", db="tododb", json_mongo=True)
app.install(plugin)


@app.route('/', method='GET')
@app.route('/todo', method='GET')
def index(mongodb):
	items = mongodb['todo'].find({"status": 1})
	return template('templates/list.tpl', items=items)

@app.route('/todo/new', method='GET')
def new(mongodb):
	return template('templates/form.tpl', task='', error='')

@app.route('/todo/new', method='POST')
def new_submitted(mongodb):
	task = request.POST.get('task')

	if task:
		mongodb['todo'].insert_one({"task": task, "status": 1})
		redirect('/')
	else:
		return template('templates/form.tpl', task=task, error="Title must be specified")

@app.route('/todo/<id>/edit', method='GET')
def edit(mongodb, id):

	item = mongodb['todo'].find_one({"_id": ObjectId(id)})

	if item:
		return template('templates/form.tpl', task=item["task"], error='')
	else:
		abort(404, 'Unable to locate task')

@app.route('/todo/<id>/edit', method='POST')
def edit_submitted(mongodb, id):
	
	item = mongodb['todo'].find_one({"_id": ObjectId(id)})

	if not item:
		abort(404, 'Unable to locate task')

        task = request.POST.get('task')

        if task:
		item["task"] = task
                mongodb['todo'].replace_one({"_id": ObjectId(id)}, item)
                redirect('/')
        else:
                return template('templates/form.tpl', task=task, error="Title must be specified")

# Technically, this should use the DELETE method
@app.route('/todo/<id>/delete', method='GET')
def delete(mongodb, id):
	mongodb['todo'].delete_one({"_id": ObjectId(id)})
	redirect('/')

debug(True)
run(app, reloader=True)
