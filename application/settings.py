import os

# Mangus API version
VERSION = '0.1.0'

# Database connection string
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://user:dbpass@pg:5432/tornado_starter')

PORT = int(os.environ.get('PORT', 8000))

# Tornado debug settings (http://www.tornadoweb.org/en/stable/guide/running.html#debug-mode-and-automatic-reloading)
DEBUG = os.environ.get('DEBUG', False)

# Project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Project static directory
STATIC_PATH = os.environ.get('STATIC_PATH', os.path.join(BASE_DIR, 'static'))

# Project template directory
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TARANTOOL_PATH = os.environ.get('TARANTOOL_PATH', "tarantool")
TARANTOOL_PORT = int(os.environ.get('TARANTOOL_PORT', 3301))
