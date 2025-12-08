#!/usr/bin/env python3
"""
测试运行脚本
运行所有单元测试并生成报告
"""
import unittest
import sys
import os


def run_all_tests():
    """运行所有测试"""
    print("=" * 60)
    print("开始运行 HelloTest 测试套件")
    print("=" * 60)
    print()
    
    # 发现并加载所有测试
    loader = unittest.TestLoader()
    start_dir = '.'
    pattern = 'test_*.py'
    
    suite = loader.discover(start_dir, pattern=pattern)
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 打印总结
    print()
    print("=" * 60)
    print("测试总结")
    print("=" * 60)
    print(f"运行测试数: {result.testsRun}")
    print(f"成功: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"失败: {len(result.failures)}")
    print(f"错误: {len(result.errors)}")
    print(f"跳过: {len(result.skipped)}")
    
    # 返回适当的退出码
    if result.wasSuccessful():
        print("\n✅ 所有测试通过!")
        return 0
    else:
        print("\n❌ 部分测试未通过")
        return 1


def main():
    """主函数"""
    # 确保在脚本所在目录运行
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    exit_code = run_all_tests()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

