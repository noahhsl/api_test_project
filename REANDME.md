
# API Test Project

这是一个基于 Python、Requests 和 Pytest 实现的小型接口自动化测试项目。

项目使用 JSONPlaceholder 作为测试接口。

## 技术栈

- Python
- Requests
- Pytest
- pytest-html

## 项目结构

api_test_project/
├── api/
│   ├── user_api.py
│   └── post_api.py
├── common/
│   ├── api_client.py
│   └── logger.py
├── config/
│   └── config.py
├── tests/
│   ├── test_user.py
│   └── test_post.py
├── conftest.py
├── requirements.txt
└── README.md

## 已实现接口

### User

GET /users/1

查询指定用户。

POST /users

创建用户。

### Post

GET /posts/1

查询指定帖子。

GET /posts?userId=1

查询指定用户的所有帖子。

## 安装依赖

进入项目根目录后执行：

python -m pip install -r requirements.txt

## 运行测试

执行：

python -m pytest -v

## 生成 HTML 测试报告

执行：

python -m pytest -v --html=report.html --self-contained-html

执行完成后，项目根目录会生成：

report.html

使用浏览器打开即可查看测试报告。

## 项目设计

common/api_client.py

负责公共 HTTP GET / POST 请求。

api/

负责不同业务接口的封装，例如 UserApi、PostApi。

conftest.py

通过 pytest fixture 创建 ApiClient、UserApi、PostApi 对象，并提供给测试用例使用。

tests/

存放 pytest 测试用例。

config/

存放项目公共配置，例如 BASE_URL。