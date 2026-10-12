# tests/test_user.py
#
# 要求：
#
# 1. 定义：
#    test_get_user(user_api)
#
#    调用：
#    response = user_api.get_user(1)
#
#    断言：
#    response.status_code == 200
#
#    获取：
#    data = response.json()
#
#    断言：
#    data["id"] == 1
#
#
# 2. 定义：
#    test_create_user(user_api)
#
#    调用：
#    response = user_api.create_user(
#        "Tom",
#        "tom@test.com"
#    )
#
#    断言：
#    response.status_code == 201
#
#    获取：
#    data = response.json()
#
#    断言：
#    data["name"] == "Tom"
#    data["email"] == "tom@test.com"
#
#
# 不需要：
# - import ApiClient
# - 自己创建 ApiClient
# - 自己创建 UserApi
#
# user_api 由 conftest.py 中的 fixture 提供。
def test_get_user(user_api):
    response=user_api.get_user(1)
    assert response.status_code==200
    data = response.json()
    assert data["id"]==1
def test_create_user(user_api):
    response = user_api.create_user("Tom","tom@test.com")
    assert response.status_code == 201
    data = response.json()
    assert data["name"]=="Tom"
    assert data["email"]=="tom@test.com"
