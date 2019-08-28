import os

"""
@author RansySun
@create 2019-08-18-15:34
"""
###################
#                 #
#  打印函数功能    #
#                 #
###################
FUNC_MSC = {
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
}



#############################
#  db用户信息保存路径(.json) #
#  log日志文件路径(log.log)  #
#  商品文件路径(excel)       #
##############################

# 当前文件所在的目录
PATH = os.path.dirname(os.path.abspath(__file__))
# 用户信息要存取的目录
DB_PATH = os.path.join(os.path.dirname(PATH), 'db')
# log日志要保存的目录
LOG_PAHT = os.path.join(os.path.dirname(PATH), 'log')
# 商品要保存的路径
EXCEL_PATH = os.path.join(os.path.dirname(PATH), 'db', 'goods_info.xlsx')
# 商品要保存字典形式（json）
GOODS_PATH = os.path.join(os.path.dirname(PATH), 'db', 'goods.json')

################
#               #
# 日志文件配置
#               #
################

import logging.config

# 定义三种日志输出格式 开始
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getLogger()指定的名字；lineno为调用日志输出函数的语句所在的代码行
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s\n'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
# 定义日志输出格式 结束

# logfile_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # log文件的目录，需要自定义文件路径 # atm
# logfile_dir = os.path.join(LOG_PAHT, 'log')

logfile_name = 'log.log'  # log文件名，需要自定义路径名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(LOG_PAHT):
    os.mkdir(LOG_PAHT)

# log文件的全路径
logfile_path = os.path.join(LOG_PAHT, logfile_name)
# 定义日志路径 结束

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},  # filter可以不定义
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M  (*****)
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置。如果''设置为固定值logger1，则下次导入必须设置成logging.getLogger('logger1')
        '': {
            # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}
















# def load_my_logging_cfg():
#     logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
#     logger = logging.getLogger(__name__)  # 生成一个log实例
#     logger.info('It works!')  # 记录该文件的运行状态
#
#     return logger


if __name__ == '__main__':
    print(PATH)
    print(DB_PATH)