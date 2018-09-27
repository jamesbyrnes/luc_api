from flask import make_response, jsonify, abort
from sqlite3 import IntegrityError, Error as SqlError

from models.blacklist import Blacklist

__required_fields = ['email_address']

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
    # if we already find it there (UNIQUE constraint)
    blacklist = Blacklist()
    try:
        last_row = blacklist.add_email(request.json['email_address'])
    except IntegrityError as e:
        abort(400, 'Email address already exists in database')
    except SqlError:
        abort(500, 'Failed to write to database')

    return make_response(jsonify({'id': last_row, **request.json}), 201)
