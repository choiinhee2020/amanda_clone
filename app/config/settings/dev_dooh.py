from .base import *

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.dev_dooh.application'

# SECRETS_DEVELOP=  SECRETS['dev']
# print(SECRETS_DEVELOP)
# DATABASES = SECRETS_DEVELOP['DATABASES']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ALLOWED_HOSTS = [
    '*'
]
INSTALLED_APPS += [

]

MIDDLEWARE += [

]

# S3 Storage
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'
AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID = SECRETS_DEFAULT['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS_DEFAULT['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = SECRETS_DEFAULT['AWS_STORAGE_BUCKET_NAME']
