import os
import sys

sys.path.append('/srv/www/adayatext.com/application/insta')
sys.path.append('/srv/www/adayatext.com/application/')

os.environ['PYTHON_EGG_CACHE'] = '/srv/www/adayatext.com/.python-egg'

os.environ['DJANGO_SETTINGS_MODULE'] = 'insta.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
