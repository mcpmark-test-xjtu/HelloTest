"""
配置管理模块
"""


class Config:
    """项目配置类"""
    
    # 项目基本信息
    PROJECT_NAME = "HelloTest"
    DEBUG = True
    
    # 日志配置
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # 其他配置
    MAX_RETRY = 3
    TIMEOUT = 30


def get_config():
    """获取配置实例"""
    return Config()

