import os
from db import dbhandler
from conf import settings

"""
@author RansySun
@create 2019-08-18-15:34
"""


def check_extra_interface(username):
    """
    查看余额
    :param username:
    :return:
    """
    # 读取用户信息
    username_dic = dbhandler.read_josn(username)
    return username_dic['extra']


def tranfer_interface(from_username, to_username, moey):
    """
    转账接口
    :param from_username: 要转账的人
    :param to_username: 向谁转账
    :param moey: 转账多少钱
    :return: 成功返回True,否则返回False
    """
    from_username_dic = dbhandler.read_josn(from_username)
    to_username_dic = dbhandler.read_josn(to_username)

    if from_username_dic['extra'] > moey:
        from_username_dic['extra'] -= moey
        to_username_dic['extra'] += moey
        dbhandler.save_json(from_username, from_username_dic)
        dbhandler.save_json(to_username, to_username_dic)
        return True, "转账成功"
    else:
        return False, "账户余额不足\n"


def repay_interface(username):
    """
    还款接口
    :param username: 还款用户
    """
    username_dic = dbhandler.read_josn(username)
    extra = username_dic['extra']
    if extra >= 15000:
        return False, '无需还款！\n'
    else:
        username_dic['extra'] = 15000
        dbhandler.save_json(username, username_dic)
        return True, f'还款{(15000 - extra) * 1.005: .1f}成功\n'


def withdraw_interface(username, money):
    """
    取款接口
    :param username: 取款用户名
    :param money: 取款金额
    :return: 成功True,否则False
    """
    username_dic = dbhandler.read_josn(username)

    # 判读用户金额是否打印取款金额
    if username_dic['extra'] >= money:

        # 修改金额
        username_dic['extra'] -= money
        dbhandler.save_json(username, username_dic)
        return True, f'取款成功，取款金额为{money}\n'
    else:
        return False, f'取款失败\n'


def history_interface(username):
    """
    产看日志接口
    :param username:
    :return: 返回用户日志信息
    """
    s = ""
    # 读取日志路径
    log_path = os.path.join(settings.LOG_PAHT, 'log.log')

    # 读取用户日志信息
    with open(log_path, 'r', encoding='utf8') as fr:
        for log in fr:
            if log.split('[')[-1].startswith(username):
                s += log
    return s
