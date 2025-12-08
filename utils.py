"""
实用工具函数模块
"""


def get_version():
    """获取项目版本号"""
    import json
    try:
        with open('package.json', 'r') as f:
            data = json.load(f)
            return data.get('version', 'unknown')
    except FileNotFoundError:
        return 'unknown'


def print_info():
    """打印项目信息"""
    version = get_version()
    print(f"HelloTest v{version}")
    print("=" * 40)

