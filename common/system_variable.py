import os

ENVIROMENT = os.getenv('ENVIROMENT','development')
DATABASE_HOST = os.getenv('DATABASE_HOST','localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT','5432')
DATABASE_DB_NAME = os.getenv('DATABASE_DB_NAME','implantation')
DATABASE_USER = os.getenv('DATABASE_USER','master')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD','root')

# EMAIL SSO SERVICE
# EMAIL_SERVICE_URL = os.environ.get('EMAIL_SERVICE_URL', "")
# EMAIL_SERVICE_DEFAULT_SENDER = os.environ.get('EMAIL_SERVICE_DEFAULT_SENDER', "contato@yandeh.com.br")
# EMAIL_SERVICE_DEFAULT_SENDER_NAME = os.environ.get('EMAIL_SERVICE_DEFAULT_SENDER_NAME', "Contato Yandeh")
# EMAIL_REDIRECT_URL = os.environ.get('EMAIL_REDIRECT_URL', 'https://portalerp.devyandeh.com.br')

# EMAIL SMTP GENERIC SERVICE
# MAILER_HOST = os.getenv('MAILER_HOST', 'smtp.gmail.com')
# MAILER_PORT = os.getenv('MAILER_PORT', '587')
# MAILER_USERNAME = os.getenv('MAILER_USERNAME', 'crm.integracao@apoioaonegocio.com.br')
# MAILER_PASSWORD = os.getenv('MAILER_PASSWORD', 'crmintegracao2018')
# APP_URL = os.getenv('APP_URL')