# Hacky solution for importing sibling modules
import sys,os
sys.path.insert(0, os.path.abspath('..'))

from flask import Flask, request 
import argparse

from endpoints import send_email, bounced_email
from handlers.json_error import JSONErrorHandler

# Add CLI handling for changing the port
parser = argparse.ArgumentParser(description='Simple mail-sending API')
parser.add_argument('-p', '--port', type=int, 
        metavar='PORT', help='The port for the API server (default: 3030)')

app = Flask(__name__)
# Need to implement this handler so we get all of the necessary
# HTTP errors to output in JSON
handler = JSONErrorHandler(app)

# Flask routes
@app.route('/api/v1/send-email', methods=['POST'])
def rt_send_email():
    return send_email.post(request)

@app.route('/api/v1/bounced-email', methods=['POST'])
def rt_bounced_email():
    return bounced_email.post(request)

if __name__ == '__main__':
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port or 3030)
