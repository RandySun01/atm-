from db import dbhandler

"""
@author RansySun
@create 2019-08-18-15:35
"""


def read_goods_interface():
    """
    读取商品信息
    :return: 返回商品信息
    """
    goods_dic = dbhandler.read_goods()
    return goods_dic


# 保存购物车和金额
user_shopping_car = dict()
money = [0]
goods_dic = read_goods_interface()


def shopping_interface():
    """
    购物接口
    :return:用户购物商品信息
    """

    # 打印商品信息
    for k, v in goods_dic.items():
        print(f"商品名称：{k: <16} 商品数量：{goods_dic[k]['amount']: ^6} 商品价格；{goods_dic[k]['price']: ^4}")

    while True:

        goods_choice = input("请输入商品名称(输入q退出)>>>：").strip()
        if goods_choice == 'q':
            break
        # 判断商品是否存在
        if goods_choice in goods_dic:

            # 用户输入购买商品数量
            count_choice = input("请输入购买商品的数量(输入q退出)>>: ").strip()
            if count_choice == 'q':
                break
            count_choice = int(count_choice)

            # 判断商品数量
            if goods_dic[goods_choice]['amount'] >= count_choice:
                goods_price = goods_dic[goods_choice]['price']  # 获取商品价格

                # 判断商品是否在购物中
                if goods_choice in user_shopping_car:
                    user_shopping_car[goods_choice] += 1
                else:
                    user_shopping_car[goods_choice] = 1

                # 减去商品数量
                goods_dic[goods_choice]['amount'] -= count_choice
                # 计算商品价钱
                price = goods_price * count_choice
                money[0] += price
                print(f"您购买的商品为{goods_choice} 金额为{price}\n")
            else:
                print("商品数量超出范围")
                continue
        else:
            print("傻逼，商品输入错了")
            continue

    return f"您购买的商品为{user_shopping_car} 共消费{money[0]}\n"


def shopping_car_interface(username):
    """
    购物车接口
    :param username: 用户名
    :return:
    """
    username_dic = dbhandler.read_josn(username)

    choice = input("购买商品输入(Y/y),取消购买（N/n>>:").strip().lower()
    if choice == 'y':

        # 判断金额是否大于
        if username_dic['extra'] > money[0]:
            username_dic['extra'] -= money[0]

            # 保存用户信息和商品信息
            dbhandler.save_json(username, username_dic)
            dbhandler.save_goods(goods_dic)

            money[0] = 0
            user_shopping_car.clear()
            return True, '购物成功，正在发货，请耐心等待！！'
        else:
            money[0] = 0
            user_shopping_car.clear()
            return False, '余额不足'
    elif choice == 'n':
        money[0] = 0
        user_shopping_car.clear()
        return False, "购物车已清空！"
