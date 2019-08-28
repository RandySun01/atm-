from db import dbhandler

"""
@author RansySun
@create 2019-08-18-17:41
"""


def read_goods_interface():
    """
    读取商品信息
    :return: 返回商品信息
    """
    goods_dic = dbhandler.read_goods()
    return goods_dic


def shopping_interface():
    user_shopping_car = dict()
    money = [0]
    goods_dic = read_goods_interface()
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

                # 计算商品价钱
                price = goods_price * count_choice
                money[0] += price
                print(f"您购买的商品为{goods_choice} 金额为{price}")
            else:
                print("商品数量超出范围")
                continue
        else:
            print("傻逼，商品输入错了")
            continue
    return f"您购买的商品为: {user_shopping_car} 共消费: {money[0]}"

if __name__ == '__main__':
    data = shopping_interface()
    print(data)
    # from lib import common
    # data = common.is_username('randysun')
    # print(data)
