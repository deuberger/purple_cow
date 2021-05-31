import json

from flask_api import FlaskAPI
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask import request, jsonify, abort, Response

from instance.config import app_config


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    from app.models import Item

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/item/', methods=['POST', 'GET'])
    def item():
        if request.method == "POST":
            rdata = []
            for i in request.data:
                item = Item(name=i["name"])
                item.save()
                rdata.append({
                    'id': item.id,
                    'name': item.name
                })
            response = Response(json.dumps(rdata), mimetype='application/json')
            response.status_code = 201
            return response
        else:
            # GET
            items = Item.get_all()
            results = []

            for item in items:
                obj = {
                    'id': item.id,
                    'name': item.name
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response


    @app.route('/bucketlists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def bucketlist_manipulation(id, **kwargs):
     # retrieve a buckelist using it's ID
        bucketlist = Bucketlist.query.filter_by(id=id).first()
        if not bucketlist:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            bucketlist.delete()
            return {
            "message": "bucketlist {} deleted successfully".format(bucketlist.id) 
         }, 200

        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            bucketlist.name = name
            bucketlist.save()
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            })
            response.status_code = 200
            return response

    return app
