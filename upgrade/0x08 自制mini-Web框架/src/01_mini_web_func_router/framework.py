"""miniweb框架，负责处理动态资源请求"""
import time

# 获取首页数据
def index():
    # 响应状态
    status = "200 OK"
    # 响应头
    response_header = [("Server", "FoxServ2.0")]
    # 处理后的数据
    data = time.ctime()

    return status, response_header, data

def center():
    pass

# 没有找到动态资源
def not_found():
    # 响应状态
    status = "404 Not Found"
    # 响应头
    response_header = [("Server", "FoxServ2.0")]
    # 处理后的数据
    data = "not found"

    return status, response_header, data


route_list = [
    ("/index.py", index),
    ("/center.py", center)
]

# 处理动态资源请求
def handle_request(env):
    # 获取动态请求资源路径
    request_path = env["request_path"]
    print("接收到的动态资源请求:", request_path)

    # 遍历路由列表、绑定函数
    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        # 没有找到动态资源
        result = not_found()
        return result
