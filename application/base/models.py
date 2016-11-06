import os

import peewee
import peewee_async
from playhouse.db_url import parse

from application import settings
from tcrudge.models import BaseModel

db_param = parse(os.environ.get("DATABASE_URL", settings.DATABASE_URL))

db = peewee_async.PooledPostgresqlDatabase(**db_param)
db.allow_sync = False


class CustomBaseModel(BaseModel):
    """
    Base class for other models
    """

    class Meta:
        database = db
