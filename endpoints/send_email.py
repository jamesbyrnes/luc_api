from flask import make_response, jsonify, abort
from sqlite3 import Error as SqlError

from models.blacklist import Blacklist
from integrations.email import EmailIntegrationFactory
from settings import settings

__required_fields = ['to', 'from', 'subject', 'body_text', 'body_html']
settings = settings.get_settings()

def __get_missing_fields(request_json):
    return [field for field in __required_fields 
            if field not in request_json.keys()]

def post(request):
    # Confirm we're dealing with JSON input and that we have the
    # required fields
    if not request.json:
        abort(400, 'Request is not JSON')
    missing_fields = __get_missing_fields(request.json)
    if len(missing_fields) > 0:
        abort(400, 'Request missing the following fields: ' + ', '.join(missing_fields))

    # Check the blacklist DB for the email address and throw an error
    # if we find it there
    blacklist = Blacklist()
    try:
        if blacklist.is_on_blacklist(request.json['to']):
            abort(400, 'Email addressee was found on blacklist')
    except SqlError as e:
        abort(500, 'Failed to read from database')
    
    email_sender = EmailIntegrationFactory.get_integration(settings['email_integration'], request.json)
    return make_response(jsonify(email_sender.get_schema()), 202)
