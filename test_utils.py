"""
工具函数测试模块
"""
import unittest
import os
import json
from utils import get_version, print_info


class TestUtils(unittest.TestCase):
    """工具函数测试类"""
    
    def test_get_version_with_package_json(self):
        """测试从 package.json 获取版本号"""
        # 确保 package.json 存在
        self.assertTrue(os.path.exists('package.json'))
        
        version = get_version()
        self.assertIsNotNone(version)
        self.assertNotEqual(version, 'unknown')
        
        # 验证版本格式 (应该是语义化版本)
        parts = version.split('.')
        self.assertEqual(len(parts), 3, "版本号应该包含三个部分")
    
    def test_get_version_matches_package_json(self):
        """测试获取的版本号与 package.json 一致"""
        with open('package.json', 'r') as f:
            data = json.load(f)
            expected_version = data.get('version')
        
        actual_version = get_version()
        self.assertEqual(actual_version, expected_version)
    
    def test_print_info(self):
        """测试打印项目信息"""
        # 这个测试只是确保函数不会抛出异常
        try:
            print_info()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"print_info() 抛出异常: {e}")


class TestConfig(unittest.TestCase):
    """配置测试类"""
    
    def test_import_config(self):
        """测试配置模块导入"""
        try:
            from config import Config, get_config
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"无法导入配置模块: {e}")
    
    def test_config_attributes(self):
        """测试配置类属性"""
        from config import Config
        
        self.assertTrue(hasattr(Config, 'PROJECT_NAME'))
        self.assertTrue(hasattr(Config, 'DEBUG'))
        self.assertTrue(hasattr(Config, 'LOG_LEVEL'))
        self.assertTrue(hasattr(Config, 'MAX_RETRY'))
        self.assertTrue(hasattr(Config, 'TIMEOUT'))
    
    def test_get_config_function(self):
        """测试获取配置函数"""
        from config import get_config
        
        config = get_config()
        self.assertIsNotNone(config)
        self.assertEqual(config.PROJECT_NAME, "HelloTest")


if __name__ == '__main__':
    unittest.main()

