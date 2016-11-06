import environ

SECRET_KEY = 'secret'
env = environ.Env()
DATABASES = {'default': env.db('DATABASE_URL', 'postgres://user:dbpass@pg:5432/tornado_starter'), }
INSTALLED_APPS = ('model_app',)
