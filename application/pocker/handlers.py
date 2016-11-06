import asyncio

from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from tcrudge.handlers import ApiListHandler, ApiItemHandler

from application.pocker.models import Profile, Role, ProfileRole


class ProfileListHandler(ApiListHandler):
    model_cls = Profile

    get_schema_input = {}
    post_schema_input = {}


class ProfileDetailHandler(ApiItemHandler):
    model_cls = Profile

    get_schema_input = {}
    put_schema_input = {}
    delete_schema_input = {}


class RoleListHandler(ApiListHandler):
    model_cls = Role

    get_schema_input = {}
    post_schema_input = {}


class RoleDetailHandler(ApiItemHandler):
    model_cls = Role

    get_schema_input = {}
    put_schema_input = {}
    delete_schema_input = {}


class AuthHandler(ApiListHandler):
    model_cls = None

    get_schema_input = {}
    post_schema_input = {}

    executor = ThreadPoolExecutor(max_workers=4)

    @run_on_executor
    def background_task(self, sesion, id_user, roles):
        return self.application.tarantool.insert("main", (sesion, id_user, roles))
    
    @run_on_executor
    def background_select(self, session):
        return self.application.tarantool.select("main", session)

    async def get(self):
        ses = await asyncio.wrap_future(self.background_select("123"))
        print(ses)
        print(ses[0][1])
        self.response(result='dd')
    
    async def post(self):
        self.background_insert("dasdsadasd", 212, 2323)
        self.response(result=await self.serialize({'dd'}))
