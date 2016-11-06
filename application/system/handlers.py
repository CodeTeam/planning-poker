from peewee_async import _run_sql
from tcrudge.handlers import BaseHandler
from tornado.web import RequestHandler

from application import settings
from application.base.models import db


class PingHandler(BaseHandler):
    """
    Health check handler
    """

    async def get(self):
        errors = []
        # Database system check
        try:
            cursor = await _run_sql(db, 'SELECT 1')
            await cursor.release
        except Exception as e:
            errors.append(str(e))

        if errors:
            self.set_status(503)
            self.response(errors=errors)
        else:
            self.response('pong')


class VersionHandler(RequestHandler):
    """
    Current API version handler
    """

    def get(self):
        self.write(settings.VERSION)
