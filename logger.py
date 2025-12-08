"""
日志管理模块
"""
import logging
import sys
from config import Config


def setup_logger(name: str = "HelloTest") -> logging.Logger:
    """
    设置并返回一个日志记录器
    
    Args:
        name: 日志记录器的名称
        
    Returns:
        配置好的日志记录器
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, Config.LOG_LEVEL))
    
    # 如果已经有处理器，不再添加
    if logger.handlers:
        return logger
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    # 创建格式化器
    formatter = logging.Formatter(Config.LOG_FORMAT)
    console_handler.setFormatter(formatter)
    
    # 添加处理器到日志记录器
    logger.addHandler(console_handler)
    
    return logger


# 创建默认的日志记录器
default_logger = setup_logger()


def log_info(message: str):
    """记录信息级别日志"""
    default_logger.info(message)


def log_warning(message: str):
    """记录警告级别日志"""
    default_logger.warning(message)


def log_error(message: str):
    """记录错误级别日志"""
    default_logger.error(message)


def log_debug(message: str):
    """记录调试级别日志"""
    default_logger.debug(message)

