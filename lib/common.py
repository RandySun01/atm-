import os
import hmac
import logging.config
from core import src
from conf import settings
from db import dbhandler

"""
@author RansySun
@create 2019-08-18-15:35
"""


def login_autho(func):
    """
    装饰器，判断用户是否登录
    :param func:  被装饰的函数对象
    :return: 返回函数对象的调用
    """

    def wrapper(*args, **kwargs):
        if not src.user_auth.get('username'):
            src.login()
            res = func(*args, **kwargs)
            return res
        res = func(*args, **kwargs)
        return res

    return wrapper


def load_my_logging(log_usernme):
    """
    生成日志
    :param log_usernme: 当前运行文件运行的模块名称
    :return: 返回日志对象
    """
    # 配置日志字典
    logging.config.dictConfig(settings.LOGGING_DIC)

    # 获取日志对象
    logger = logging.getLogger(log_usernme)

    # 初始化日志
    logger.info("---Logger starts it work")

    return logger


def input_usernmae_pwd():
    """
    输入用户名和密码（加密）
    :return: 返回用户名和密码
    """
    # 输入用户信息
    username = input("请输入用户名>>>: ").strip()
    pwd = input("请输入密码>>>: ").strip()

    # 生成加密,密码
    m = hmac.new("randysun".encode('utf8 '))
    m.update(pwd.encode('utf8'))

    # 得到加密的密码
    pwd = m.hexdigest()

    return username, pwd


def is_username(username):
    """
    通过文件是否存在，判断用户是否存在
    :param username: 用户名
    :return: 存在返回True 否则返回Flase
    """
    # 获取用户信息路径
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')

    # 判断用户是否存在
    if os.path.exists(user_path):
        return True
    else:
        return False


if __name__ == '__main__':
    logger = load_my_logging("randysun")
    logger.info("测试一下")
    print(is_username("randysun"))
