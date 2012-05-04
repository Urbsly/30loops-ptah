from paste.deploy import loadapp
app = loadapp('config:settings.ini', relative_to='.')
