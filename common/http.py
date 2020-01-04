from bottle import HTTPResponse

import datetime
import json
import simplejson


class Response:

    def __init__(self, status):
        if type(status) is not int:
            raise ValueError("Invalid status type")
        self._body = None
        self._status = status
        self._headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, OPTIONS, DELETE",
            "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization",
        }

    def content_type(self, content_type):
        self._headers["Content-Type"] = content_type
        return self

    def headers(self, custom_headers):
        self._headers = dict(**self._headers, **custom_headers)
        return self

    def dateconverter(self, o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    def body(self, data):
        data_ = data

        if self._status >= 300:
            self._body = data
        else:
            if data_ == None:
                self.body = {}
            elif isinstance(data_, dict):
                self._body = json.dumps(data_, default=self.dateconverter)
            elif isinstance(data_, list):
                self._body = json.dumps(data_, default=self.dateconverter)
            else:
                self._body = simplejson.dumps(
                    vars(data_), use_decimal=True, default=str
                )

        return self

    def binary(self, data):
        self._body = data
        return self

    def build(self):
        return HTTPResponse(body=self._body, status=self._status, headers=self._headers)
