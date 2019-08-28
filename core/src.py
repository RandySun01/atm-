from lib import common
from interface import user
from interface import bank
from interface import store

"""
@author RansySun
@create 2019-08-18-15:34
"""
"""
'0': '注销',
    '1': '登录',
    '2': '注册',
    '3': '查看余额',
    '4': '转账',
    '5': '还款',
    '6': '取款',
    '7': '查看流水',
    '8': '购物',
    '9': '购物车',
    'q': '退出'
"""
# 判断用户是否注册
user_auth = {'username': None}
username = user_auth['username']

# 日志加载
logger = common.load_my_logging('user')


@common.login_autho
def logout():
    global username
    print("欢迎来到注销功能！\n")
    user = user_auth['username']
    user_auth['username'] = None
    username = None
    logger.info(f'{user}--已经注销')
    print(f'--{user}--已经注销\n')


def login():
    """
    实现登录功能
    """
    print("欢迎来到登录界面！\n")
    count = 0
    global username
    # 三次判断
    while count < 3:
        # 用户信息输入
        login_username, pwd = common.input_usernmae_pwd()
        flag, msc = user.login_interface(login_username, pwd)
        print(msc)

        # 登录成功
        if flag:
            user_auth['username'] = login_username
            username = login_username
            logger.info(f'{login_username}--登录成功')
            break
        count += 1

        # 用户名存在三次输入错误，对用户枷锁
        if count == 3:
            flag, msc = user.locked_interface(login_username)
            logger.info(f'{login_username}--{msc}')
            print(msc)
            break


def register():
    """
    用户注册
    """
    print("欢迎来到注销页面\n")
    count = 0
    while count < 3:
        # 输入用户信息
        reg_username, pwd = common.input_usernmae_pwd()

        # 实现用户注册
        flag, msg = user.register_interface(reg_username, pwd)
        print(msg)
        if flag:
            logger.info(f'{reg_username}--{msg}')
            break

        count += 1
        if count == 3:
            print("三次机会已用完！")


@common.login_autho
def check_extra():
    """
    查看余额
    """
    print("欢迎来到查看余额功能")
    extra = bank.check_extra_interface(username)
    print(f'你的余额为: {extra}\n')
    logger.info(f'{username}--查看余额-{extra}')


@common.login_autho
def tranfer():
    print("欢迎来到转账功能\n")

    from_username = username
    to_username = input("请输入你需要转账的账户>>>: ").strip()

    # 判断用户是否存在
    user_flag = common.is_username(to_username)

    # 进行转账
    if user_flag:
        money = input("请输入你要转账的金额！").strip()
        if money.isdigit():
            money = int(money)

            # 进行转账
            flag, msc = bank.tranfer_interface(from_username, to_username, money)
            print(msc)

            if flag:
                print(f'[{from_username}]向[{to_username}]转了[{money}]\n')
                logger.info(f'{from_username}向{to_username}转了{money}')
        else:
            print("请输入正确的金额！")
            return
    else:
        print("你转账的用户不存在！\n")


@common.login_autho
def repay():
    """
    还款功能
    """
    print("欢迎来到还款界面")
    flag, msc = bank.repay_interface(username)
    print(msc)
    if flag:
        logger.info(f"{username}{msc}")


@common.login_autho
def withdraw():
    """
    取款功能
    :return: none
    """
    print("欢迎来到取款功能\n")

    money = input("请输入取款金额>>: ").strip()

    # 判断用户输入是否数字
    if money.isdigit():
        money = int(money)

        # 实现取款功能
        flag, msc = bank.withdraw_interface(username, money)
        print(msc)

        if flag:
            logger.info(f'{username}{msc}')

    else:
        print("请输入正确的金额！\n")
        return


@common.login_autho
def history():
    """
    查看银行流水信息
    """
    print("欢迎来到银行流水查看功能\n")

    # 实现查看日志功能
    msc = bank.history_interface(username)
    print(msc)
    logger.info(f"{username}查看银行流水日志！")


@common.login_autho
def shopping():
    print("欢迎来到购物车界面\n")
    msg = store.shopping_interface()
    print(msg)
    logger.info(f"{username}{msg}")


@common.login_autho
def shopping_car():
    print("欢迎来到购物车界面\n")
    flag, msg = store.shopping_car_interface(username)
    print(msg)
    if flag:
        logger.info(f"{username}购物成功！-- {msg}")


def run():
    from conf import settings
    FUNC_DIC = {
        '0': logout,
        '1': login,
        '2': register,
        '3': check_extra,
        '4': tranfer,
        '5': repay,
        '6': withdraw,
        '7': history,
        '8': shopping,
        '9': shopping_car,

    }
    while True:
        # 打印功能
        for k, v in settings.FUNC_MSC.items():
            print(f'功能编号{k}---{v}')

        func_choice = input("请输入你要选择的功能编号(输入q退出)>>>: ").strip()

        # 判断是否退出
        if func_choice == 'q':
            break

        if func_choice in FUNC_DIC:
            FUNC_DIC[func_choice]()
        else:
            print("输入错误了， 傻逼！")
            continue
