
import logging
#创建一个日志对象，名字叫 api_test
logger = logging.getLogger("api_test")
#设置最低纪录级别 INFO
logger.setLevel(logging.INFO)
'''
#创建一个输出到终端的处理器
handler = logging.StreamHandler()
#定义日志长什么样
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
'''
#注释代码块优化
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    
    #把格式交给handler
    handler.setFormatter(formatter)
    #把这个终端输出器挂到logger上
    logger.addHandler(handler)

