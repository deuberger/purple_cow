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

    @app.route('/item/', methods=['POST', 'GET', 'DELETE'])
    def item():
        if request.method == "POST":
            results = []
            for i in request.data:
                item = Item(name=i["name"])
                item.save()
                results.append({
                    'id': item.id,
                    'name': item.name
                })
            response = jsonify(results)
            response.status_code = 201
            return response
        elif request.method == "GET":
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
        elif request.method == 'DELETE':
            Item.delete_all()
            response = Response()
            response.status_code = 200
            return response

    @app.route('/item/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def item_manipulation(id, **kwargs):
        item = Item.query.filter_by(id=id).first()
        if not item:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            item.delete()
            response = Response()
            response.status_code = 200
            return response

        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            item.name = name
            item.save()
            response = jsonify({
                'id': item.id,
                'name': item.name
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': item.id,
                'name': item.name
            })
            response.status_code = 200
            return response

    return app
