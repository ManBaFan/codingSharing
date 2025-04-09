Python 文件和目录命名规范

⸻
## ✅ 推荐文件命名规范

| 命名类型       | 命名规范           | 示例                     | 说明                             |
|----------------|--------------------|--------------------------|----------------------------------|
| **Python 文件**  | 全小写，单词之间用下划线分隔 | `my_script.py`, `data_loader.py` | 保持简洁，符合 Python 社区风格 |
| **类文件**     | 驼峰式命名（首字母大写） | `MyClass.py`, `DataParser.py`  | 用于包含类定义的文件            |
| **模块文件**    | 全小写，单词之间用下划线分隔 | `my_module.py`, `utils.py`  | 用于包含模块的文件             |
| **配置文件**    | 简洁小写，使用 `.conf` 或 `.yaml` 后缀 | `settings.conf`, `config.yaml` | 配置文件，多为键值对格式         |
| **数据文件**    | 小写，使用 `.csv`, `.json` 等后缀 | `data.csv`, `users.json`    | 存储数据的文件，使用通用格式   |
| **日志文件**    | 小写，使用 `.log` 后缀 | `app.log`, `error.log`    | 存储程序运行日志文件             |

---

## 📁 示例文件结构
⸻
my_project/
├── main.py
├── config_loader.py
├── model_trainer.py
├── utils/
│   ├── __init__.py
│   └── math_utils.py

⸻

🧠 贴士
	1.	避免与标准库同名：比如不要用 email.py, json.py，否则会冲突。
	2.	使用有意义的名称：描述文件职责，例如 fetch_data.py 表示负责抓取数据。
	3.	使用统一风格：团队项目中统一小写+下划线，避免多种风格混用。

⸻
## ✅ 推荐目录命名规范（PEP 8 + 实战经验）

| 目录类型       | 命名规范           | 示例                       | 说明                             |
|----------------|--------------------|----------------------------|----------------------------------|
| **包目录**     | 全小写，尽量无下划线 | `utils/`, `core/`, `models/`  | 保持简洁，与 Python 包名保持一致 |
| **模块分组目录** | 小写 + 下划线       | `data_loader/`, `user_api/` | 用于分类文件                     |
| **测试目录**   | 一般叫 `tests/`     | `tests/`, `test_utils/`    | 存放单元测试文件                 |
| **配置目录**   | 简洁小写           | `config/`, `settings/`     | 放置配置文件                     |
| **资源目录**   | 小写复数形式         | `static/`, `templates/`, `assets/` | 特别适用于 web 项目              |
| **脚本目录**   | `scripts/`          | `scripts/deploy.py`        | 执行脚本集合                     |

---

## 📁 示例项目结构
my_project/
├── main.py
├── config/
│   └── settings.py
├── core/
│   ├── logic.py
│   └── helpers.py
├── models/
│   └── user.py
├── tests/
│   └── test_user.py
├── scripts/
│   └── migrate_data.py
└── README.md
---

## ❌ 不推荐命名方式

- 驼峰式：`MyModule/` → ❌
- 混合大小写：`DataLoader/` → ❌
- 带空格：`my folder/` → ❌
- 数字开头：`123data/` → ❌

---

## 📌 提示

- 如果该目录是一个 **Python 包**，记得添加 `__init__.py`（哪怕是空文件）。
- 建议为每个目录 **设置职责清晰的名字**，不要“杂物间式”地堆在一起。

---

## ✅ 推荐的 Markdown 文件命名规范

| 命名类型       | 命名规范               | 示例                     | 说明                             |
|----------------|------------------------|--------------------------|----------------------------------|
| **Markdown 文件** | 全小写，单词之间用下划线分隔 | `my_file.md`, `README.md` | 文件名应简洁、描述性强，避免过长 |
| **README 文件** | 使用 `README` 大写字母，并添加 `.md` 后缀 | `README.md`             | 用于项目概述，通常作为根目录文件 |
| **文档文件**   | 全小写，单词之间用下划线分隔 | `installation_guide.md`, `api_reference.md` | 用于存储项目的使用、安装或 API 文档 |
| **章节文件**   | 全小写，使用 `.md` 后缀 | `introduction.md`, `getting_started.md` | 用于分章节的文档内容             |
| **配置文件**   | 小写，使用 `.yaml` 或 `.json` 后缀 | `config.yaml`, `settings.json` | 配置文件通常用于存储项目的配置信息 |
| **数据文件**   | 小写，使用 `.csv`, `.json` 等后缀 | `users.csv`, `data.json` | 存储数据的文件，使用通用格式   |
| **脚本文件**   | 全小写，使用 `.sh` 或 `.py` 后缀 | `deploy.sh`, `generate_report.py` | 用于存储脚本文件，通常与自动化相关 |

---

## 📁 示例项目结构

my_project/
├── README.md
├── config/
│   └── config.yaml
├── docs/
│   ├── introduction.md
│   ├── installation_guide.md
│   └── api_reference.md
├── scripts/
│   └── deploy.sh
└── data/
└── users.csv

---

## ❌ 不推荐命名方式

- 空格：`my file.md` → ❌
- 混合大小写：`MyFile.md` → ❌
- 带特殊字符：`my@file.md` → ❌
- 数字开头：`1st_file.md` → ❌

---

## 📌 提示

- 尽量保持文件名简洁，描述文件内容。
- 使用一致的命名风格，保持项目中所有文件命名的统一性。
- `README.md` 是项目的入口文档，应放置在根目录，详细介绍项目内容、安装及使用方法。
