import asyncio
import tarantool
import peewee_async
from tornado import web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from application import settings
from application.base.models import db
from application.system import handlers as system_handlers

from application.pocker.handlers import (
    ProfileListHandler, ProfileDetailHandler, RoleListHandler, RoleDetailHandler,
    AuthHandler
)

IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')


class DocsHandler(web.RequestHandler):
    """
    Swagger project documentation
    To configure Swagger use ../static/swagger.json
    """

    def get(self, *args, **kwargs):
        self.render('swagger.html')


app_handlers = [
    # System handlers
    ('^/ping/?$', system_handlers.PingHandler),
    ('^/version/?$', system_handlers.VersionHandler),
    # Docs
    ('^/docs/?$', DocsHandler),
    ('^/api/v1/profiles/', ProfileListHandler),
    ('^/api/v1/profiles/([^/]+)/', ProfileDetailHandler),
    ('^/api/v1/roles/', RoleListHandler),
    ('^/api/v1/roles/([^/]+)/', RoleDetailHandler),
    ('^/api/v1/auth/', AuthHandler),
]

if settings.DEBUG:
    # Serve static by Tornado in debug mode (for Vagrant environment)
    # If running in Docker, static files are served by Nginx
    app_handlers.append((r'/static/(.*)', web.StaticFileHandler, {'path': settings.STATIC_PATH}))

application = web.Application(app_handlers, debug=settings.DEBUG, template_path=settings.TEMPLATE_PATH)

# ORM
application.objects = peewee_async.Manager(db)
application.tarantool = tarantool.connect(
    settings.TARANTOOL_PATH, 
    settings.TARANTOOL_PORT
)


def runserver():
    if settings.DEBUG:
        application.listen(settings.PORT, '0.0.0.0')
    else:
        server = HTTPServer(application)
        server.bind(settings.PORT)
        server.start(0)
    loop = asyncio.get_event_loop()
    loop.run_forever()
