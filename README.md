# Mailsend API

This is a proof-of-concept API test with the following features:

* Send emails through third-party email sending integrations.
* Add to and track a blacklist of failed emails and prevent future sending to those emails.

## Requirements
* Python >3.6
* sqlite3

## Installation

### Dependencies
 You can install the python dependencies for this program via `pip` or `pipenv`:

```
$ pip install -r requirements.txt
```

```
$ pipenv install
```

### Configuration
A `settings.json` file is required for this file to run. There is currently only one parameter for the file: `email_integration`, which excepts either `amazon` or `sendgrid` as an argument.

## Usage
### Running
Use your preferred method for launching (virtualenv, pipenv, etc.) on `api.py`.

This file take two arguments:

* `-h` or `--help`: Display a help menu.
* `-p PORT` or `--port PORT`: Set the port to something other than the default (3030).

The app will then listen on your selected port or 3030 by default.

### Endpoints
This app has two endpoints:

`POST /api/v1/send-email`: Send an email through an integrated provider as specified in `settings.json`.

* Required MIME type: `application/json`
* Required schema: `from`, `to`, `subject`, `body_html`, `body_text` (all string values)
* Returned MIME type: `application/json`
* Returned data: Restructured schema for the specified email provider.

`POST /api/v1/bounced-email`: Add an email to a "do not send" blacklist.

* Required MIME type: `application/json`
* Required schema: `email_address` (string value)
* Returned MIME type: `application/json`
* Returned data: Email address along with its ID in the database.
