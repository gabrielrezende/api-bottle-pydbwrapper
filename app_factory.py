from bottle import Bottle, JSONPlugin

import datetime
import decimal
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


def create_app():
    app = Bottle()
    app.install(JSONPlugin(json_dumps=lambda o: json.dumps(o, cls=JSONEncoder)))
    return app
