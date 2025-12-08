#!/usr/bin/env python3
"""
命令行接口模块
提供友好的命令行交互界面
"""
import argparse
import sys
from utils import get_version, print_info
from config import get_config
from logger import setup_logger


def create_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器"""
    parser = argparse.ArgumentParser(
        description="HelloTest - CI/CD 自动化测试项目",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python cli.py --version          显示版本信息
  python cli.py --info             显示项目信息
  python cli.py --config           显示配置信息
        """
    )
    
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='显示版本号'
    )
    
    parser.add_argument(
        '-i', '--info',
        action='store_true',
        help='显示项目信息'
    )
    
    parser.add_argument(
        '-c', '--config',
        action='store_true',
        help='显示配置信息'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='启用调试模式'
    )
    
    return parser


def display_config():
    """显示配置信息"""
    config = get_config()
    print("\n配置信息:")
    print(f"  项目名称: {config.PROJECT_NAME}")
    print(f"  调试模式: {config.DEBUG}")
    print(f"  日志级别: {config.LOG_LEVEL}")
    print(f"  最大重试: {config.MAX_RETRY}")
    print(f"  超时时间: {config.TIMEOUT}s")


def main():
    """主函数"""
    parser = create_parser()
    args = parser.parse_args()
    
    # 如果没有提供任何参数，显示帮助
    if len(sys.argv) == 1:
        parser.print_help()
        return 0
    
    # 设置日志
    logger = setup_logger()
    
    if args.debug:
        logger.info("调试模式已启用")
    
    # 处理命令
    if args.version:
        version = get_version()
        print(f"HelloTest v{version}")
    
    if args.info:
        print_info()
        print("这是一个用于测试 CI/CD 自动化工作流的示例项目。")
    
    if args.config:
        display_config()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

