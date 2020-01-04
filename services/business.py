from app_factory import create_app
from bottle import request
from business.business import BusinessBo
from common.exceptions import EntityError
from common.http import Response
from utils.formatter import Formatter
from utils.validation import required_fields

import common.messages as m
import datetime

URL = '/business'
BO = BusinessBo

app = create_app()


@app.get(URL)
def get_all():
    try:
        result = BO().find_all()
        return Response(200).body(result).build()
    except EntityError as ee:
        return Response(ee.code).body({"error": ee.message}).build()
    except Exception as e:
        return Response(500).body({"error": str(e)}).build()


@app.get(URL+'/<id>')
def get_by_id(id):
    try:
        result = BO().find_by_id(id)
        return Response(200).body(result).build()
    except EntityError as ee:
        return Response(ee.code).body({"error": ee.message}).build()
    except Exception as e:
        return Response(500).body({"error": str(e)}).build()

@app.get(URL+'/code/<code>')
def get_by_code(code):
    try:
        result = BO().find_by_code(code)
        return Response(200).body(result).build()
    except EntityError as ee:
        return Response(ee.code).body({"error": ee.message}).build()
    except Exception as e:
        return Response(500).body({"error": str(e)}).build()        

@app.post(URL)
def insert():
    try:
        data = request.json
        
        result = BO().find_by_code(data['code'])

        if result:
            return Response(302).body({'data':result, "message":"Entidade já existesnte."}).build()

        result = BO().insert(data)

        return Response(201).body({"message":"Inserido com sucesso."}).build()
    except EntityError as ee:
        return Response(ee.code).body({"error": ee.message}).build()
    except Exception as e:
        return Response(500).body({"error": str(e)}).build()        

@app.put(URL)
def update():
    try:
        data = request.json
        
        result = BO().find_by_id(data['id'])

        if not result:
            return Response(302).body({'data':result, "message":"Entidade já existesnte."}).build()

        result = BO().update(data)

        return Response(200).body({"message":"Alterado com sucesso."}).build()
    except EntityError as ee:
        return Response(ee.code).body({"error": ee.message}).build()
    except Exception as e:
        return Response(500).body({"error": str(e)}).build()            


@app.delete(URL+'/<id>')
def delete(id):
    try:
        result = BO().find_by_id(id)

        if not result:
            return Response(204).body({'data':result, "message":"Entidade não encontrada."}).build()

        result = BO().delete(id)

        return Response(200).body({"message":"Deletado com sucesso."}).build()
    except EntityError as ee:
        return Response(ee.code).body({"error": ee.message}).build()
    except Exception as e:
        return Response(500).body({"error": str(e)}).build()

@app.get(URL+'/procedure/<id>')
def get_by_procedure(id):
    try:
        result = BO().find_by_procedure(id)
        return Response(200).body(result).build()
    except EntityError as ee:
        return Response(ee.code).body({"error": ee.message}).build()
    except Exception as e:
        return Response(500).body({"error": str(e)}).build() 