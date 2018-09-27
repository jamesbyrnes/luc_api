from abc import ABC, abstractmethod

class EmailIntegration(ABC):
    def __init__(self, email_data):
        self.schema = self.make_schema(email_data)

    @abstractmethod
    def make_schema(self, email_data):
        raise NotImplementedError('This method has not been implemented')

    @abstractmethod
    def send_email(self):
        raise NotImplementedError('This method has not been implemented')

    def get_schema(self):
        return self.schema

class EmailIntegrationFactory(object):
    @staticmethod
    def get_integration(typ, email_data):
        if (typ == 'amazon'):
            return AmazonEmailIntegration(email_data) 
        elif (typ == 'sendgrid'):
            return SendgridEmailIntegration(email_data)
        else:
            raise NotImplementedError('This integration has not been implemented')

class AmazonEmailIntegration(EmailIntegration):
    def make_schema(self, email_data):
        return {
            'Destination': {
                'ToAddresses': [email_data['to']]
            },
            'Message': {
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': email_data['body_html']
                    },
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': email_data['body_text']
                    }
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': email_data['subject']
                }
            },
            'Sender': email_data['from']
        }

    def send_email(self):
        super()

class SendgridEmailIntegration(EmailIntegration):
    def make_schema(self, email_data):
        return {
            "personalizations": [{
                "to": [{
                    "email": email_data['to']
                }],
                "subject": email_data['subject']
            }],
            "from": {
                "email": email_data['from']
            },
            "content": [
                {
                    "type": "text/plain",
                    "value": email_data['body_text']
                },
                {
                    "type": "text/html",
                    "value": email_data['body_html']
                }
            ]
        }

    def send_email(self):
        super()
