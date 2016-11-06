import json

import msgpack
import pytest

from application.settings import VERSION
from application.system import handlers as system_handlers


def async_err_func_getter(exception, msg='Test exception'):
    """
    Async error function creator
    """

    async def async_err_func(*args, **kwargs):
        """
        Async error function. Raises exception with msg text
        Just because we can not raise in lambda
        """
        raise exception(msg)

    return async_err_func


@pytest.mark.gen_test
async def test_ping_handler(http_client, base_url):
    """
    Test ping handler
    """

    resp = await http_client.fetch(base_url + '/ping/')
    assert resp.code == 200

    data = json.loads(resp.body.decode())
    assert data['errors'] == []
    assert data['result'] == 'pong'


@pytest.mark.gen_test
async def test_ping_error(http_client, base_url, monkeypatch):
    """
    Test ping handler error handling
    """
    monkeypatch.setattr(system_handlers, '_run_sql', async_err_func_getter(Exception))

    resp = await http_client.fetch(base_url + '/ping/', raise_error=False)

    assert resp.code == 503
    data = json.loads(resp.body.decode())
    assert 'errors' in data
    assert len(data['errors']) == 1
    assert data['errors'][0] == 'Test exception'


@pytest.mark.gen_test
async def test_ping_handler_msgpack(http_client, base_url):
    """
    Test ping handler with msgpack
    """

    resp = await http_client.fetch(base_url + '/ping/', headers={'Accept': 'application/x-msgpack'})
    assert resp.code == 200

    data = msgpack.unpackb(resp.body, encoding='utf-8')
    assert data['errors'] == []
    assert data['result'] == 'pong'


@pytest.mark.gen_test
async def test_version_handler(http_client, base_url):
    """
    Test version handler
    """
    response = await http_client.fetch(base_url + '/version/')
    assert response.code == 200
    assert response.body.decode() == VERSION
