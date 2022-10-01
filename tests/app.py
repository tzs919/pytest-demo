import requests

DEFAULT_CONFIG = {"user": "user1", "database": "db1"}


def create_connection_string(config=None):
    config = config or DEFAULT_CONFIG
    return f"User Id={config['user']}; Location={config['database']};"


def get_json(url):
    """请求一个接口，返回json对象"""
    r = requests.get(url)
    return r.json()
