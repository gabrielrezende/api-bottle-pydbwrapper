from app_factory import create_app
from bottle import HTTPResponse, request, response
from livereload import Server
from common.http import Response
# settings.py
from dotenv import load_dotenv
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

import common.system_variable as s
import services.business
import services.email

app = create_app()

app.merge(services.business.app)
app.merge(services.email.app)

@app.get('/')
def api():
    return Response(200).body({'message':'API Sankhya Implantation - OK'}).build()

@app.hook("after_request")
def enable_cors():
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, OPTIONS, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization"


@app.error(400)
def treat_request_400(res):
    if request.method == "OPTIONS":
        return __treat_request_options(res)
    return request.app.default_error_handler(__treat_request_options(res))


@app.error(401)
def treat_request_401(res):
    if request.method == "OPTIONS":
        return __treat_request_options(res)
    return request.app.default_error_handler(__treat_request_options(res))


@app.error(404)
def treat_request_404(res):
    if request.method == "OPTIONS":
        return __treat_request_options(res)
    return request.app.default_error_handler(__treat_request_options(res))


@app.error(405)
def treat_request_405(res):
    if request.method == "OPTIONS":
        return __treat_request_options(res)
    return request.app.default_error_handler(__treat_request_options(res))


def __treat_request_options(res):
    res = HTTPResponse()
    res.headers[
        "Access-Control-Allow-Headers"
    ] = "Accept, Authorization, Content-Type, Origin, X-CSRF-Token, X-Requested-With"
    res.headers["Access-Control-Allow-Methods"] = "DELETE, GET, OPTIONS, POST, PUT"
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


def main():
    if s.ENVIROMENT == 'development':
        server = Server(app)
        server.serve(host='0.0.0.0',port=5000, debug=True)
    else :
        app.run(host="0.0.0.0", port=5000, debug=True, reloader=False)


if __name__ == "__main__":
    main()
