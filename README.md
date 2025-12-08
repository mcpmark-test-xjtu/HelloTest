# HelloTest

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

一个用于测试 GitHub Actions 自动化发布工作流的示例项目。

## 📋 目录

- [项目说明](#项目说明)
- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [使用方法](#使用方法)
- [项目结构](#项目结构)
- [测试](#测试)
- [文档](#文档)
- [贡献](#贡献)
- [许可证](#许可证)

## 项目说明

HelloTest 是一个专门设计用于 **MCPMark** 测试框架的物料仓库，主要用于验证 GitHub Actions CI/CD 自动化发布工作流的功能。

### 用途

- 🔄 测试 CI/CD 自动化工作流
- 📦 验证自动发布流程
- ✅ 检查版本管理机制
- 🚀 演示 GitHub Actions 集成

## 功能特性

- ✨ **完整的项目结构**: 包含源码、测试、配置、文档
- 🔧 **配置管理**: 集中式配置管理系统
- 📝 **日志系统**: 基于 Python logging 的日志模块
- 🧪 **单元测试**: 完整的测试覆盖
- 🎯 **命令行工具**: 友好的 CLI 接口
- 📚 **详细文档**: 完善的使用和贡献指南
- 🔖 **版本管理**: 支持语义化版本控制

## 快速开始

### 前置要求

- Python 3.7 或更高版本
- Git

### 安装

1. 克隆仓库：
```bash
git clone <repository-url>
cd hellotest
```

2. 安装依赖（可选，当前无外部依赖）：
```bash
pip install -r requirements.txt
```

3. 初始化仓库（如需要）：
```bash
python setup_repo.py
```

## 使用方法

### 运行主程序

```bash
python main.py
```

### 使用命令行工具

查看版本：
```bash
python cli.py --version
```

查看项目信息：
```bash
python cli.py --info
```

查看配置：
```bash
python cli.py --config
```

启用调试模式：
```bash
python cli.py --debug --info
```

## 项目结构

```
hellotest/
├── main.py              # 主程序入口
├── cli.py               # 命令行接口
├── config.py            # 配置管理
├── utils.py             # 工具函数
├── logger.py            # 日志模块
├── __init__.py          # 包初始化
├── test_main.py         # 主程序测试
├── test_utils.py        # 工具测试
├── run_tests.py         # 测试运行器
├── setup_repo.py        # 仓库初始化脚本
├── package.json         # 项目元数据
├── pyproject.toml       # Python 项目配置
├── requirements.txt     # Python 依赖
├── .gitignore           # Git 忽略文件
├── README.md            # 项目说明（本文件）
├── CHANGELOG.md         # 变更日志
├── CONTRIBUTING.md      # 贡献指南
├── LICENSE              # MIT 许可证
├── .github/             # GitHub 配置
│   └── PULL_REQUEST_TEMPLATE.md
└── docs/                # 文档目录
    ├── USAGE.md         # 详细使用指南
    └── MATERIAL_INFO.md # 物料说明文档
```

## 测试

### 运行所有测试

```bash
python run_tests.py
```

### 运行特定测试

```bash
python -m unittest test_main.py
python -m unittest test_utils.py
```

### 测试覆盖

项目包含以下测试：
- ✅ 主程序功能测试
- ✅ 工具函数测试
- ✅ 配置模块测试
- ✅ 导入和集成测试

## 文档

详细文档位于 `docs/` 目录：

- [使用指南](docs/USAGE.md) - 详细的使用说明
- [物料说明](docs/MATERIAL_INFO.md) - 物料仓库说明
- [贡献指南](CONTRIBUTING.md) - 如何参与贡献
- [变更日志](CHANGELOG.md) - 版本变更记录

## CI/CD 集成

本项目设计用于测试 GitHub Actions 自动化工作流。测试流程包括：

1. 创建发布工作流配置
2. 设置版本管理
3. 自动创建 Git Tag
4. 自动生成 GitHub Release

详见 [物料说明文档](docs/MATERIAL_INFO.md)。

## 开发

### 本地开发

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'Add amazing feature'`
4. 推送分支：`git push origin feature/amazing-feature`
5. 创建 Pull Request

### 代码规范

- 遵循 PEP 8 Python 代码规范
- 添加适当的文档字符串
- 编写单元测试
- 更新相关文档

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细信息。

### 贡献者

感谢所有为本项目做出贡献的开发者！

## 版本历史

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细的版本变更历史。

当前版本：**0.9.0**

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 相关链接

- [MCPMark 测试框架](https://github.com/yourusername/mcpmark)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [语义化版本规范](https://semver.org/)

## 联系方式

如有问题或建议，请提交 Issue。

---

**注意**: 本项目是 MCPMark 测试框架的测试物料，专门用于验证 CI/CD 自动化工作流。

