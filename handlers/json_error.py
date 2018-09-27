from flask import jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

class JSONErrorHandler(object):
    def __init__(self, app=None):
        if app:
            self.app = app
            self.register(HTTPException)
            for code, v in default_exceptions.items():
                self.register(code)

    def std_handler(self, error):
        if isinstance(error, HTTPException):
            response = jsonify(message=error.description)
            response.status_code = error.code
        else:
            response = jsonify(message="The server encountered an internal error.")
            response.status_code = 500
        return response

    def register(self, exception_or_code, handler=None):
        self.app.errorhandler(exception_or_code)(handler or self.std_handler)
