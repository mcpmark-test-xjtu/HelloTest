#!/usr/bin/env python3
"""
物料仓库初始化脚本
用于初始化 hellotest 仓库作为 CI/CD 测试的物料
"""
import subprocess
import sys
import os


def run_command(cmd, check=True):
    """运行命令并返回结果"""
    print(f"执行命令: {cmd}")
    result = subprocess.run(
        cmd, 
        shell=True, 
        capture_output=True, 
        text=True,
        check=False
    )
    
    if result.returncode != 0 and check:
        print(f"错误: {result.stderr}")
        return False
    
    if result.stdout:
        print(result.stdout)
    
    return True


def init_repo():
    """初始化 git 仓库"""
    print("=" * 60)
    print("开始初始化 HelloTest 物料仓库")
    print("=" * 60)
    
    # 检查是否已经是 git 仓库
    if os.path.exists('.git'):
        print("⚠️  检测到已存在的 .git 目录")
        response = input("是否重新初始化? (y/N): ")
        if response.lower() != 'y':
            print("取消初始化")
            return False
        
        # 删除现有的 .git
        run_command("rm -rf .git", check=False)
    
    # 1. 初始化 git 仓库
    print("\n步骤 1: 初始化 git 仓库...")
    if not run_command("git init"):
        return False
    
    # 2. 配置 git 用户信息（如果需要）
    print("\n步骤 2: 配置 git 用户信息...")
    run_command('git config user.name "HelloTest Bot"', check=False)
    run_command('git config user.email "bot@hellotest.local"', check=False)
    
    # 3. 添加所有文件
    print("\n步骤 3: 添加文件到暂存区...")
    if not run_command("git add ."):
        return False
    
    # 4. 创建初始提交
    print("\n步骤 4: 创建初始提交...")
    commit_message = "Initial commit: Setup HelloTest project structure"
    if not run_command(f'git commit -m "{commit_message}"'):
        return False
    
    # 5. 重命名默认分支为 main（如果需要）
    print("\n步骤 5: 确保主分支名为 main...")
    run_command("git branch -M main", check=False)
    
    print("\n" + "=" * 60)
    print("✅ 仓库初始化完成!")
    print("=" * 60)
    print("\n项目信息:")
    print(f"  - 项目名称: HelloTest")
    print(f"  - 初始版本: 0.9.0")
    print(f"  - 主分支: main")
    print(f"  - 文件数量: {len(os.listdir('.')) - 1}")  # -1 to exclude .git
    
    print("\n下一步:")
    print("  1. 将此仓库推送到 GitHub")
    print("  2. 运行 CI/CD 自动化测试")
    print(f"  3. 验证脚本将检查自动发布工作流")
    
    return True


def show_status():
    """显示仓库状态"""
    print("\n当前仓库状态:")
    run_command("git status", check=False)
    print("\n提交历史:")
    run_command("git log --oneline", check=False)


if __name__ == "__main__":
    # 切换到脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    success = init_repo()
    
    if success:
        show_status()
        sys.exit(0)
    else:
        print("\n❌ 初始化失败")
        sys.exit(1)

