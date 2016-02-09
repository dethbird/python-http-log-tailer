import os

environment = os.environ.get('Environment', 'dev')
host = os.environ.get('HTTP_HOST', 'localhost')
port = os.environ.get('HTTP_PORT', 8080)
secret = os.environ.get('SECRET', '')

access_log = os.environ.get('ACCESS_LOG', "access.log")
error_log = os.environ.get('ERROR_LOG', "error.log")
