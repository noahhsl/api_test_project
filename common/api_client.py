# common/api_client.py
#
# 要求：
#
# 1. 导入 requests
#
# 2. 定义 ApiClient 类
#
# 3. __init__(base_url)
#    保存：
#    self.base_url = base_url
#
# 4. get(path, params=None)
#    请求完整地址：
#    self.base_url + path
#
#    使用：
#    requests.get(
#        url,
#        params=params,
#        timeout=10
#    )
#
#    返回 response
#
# 5. post(path, json=None)
#    请求完整地址：
#    self.base_url + path
#
#    使用：
#    requests.post(
#        url,
#        json=json,
#        timeout=10
#    )
#
#    返回 response
#
# 请独立写完整文件代码。

import requests
from common.logger import logger
class ApiClient:
    def __init__(self,base_url):
        self.base_url=base_url
    def get(self,path,params=None):
        url = f'{self.base_url}{path}'
        logger.info(f'GET {url}')
        response = requests.get(url,params=params,timeout=10)
        logger.info(f'RESPONSE {response.status_code}')
        return response
    def post(self,path,json=None):
        url=f'{self.base_url}{path}'
        logger.info(f"POST {url}")
        response = requests.post(url,json=json,timeout=10)
        logger.info(f"RESPONSE {response.status_code}")
        return response
    