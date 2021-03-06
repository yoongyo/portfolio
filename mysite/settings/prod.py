from .common import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['yoongyoPortfolio.pythonanywhere.com']

# DATABASE
db_from_env = dj_database_url.config(env='DATABASE_URL', conn_max_age=500)

# 기존 DATABASES
DATABASES['default'].update(db_from_env)

# with open(os.path.join(BASE_DIR, 'secret.json'), 'r') as f:
#     secret = json.loads(f.read())


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mysite', 'staticfiles')
STATICFILES_DIRS = [
 os.path.join(BASE_DIR,  'mysite', 'static'),
]