import os
import json
from conf import settings

"""
@author RansySun
@create 2019-08-18-15:34
"""


def save_json(username: str, content: dict):
    """
    保存用户信息，以用户名，为文件名
    :param username: 用户名
    :param content: 用户信息字典
    """
    # 读取路径
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')

    # 保存信息
    with open(user_path, 'w', encoding='utf-8') as fw:
        json.dump(content, fw)


def read_josn(username: dict):
    """
    读取用户信息json
    :param username: 用户名
    :return: 返回用户信息
    """
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')

    # 读取用户信息
    with open(user_path, 'r', encoding='utf8') as fr:
        user_data = json.load(fr)

    return user_data


def save_goods(contend: dict):
    """
    保存商品信息
    :param contend: 修改字典的参数
    """
    # 写入字典信息
    with open(settings.GOODS_PATH, 'w', encoding='utf8') as fw:
        json.dump(contend, fw)


def read_goods():
    """
    读取商品信息
    :return: 返回商品信息
    """
    # 读取商品信息
    with open(settings.GOODS_PATH, 'r', encoding='utf-8') as fr:
        goods = json.load(fr)

    return goods


if __name__ == '__main__':
    save_json('randyusn', {'a': 1})
    data = read_josn('randyusn')
    print(data)

    goods = read_goods()
    print(goods)
