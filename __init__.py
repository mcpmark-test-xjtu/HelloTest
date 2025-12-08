"""
HelloTest - CI/CD 自动化测试物料项目

这是一个用于测试 GitHub Actions 自动化发布工作流的示例项目。
"""

__version__ = "0.9.0"
__author__ = "HelloTest Contributors"
__license__ = "MIT"

from .utils import get_version, print_info
from .config import Config, get_config

__all__ = [
    'get_version',
    'print_info', 
    'Config',
    'get_config',
]

