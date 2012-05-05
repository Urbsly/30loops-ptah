import os

import ptah
from pyramid.config import Configurator
from pyramid.asset import abspath_from_asset_spec
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig

auth_policy = AuthTktAuthenticationPolicy('secret')
session_factory = UnencryptedCookieSessionFactoryConfig('secret')


def main(global_config, **settings):
    """ Function which returns a configured Pyramid/Ptah WSIG Application """

    # Info: This is how Pyramid is configured.

    # Originally for Heroku, needs to be modified for 30Loops
    #durl = os.environ.get("DATABASE_URL")
    #if durl:
    #    settings['sqlalchemy.url']=durl

    config = Configurator(settings=settings,
                          session_factory = session_factory,
                          authentication_policy = auth_policy)

    # Info: This includes packages which have Pyramid configuration
    config.include('ptah')
    config.commit()

    # Refer: Ptah: _Initialization_
    config.ptah_init_settings()

    # Refer: Ptah: _Initialization_
    config.ptah_init_sql()

    # enable ptah management
    config.ptah_init_manage(managers=('*',))

    # populate database
    config.ptah_populate()

    # Refer: Pyramid's _URL Dispatch_
    config.add_route('home', '/')

    # static assets
    config.add_static_view('_urbsly', 'urbsly:static')

    # Refer: Pyramid's _Configuration Decorations and Code Scanning_
    config.scan()

    return config.make_wsgi_app()
