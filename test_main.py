"""
主程序测试模块
"""
import unittest
from io import StringIO
import sys


class TestMain(unittest.TestCase):
    """主程序测试类"""
    
    def test_import(self):
        """测试模块导入"""
        try:
            import main
            self.assertTrue(True)
        except ImportError:
            self.fail("无法导入 main 模块")
    
    def test_main_function_exists(self):
        """测试主函数是否存在"""
        import main
        self.assertTrue(hasattr(main, 'main'))
        self.assertTrue(callable(main.main))
    
    def test_main_output(self):
        """测试主函数输出"""
        import main
        
        # 捕获标准输出
        captured_output = StringIO()
        sys.stdout = captured_output
        
        main.main()
        
        # 恢复标准输出
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Hello", output)


if __name__ == '__main__':
    unittest.main()

