#!/usr/bin/env python3
"""
GitHub 部署脚本
快速将 HelloTest 物料仓库部署到 GitHub
"""
import subprocess
import sys
import os


def run_command(cmd, check=True, capture_output=True):
    """运行命令并返回结果"""
    print(f"执行: {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=capture_output,
        text=True,
        check=False
    )
    
    if result.returncode != 0 and check:
        print(f"❌ 命令执行失败: {result.stderr}")
        return False
    
    if result.stdout and capture_output:
        print(result.stdout)
    
    return True


def check_git_repo():
    """检查是否为 git 仓库"""
    return os.path.exists('.git')


def check_remote_exists(remote_name='origin'):
    """检查远程仓库是否存在"""
    result = subprocess.run(
        f"git remote get-url {remote_name}",
        shell=True,
        capture_output=True,
        text=True,
        check=False
    )
    return result.returncode == 0


def main():
    """主函数"""
    print("=" * 70)
    print("HelloTest GitHub 部署脚本")
    print("=" * 70)
    print()
    
    # 切换到脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # 检查是否为 git 仓库
    if not check_git_repo():
        print("⚠️  当前目录不是 git 仓库")
        response = input("是否初始化为 git 仓库? (y/N): ")
        if response.lower() == 'y':
            if not run_command("python setup_repo.py"):
                return 1
        else:
            print("❌ 需要先初始化 git 仓库")
            return 1
    
    print("✅ Git 仓库已就绪")
    
    # 获取 GitHub 仓库 URL
    if check_remote_exists('origin'):
        result = subprocess.run(
            "git remote get-url origin",
            shell=True,
            capture_output=True,
            text=True
        )
        existing_url = result.stdout.strip()
        print(f"\n当前 origin 远程仓库: {existing_url}")
        response = input("是否使用现有的远程仓库? (Y/n): ")
        
        if response.lower() == 'n':
            new_url = input("请输入新的 GitHub 仓库 URL: ").strip()
            if new_url:
                run_command(f"git remote set-url origin {new_url}")
                repo_url = new_url
            else:
                repo_url = existing_url
        else:
            repo_url = existing_url
    else:
        print("\n请输入 GitHub 仓库 URL（格式: https://github.com/username/repo.git）")
        repo_url = input("GitHub URL: ").strip()
        
        if not repo_url:
            print("❌ 未提供仓库 URL")
            return 1
        
        if not run_command(f"git remote add origin {repo_url}"):
            return 1
    
    print(f"\n📦 准备推送到: {repo_url}")
    
    # 确认推送
    print("\n将要执行以下操作:")
    print("  1. 推送 main 分支到 GitHub")
    print("  2. 设置 upstream 跟踪")
    
    response = input("\n确认推送? (Y/n): ")
    if response.lower() == 'n':
        print("❌ 用户取消推送")
        return 0
    
    # 推送到 GitHub
    print("\n开始推送...")
    if not run_command("git push -u origin main", check=False, capture_output=False):
        print("\n⚠️  推送失败，可能需要:")
        print("  1. 检查 GitHub 仓库是否已创建")
        print("  2. 确认有推送权限")
        print("  3. 验证 Git 凭据")
        return 1
    
    print("\n" + "=" * 70)
    print("✅ 部署成功!")
    print("=" * 70)
    print(f"\n仓库地址: {repo_url}")
    print("\n下一步:")
    print("  1. 访问 GitHub 仓库检查文件")
    print("  2. 配置必要的环境变量 (.mcp_env)")
    print("  3. 运行测试验证工作流")
    print(f"\n运行测试:")
    print(f"  cd /path/to/tasks/githubs/cicd_workflow_automation/q1")
    print(f"  python verify.py")
    
    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        sys.exit(1)

