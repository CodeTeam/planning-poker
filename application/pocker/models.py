import asyncio
import json
import datetime

import peewee

from application.base.models import CustomBaseModel


class BaseProjectModel(CustomBaseModel):
    created_at = peewee.DateTimeField(null=True)
    updated_at = peewee.DateTimeField(null=True)
    
    @classmethod
    async def _create(cls, app, data):

        data['created_at'] = datetime.datetime.now()
        data['updated_at'] = datetime.datetime.now()

        return await app.objects.create(cls, **data)
    
    async def _update(self, app, data):
        for k, v in data.items():
            setattr(self, k, v)
        setattr(self, 'updated_at', datetime.datetime.now())
        await app.objects.update(self)
        return self
    
    async def _delete(self, app):
        setattr(self, 'updated_at', datetime.datetime.now())
        await app.objects.delete(self)
        return self


class Role(BaseProjectModel):
    name = peewee.TextField(unique=True)

    class Meta:
        db_table = 'role'


class Profile(BaseProjectModel):
    username = peewee.TextField(unique=True)
    description = peewee.TextField(null=True)
    password = peewee.TextField()
    first_name = peewee.TextField(null=True)
    last_name = peewee.TextField(null=True)
    middle_name = peewee.TextField(null=True)

    class Meta:
        db_table = 'profile'


class ProfileRole(BaseProjectModel):
    profile = peewee.ForeignKeyField(Profile)
    role = peewee.ForeignKeyField(Role)

    class Meta:
        db_table = 'profile_role'
        unique_together = ('profile', 'role')
