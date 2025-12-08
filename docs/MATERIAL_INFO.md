# HelloTest 物料说明文档

## 物料概述

**HelloTest** 是一个专门设计用于测试 GitHub Actions CI/CD 自动化发布工作流的物料仓库。

## 物料用途

此物料用于 **MCPMark** 测试框架中的 GitHub 相关测试任务，具体测试场景为：

- **测试类型**: CI/CD 工作流自动化
- **测试重点**: 自动化发布流程
- **验证内容**: GitHub Actions 工作流配置和执行

## 物料特点

### 1. 完整的项目结构

物料包含一个完整的 Python 项目结构，包括：
- 源代码文件
- 测试文件
- 配置文件
- 文档文件

### 2. 版本管理

- 使用 `package.json` 管理版本号
- 初始版本设置为 `0.9.0`
- 支持语义化版本规范

### 3. 测试友好

- 包含单元测试
- 提供测试运行脚本
- 支持持续集成

### 4. 文档完善

- README.md: 项目说明
- USAGE.md: 使用指南
- CONTRIBUTING.md: 贡献指南
- CHANGELOG.md: 变更日志

## 测试流程

使用此物料的典型测试流程：

1. **初始化仓库**
   ```bash
   cd hellotest
   python setup_repo.py
   ```

2. **推送到 GitHub**
   ```bash
   git remote add origin <github-repo-url>
   git push -u origin main
   ```

3. **执行测试任务**
   - Agent 将根据 instruction.md 执行自动化任务
   - 创建新分支 `ci/add-release-workflow`
   - 添加 GitHub Actions 工作流文件
   - 创建 Pull Request
   - 更新版本号
   - 合并 PR 触发自动发布

4. **验证结果**
   ```bash
   python verify.py
   ```

## 预期测试结果

成功完成测试后，应该：

1. ✅ 创建了 `ci/add-release-workflow` 分支
2. ✅ 添加了 `.github/workflows/release.yml` 工作流文件
3. ✅ 创建了正确格式的 Pull Request
4. ✅ PR 包含两个提交：
   - 第一个提交：添加工作流和初始文件
   - 第二个提交：更新版本号到 1.0.1
5. ✅ PR 合并到 main 分支
6. ✅ 自动创建了 `v1.0.1` 的 Git Tag
7. ✅ 自动创建了 `v1.0.1` 的 GitHub Release

## 验证脚本说明

`verify.py` 脚本会检查以下内容：

### 1. 分支检查
- 验证 `ci/add-release-workflow` 分支是否存在

### 2. 文件检查
- 验证工作流文件是否存在且包含必要的关键字
- 验证 package.json 是否正确更新

### 3. PR 检查
- 验证 PR 是否创建且包含正确的章节（Summary, Changes, Testing）
- 验证 PR 是否已合并（状态为 closed）

### 4. 提交检查
- 验证 PR 包含至少 2 个提交
- 检查提交信息是否合理

### 5. Release 检查
- 验证是否创建了正确版本的 Release
- 验证 Tag 名称是否为 `v1.0.1`

### 6. 版本检查
- 验证 main 分支上的 package.json 版本是否为 `1.0.1`

## 物料文件清单

### 核心文件
- `main.py` - 主程序入口
- `cli.py` - 命令行接口
- `config.py` - 配置管理
- `utils.py` - 工具函数
- `logger.py` - 日志模块
- `__init__.py` - 包初始化

### 测试文件
- `test_main.py` - 主程序测试
- `test_utils.py` - 工具函数测试
- `run_tests.py` - 测试运行器

### 配置文件
- `package.json` - 项目元数据（版本: 0.9.0）
- `pyproject.toml` - Python 项目配置
- `requirements.txt` - Python 依赖
- `.gitignore` - Git 忽略规则

### 文档文件
- `README.md` - 项目说明
- `USAGE.md` - 使用指南
- `CONTRIBUTING.md` - 贡献指南
- `CHANGELOG.md` - 变更日志
- `LICENSE` - MIT 许可证

### 辅助脚本
- `setup_repo.py` - 仓库初始化脚本

### GitHub 模板
- `.github/PULL_REQUEST_TEMPLATE.md` - PR 模板

## 环境要求

- Python >= 3.7
- Git
- GitHub Token (用于 API 访问)

## 相关配置

测试时需要设置以下环境变量：

```bash
# .mcp_env 文件
MCP_GITHUB_TOKEN=<your-github-token>
GITHUB_EVAL_ORG=<your-github-org>
```

## 注意事项

1. **版本号**: 初始版本设置为 0.9.0，测试会将其更新到 1.0.1
2. **分支名**: 固定使用 `ci/add-release-workflow`
3. **PR 关键字**: 验证脚本会搜索包含 "release workflow" 的 PR
4. **工作流名称**: 应为 "Automated Release"

## 故障排除

### 问题: 验证脚本找不到 PR
- 检查 PR 标题是否包含 "release workflow"
- 检查分支名是否为 `ci/add-release-workflow`

### 问题: Release 未自动创建
- 检查工作流文件配置是否正确
- 检查是否有权限创建 Release
- 查看 GitHub Actions 运行日志

### 问题: 版本号不匹配
- 确保 package.json 已正确更新到 1.0.1
- 确保更改已合并到 main 分支

## 维护建议

1. 定期更新依赖包
2. 保持文档同步更新
3. 添加更多测试用例
4. 优化工作流配置

## 许可证

MIT License - 详见 LICENSE 文件

