import json

import ptah
from pyramid.config import Configurator
from pyramid.asset import abspath_from_asset_spec
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig

auth_policy = AuthTktAuthenticationPolicy('secret')
session_factory = UnencryptedCookieSessionFactoryConfig('secret')


def main(global_config, **settings):
    """ Function which returns a configured Pyramid/Ptah WSIG Application """

    # Construct a db connection URL from 30Loops environment variables
    # pattern is postgresql+psycopg2://scott:tiger@localhost/mydatabase
    env = None
    try:
        f = open('/app/conf/environment.json')
        env = json.load(f)
        db_user = env["DB_USER"]
        db_name = env["DB_NAME"]
        db_host = env["DB_HOST"]
        db_pass = env["DB_PASSWORD"]
        db_url = "postgresql+psycopg2://"+db_user+":"+db_pass+"@"+db_host+"/"+dbname

    # Override the SQLAlchemy url from settings.ini
    if env:
        settings['sqlalchemy.url']=db_url

    # Info: This is how Pyramid is configured.
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
