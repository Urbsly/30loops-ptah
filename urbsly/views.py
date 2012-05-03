import logging
import ptah
from pyramid.view import view_config

log = logging.getLogger(__name__)


@view_config(renderer='urbsly:templates/homepage.pt',
             route_name='home')

class HomepageView(object):

    def __init__(self, request):
        self.request = request
        ptah.include(request, 'bootstrap')
        ptah.include(request, 'bootstrap-js')

    def __call__(self):
        request = self.request
        self.rendered_includes = ptah.render_includes(request)
        self.rendered_messages = ptah.render_messages(request)
        return {}
