# api/user_api.py
#
# 目标：
# 封装 JSONPlaceholder 的用户接口。
#
# 注意：
# ApiClient 负责真正发送 GET / POST 请求。
# UserApi 只负责用户业务接口的 path 和 data。
#
# 要求：
#
# 1. 定义 UserApi 类
#
# 2. __init__(client)
#    - client 是 ApiClient 对象
#    - 保存：
#      self.client = client
#
# 3. get_user(user_id)
#    - 请求路径：
#      /users/{user_id}
#
#    例如：
#      user_id = 1
#      path = "/users/1"
#
#    - 调用：
#      self.client.get(path)
#
#    - 返回 response
#
# 4. create_user(name, email)
#    - 请求路径：
#      /users
#
#    - 请求体：
#      {
#          "name": name,
#          "email": email
#      }
#
#    - 调用：
#      self.client.post(path, json=data)
#
#    - 返回 response
#
# 请独立完成 UserApi 类。

class UserApi:
    #如果一个类需要长期使用另一个类的对象，就可以在 __init__ 里接收这个对象，
    #再保存成 self.xxx,下面这个client就是一个对象，我需要用到ApiClient这个类的对象方便调get()和post() 
    def __init__(self,client):
        self.client=client
    def get_user(self,user_id):
        path = f'/users/{user_id}'
        response = self.client.get(path)
        return response

    def create_user(self,name,email):
        path = '/users'
        data = {"name":name,"email":email}
        response=self.client.post(path,json=data)
        return response

