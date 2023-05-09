import logging

f = open('log.txt', 'a', encoding='utf-8')  # 创建文件保存日志信息
# 调整日志输出的最低等级和日志格式
# 格式：2023-05-09 10:17:37,066 - 10-logging日志信息.py[line:9] - root - DEBUG: 这是一条debug级别日志信息！
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s: %(message)s',
                    # 输出日志到文件中
                    stream=f
                    )

# 输出日志信息到终端，默认不会输出warning级别以下的日志信息
logging.debug('这是一条debug级别日志信息！')
logging.info('这是一条info级别日志信息！！')
logging.warning('这是一条warning级别日志信息！！！')
logging.error('这是一条error级别日志信息！！！！')
logging.critical('这是一条critical级别日志信息！！！！！！')
