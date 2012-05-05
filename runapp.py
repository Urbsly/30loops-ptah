import os.path
from pyramid.paster import get_app
app = get_app(os.path.join(os.path.dirname(__file__), 'settings.ini'))
