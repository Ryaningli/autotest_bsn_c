import logging.handlers


# 自定义日志器类
class GetLogger:

    logger = None

    # 获取logger
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger('Ryan')

            # 设置日志器的默认级别（默认info)
            cls.logger.setLevel(logging.INFO)

            # 获取处理器（控制台）
            sh = logging.StreamHandler()

            # 获取处理器（时间分割，午夜轮换，最多保存30个文件)
            th = logging.handlers.TimedRotatingFileHandler(
                './log/autotest_bsn_c.log', when='MIDNIGHT', interval=1, backupCount=30, encoding='utf-8'
            )

            # 获取格式器
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
            formatter = logging.Formatter(fmt)

            # 将格式器设置到处理器中
            sh.setFormatter(formatter)
            th.setFormatter(formatter)

            # 将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger
