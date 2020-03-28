from .base import *

DEBUG = False
WSGI_APPLICATION = 'config.wsgi.production.application'


SECRETS_PRODUCTION=  SECRETS['productions']
print(SECRETS_PRODUCTION)
DATABASES = SECRETS_PRODUCTION

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'che1-db.czxnimwgemge.ap-northeast-2.rds.amazonaws.com',
#         'PORT': '5432',
#         'NAME': 'deploy',
#         'USER': 'Che1',
#         'PASSWORD': '*******',
#     }
# }
INSTALLED_APPS += [

]

MIDDLEWARE += [

]

AWS_ACCESS_KEY_ID = SECRETS_DEFAULT['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS_DEFAULT['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = SECRETS_DEFAULT['AWS_STORAGE_BUCKET_NAME']
