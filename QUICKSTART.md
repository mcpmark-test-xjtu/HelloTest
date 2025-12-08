# HelloTest 快速启动指南

## 🚀 3 步快速开始

### 第 1 步：初始化 Git 仓库

```bash
cd /Users/edy/PycharmProjects/pjs/hellotest
python setup_repo.py
```

这将：
- ✅ 初始化 git 仓库
- ✅ 添加所有文件
- ✅ 创建初始提交
- ✅ 设置 main 分支

### 第 2 步：推送到 GitHub

**选项 A：使用自动化脚本（推荐）**

```bash
python deploy_to_github.py
```

脚本会引导你完成：
1. 输入 GitHub 仓库 URL
2. 确认推送
3. 自动完成部署

**选项 B：手动推送**

```bash
# 在 GitHub 上创建新仓库后
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 第 3 步：运行测试验证

```bash
cd /Users/edy/PycharmProjects/pjs/tasks/githubs/cicd_workflow_automation/q1
python verify.py
```

## 📋 前提条件

### 必需
- ✅ Python 3.7+ 已安装
- ✅ Git 已安装和配置
- ✅ 在 GitHub 上创建了空仓库

### 环境变量配置

在项目根目录创建 `.mcp_env` 文件：

```bash
MCP_GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxx
GITHUB_EVAL_ORG=your-github-username-or-org
```

**获取 GitHub Token：**
1. 访问 https://github.com/settings/tokens
2. 生成新的 Personal Access Token
3. 选择权限：`repo`, `workflow`, `write:packages`
4. 复制 token 到 `.mcp_env` 文件

## 🧪 本地测试（可选）

在推送到 GitHub 之前，可以先在本地测试：

```bash
# 运行主程序
python main.py

# 使用命令行工具
python cli.py --version
python cli.py --info
python cli.py --config

# 运行测试套件
python run_tests.py

# 或运行单个测试
python -m unittest test_main.py
python -m unittest test_utils.py
```

## 📝 测试流程说明

### 自动化测试会做什么？

根据 `instruction.md` 的要求，测试流程包括：

1. **创建分支**
   - 分支名：`ci/add-release-workflow`

2. **添加文件**
   - `.github/workflows/release.yml` - 自动发布工作流
   - `package.json` - 版本信息（初始为 1.0.0）

3. **创建 PR**
   - 标题包含 "release workflow"
   - 包含 Summary, Changes, Testing 三个章节

4. **更新版本**
   - 将 package.json 版本从 1.0.0 更新到 1.0.1
   - 创建第二个提交

5. **合并 PR**
   - 合并到 main 分支

6. **自动发布**
   - 工作流自动触发
   - 创建 Git Tag: `v1.0.1`
   - 创建 GitHub Release: `v1.0.1`

### 验证点

`verify.py` 会检查：

- ✅ 分支是否创建
- ✅ 工作流文件是否正确
- ✅ PR 格式是否符合要求
- ✅ 提交数量是否为 2
- ✅ 版本号是否正确更新
- ✅ PR 是否已合并
- ✅ Release 是否自动创建
- ✅ Tag 是否正确

## 🔧 常见问题

### Q1: 推送失败，提示权限不足？

**A**: 确保你有仓库的写权限：
- 检查是否是仓库 owner 或 collaborator
- 验证 GitHub Token 权限
- 确认仓库 URL 正确

### Q2: setup_repo.py 报错？

**A**: 确保：
- 当前在 hellotest 目录
- Python 版本 >= 3.7
- Git 已安装：`git --version`

### Q3: 验证脚本找不到 PR？

**A**: 检查：
- PR 标题是否包含 "release workflow"
- 分支名是否为 `ci/add-release-workflow`
- 环境变量是否正确配置

### Q4: 工作流没有触发？

**A**: 确认：
- 工作流文件路径：`.github/workflows/release.yml`
- 触发条件：push 到 main 分支
- GitHub Actions 是否启用
- Token 权限是否足够

## 📚 更多资源

- **详细文档**: 查看 `docs/USAGE.md`
- **物料说明**: 查看 `docs/MATERIAL_INFO.md`
- **项目总结**: 查看 `PROJECT_SUMMARY.md`
- **贡献指南**: 查看 `CONTRIBUTING.md`

## 💡 提示

1. **首次使用**: 建议先阅读 `PROJECT_SUMMARY.md` 了解整体结构
2. **调试模式**: 使用 `--debug` 参数查看详细日志
3. **测试先行**: 推送前先运行本地测试确保一切正常
4. **备份重要数据**: 虽然是测试项目，但建议保存重要的配置信息

## 🎯 快速检查清单

推送到 GitHub 前的检查：

- [ ] Git 仓库已初始化（运行 `setup_repo.py`）
- [ ] 在 GitHub 创建了空仓库
- [ ] 配置了 `.mcp_env` 文件
- [ ] GitHub Token 权限正确
- [ ] 本地测试通过（可选）
- [ ] 了解测试流程和验证点

## 🆘 获取帮助

遇到问题？

1. 查看错误信息和日志
2. 阅读相关文档
3. 检查配置文件
4. 提交 Issue 描述问题

---

**准备好了？开始第 1 步吧！** 🚀

```bash
python setup_repo.py
```

