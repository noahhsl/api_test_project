# conftest.py
#
# 要求：
#
# 1. 导入 pytest
#
# 2. 导入：
#    ApiClient
#    UserApi
#
# 3. 定义 fixture：
#
#    api_client()
#
#    base_url =
#    "https://jsonplaceholder.typicode.com"
#
#    创建：
#    client = ApiClient(base_url)
#
#    返回 client
#
#
# 4. 定义 fixture：
#
#    user_api(api_client)
#
#    注意：
#    这里的 api_client 不是普通变量，
#    而是上面那个 fixture 返回的 ApiClient 对象。
#
#    创建：
#    api = UserApi(api_client)
#
#    返回 api
#
#
# 最终目标：
#
# test_user.py 里以后可以直接写：
#
# def test_get_user(user_api):
#     ...
#
# 不需要自己再次创建 ApiClient 和 UserApi。
import pytest
from api.user_api import UserApi
from api.post_api import PostApi
from common.api_client import ApiClient
from config.config import BASE_URL


@pytest.fixture
#这个fixture 提供ApiClient对象
def api_client():
    #base_url = "https://jsonplaceholder.typicode.com"
    client = ApiClient(BASE_URL)
    return client

@pytest.fixture
#这个fixture 提供UserApi对象
#这里传进来的api_client其实是上面return的client,在pytest里可以直接写方法名，pytest会自动调用同名fixture
def user_api(api_client):
    api = UserApi(api_client)
    return api

@pytest.fixture
#这个fixture提供PostApi对象
def post_api(api_client):
    api = PostApi(api_client)
    return api