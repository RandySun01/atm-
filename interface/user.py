from lib import common
from db import dbhandler

"""
@author RansySun
@create 2019-08-18-15:35
"""


def register_interface(username, pwd):
    """
    实现用户注册功能接口
    :param username: 用户名
    :param pwd: 密码
    :return: 返回是否注册成功
    """
    # 判断用户是否存在
    flag = common.is_username(username)

    # 判断用户是否存在，进行逻辑处理
    if flag:
        return False, '用户已经存在！\n'
    else:
        # 保存用户信息
        contend = {'username': username, 'pwd': pwd, 'extra': 15000, 'locked': 0}
        dbhandler.save_json(username, contend)

        return True, '注册成功！\n'


def login_interface(username, pwd):
    """
    实现用户登录接口
    :param username: 用户名
    :param pwd: 密码
    :return: 登录成功返回True, 否则返回Flase
    """
    # 判断用户是否存在
    flag = common.is_username(username)
    if not flag:
        return False, '用户不存在！\n'

    # 读取用户信息
    user_dic = dbhandler.read_josn(username)
    if user_dic['locked']:
        return False, '用户已被锁定, 快去解锁！\n'

    # 判断密码是否相同
    if user_dic['pwd'] == pwd:
        return True, '登录成功！\n'

    return False, '用户名或密码错误!'


def locked_interface(username):
    """
    如果账户存在用户输入错我三次，
    将对用户枷锁
    :param username:
    :return:
    """
    # 判断用户是否存在，存在对用户枷锁
    flag = common.is_username(username)
    if flag:
        user_dic = dbhandler.read_josn(username)
        user_dic['locked'] = 1
        # 保存枷锁信息
        dbhandler.save_json(username, user_dic)
        return True, '账号已被锁定, 请找管理员解锁！\n'
    else:
        return False, '用户不存在!\n'
