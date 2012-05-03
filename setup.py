import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'ptah',
    'pyramid', 
    'pyramid_debugtoolbar']

test_requires = [
    'nose',
    'ptah',
    'pyramid',]


setup(name='urbsly',
      version='0.0',
      description='urbsly',
      long_description="Your description here",
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      test_suite = 'nose.collector',
      entry_points = """\
        [paste.app_factory]
        main = urbsly.app:main
      """,
      paster_plugins=['pyramid'],
      )
