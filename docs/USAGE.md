# HelloTest 使用指南

## 目录
- [快速开始](#快速开始)
- [命令行工具](#命令行工具)
- [运行测试](#运行测试)
- [项目结构](#项目结构)
- [配置说明](#配置说明)

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行项目

```bash
python main.py
```

## 命令行工具

项目提供了一个命令行接口工具 `cli.py`：

### 查看版本
```bash
python cli.py --version
```

### 查看项目信息
```bash
python cli.py --info
```

### 查看配置
```bash
python cli.py --config
```

### 调试模式
```bash
python cli.py --debug --info
```

## 运行测试

### 运行所有测试
```bash
python run_tests.py
```

### 运行特定测试文件
```bash
python -m unittest test_main.py
python -m unittest test_utils.py
```

### 运行单个测试用例
```bash
python -m unittest test_main.TestMain.test_main_output
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
├── README.md            # 项目说明
├── CHANGELOG.md         # 变更日志
├── CONTRIBUTING.md      # 贡献指南
├── LICENSE              # 许可证
├── .gitignore           # Git 忽略文件
├── .github/             # GitHub 配置
│   └── PULL_REQUEST_TEMPLATE.md
└── docs/                # 文档目录
    └── USAGE.md         # 使用指南
```

## 配置说明

### config.py

项目配置在 `config.py` 中定义：

```python
class Config:
    PROJECT_NAME = "HelloTest"
    DEBUG = True
    LOG_LEVEL = "INFO"
    MAX_RETRY = 3
    TIMEOUT = 30
```

### 自定义配置

你可以通过修改 `config.py` 或创建新的配置类来自定义项目配置。

## 版本管理

项目版本号在 `package.json` 中维护：

```json
{
  "name": "hellotest",
  "version": "0.9.0",
  ...
}
```

## 日志

项目使用 Python 标准库的 `logging` 模块。日志配置可以在 `config.py` 中调整。

### 日志级别

- DEBUG: 详细的调试信息
- INFO: 一般信息
- WARNING: 警告信息
- ERROR: 错误信息
- CRITICAL: 严重错误

## 开发工作流

1. **克隆仓库**
   ```bash
   git clone <repository-url>
   cd hellotest
   ```

2. **创建虚拟环境（推荐）**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate     # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **运行测试**
   ```bash
   python run_tests.py
   ```

5. **开发新功能**
   ```bash
   git checkout -b feature/new-feature
   # ... 进行开发 ...
   python run_tests.py  # 确保测试通过
   git commit -m "Add new feature"
   ```

## CI/CD 集成

本项目设计用于测试 GitHub Actions 自动化工作流。相关工作流配置将在 `.github/workflows/` 目录中。

### 自动化发布工作流

当推送到 main 分支且 `package.json` 中的版本号发生变化时，会自动创建新的 Git Tag 和 GitHub Release。

## 故障排除

### 导入错误

如果遇到导入错误，确保你在项目根目录运行命令：

```bash
cd /path/to/hellotest
python main.py
```

### 测试失败

如果测试失败，检查：
1. 所有依赖是否正确安装
2. Python 版本是否 >= 3.7
3. 是否在项目根目录运行测试

## 获取帮助

- 查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解贡献指南
- 查看 [README.md](../README.md) 了解项目概述
- 提交 Issue 报告问题或建议

