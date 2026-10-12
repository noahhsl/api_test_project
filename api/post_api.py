# api/post_api.py
#
# 项目需求：
#
# 现在要新增“帖子接口模块” PostApi。
#
# PostApi 不直接使用 requests，
# 而是使用外部传进来的 ApiClient 对象发送请求。
#
#
# 功能 1：根据帖子 ID 查询帖子
#
# 方法：
# get_post(post_id)
#
# 示例：
# get_post(1)
#
# 实际请求：
# GET /posts/1
#
# 要求：
# - 根据 post_id 生成请求路径
# - 使用 self.client.get(path)
# - 返回 response
#
#
# 功能 2：查询某个用户的所有帖子
#
# 方法：
# get_posts_by_user(user_id)
#
# 示例：
# get_posts_by_user(1)
#
# 实际请求：
# GET /posts?userId=1
#
# 要求：
# - path 使用 "/posts"
# - 查询参数使用 params：
#
#   {
#       "userId": user_id
#   }
#
# - 使用：
#   self.client.get(path, params=params)
#
# - 返回 response
#
#
# 类初始化：
#
# __init__(client)
#
# 外面会传入一个 ApiClient 对象。
#
# 保存：
# self.client = client
#
#
# 请独立完成 PostApi 类。
class PostApi():
    def __init__(self,client):
        self.client=client
    def get_post(self,post_id):
        path = f'/posts/{post_id}'
        response = self.client.get(path)
        return response
    def get_posts_by_user(self,user_id):
        path = "/posts"
        params = {"userId":user_id}
        response = self.client.get(path,params=params)
        return response
