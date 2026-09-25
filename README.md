# AI-Code-Agent

一个基于 **LLM Function Calling** 架构实现的智能代码 Agent。

本项目模拟 AI Coding Assistant 的工作流程，通过调用大语言模型 API，使 Agent 能够自主选择并调用工具，完成代码读取、编译检测、错误分析、代码修改以及运行验证，实现从问题发现到修复验证的自动化闭环。

---

## 项目介绍

传统代码助手通常只能根据用户输入提供代码建议，而本项目尝试构建一个具备 **工具调用能力（Tool Calling）** 的 AI Agent。

用户提出代码相关任务后，Agent 可以根据任务需求自主决定调用不同工具：

- 读取代码文件
- 编译 C++ 程序
- 分析编译错误
- 修改代码文件
- 执行程序并验证结果

整体流程：

```
用户请求
    ↓
LLM Agent
    ↓
自主选择工具
    ↓
读取代码
    ↓
编译检查
    ↓
分析错误
    ↓
修改代码
    ↓
运行验证
    ↓
生成结果报告
```

---

## 功能特点

### 1. 代码文件读取

工具：

```
read_file(filename)
```

功能：

- 获取 workspace 中的源代码文件
- 将代码内容提供给大语言模型分析
- 避免用户手动复制代码


---

### 2. C++ 编译检测

工具：

```
compile_cpp(filename)
```

功能：

- 调用 g++ 编译 C++ 文件
- 获取编译器错误信息
- 将错误反馈给 Agent 进行分析


示例：

错误代码：

```cpp
cout << i << " "
```

编译器返回：

```
expected ';' before '}' token
```

Agent 可以根据错误信息定位问题：

缺少分号 `;`

---

### 3. 自动修改代码

工具：

```
write_file(filename, content)
```

功能：

- 根据模型分析结果修改源代码
- 自动完成代码修复


---

### 4. 程序运行验证

工具：

```
run_cpp(filename, input_data)
```

功能：

- 执行 C++ 程序
- 获取标准输出
- 验证修改后的代码是否正确


---

## 技术栈

- Python
- Large Language Model API
- Function Calling
- C++
- subprocess
- 文件系统操作
- Git


---

## 项目结构

```text
AI-Code-Agent
│
├── main.py                 # Agent核心逻辑
│
├── tools                   # Agent工具目录
│   ├── file_tool.py        # 文件读取工具
│   ├── compile_cpp.py      # C++编译工具
│   ├── run_cpp.py          # C++运行工具
│   └── write_file.py       # 文件修改工具
│
├── workspace               # 工作目录
│   └── test.cpp
│
├── requirements.txt
│
├── README.md
│
└── .env                    # API Key配置文件
```

---

## Agent 工作流程示例

用户：

```
修复 test.cpp 的错误
```

Agent：

```
调用 read_file
        ↓
读取源代码

调用 compile_cpp
        ↓
获取编译错误

分析错误原因

调用 write_file
        ↓
修改代码

调用 compile_cpp
        ↓
重新编译验证

调用 run_cpp
        ↓
运行测试

输出修复报告
```

---

## 示例

用户输入：

```
运行 test.cpp，输入5
```

Agent 执行：

```
AI调用:
read_file

AI调用:
run_cpp
```

最终输出：

```
程序运行成功

输入:
5

输出:
0 1 2 3 4
```

---

## 环境配置

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

---

### 2. 配置 API Key

在项目根目录创建：

```
.env
```

填写：

```text
DEEPSEEK_API_KEY=your_api_key
```

程序会自动读取环境变量：

```python
os.environ.get("DEEPSEEK_API_KEY")
```

---

### 3. 运行

```bash
python main.py
```

---

## 已实现能力

- ✅ LLM API 调用
- ✅ Function Calling 工具调用
- ✅ 文件读取
- ✅ 文件修改
- ✅ C++ 自动编译
- ✅ C++ 程序运行
- ✅ 编译错误分析
- ✅ 自动修复代码
- ✅ 自动验证运行结果


---

## 项目亮点

- 基于 LLM Function Calling 实现 Agent 自主决策
- 将大语言模型与真实开发工具结合
- 实现代码分析 → 错误定位 → 修改 → 验证的完整闭环
- 模拟 AI Coding Assistant 基本工作流程


---

## 后续优化方向

- 增加代码 Diff 修改模式
- 保存 Agent 执行日志
- 增加 Git 版本管理
- 支持更多编程语言
- 增加代码质量分析
- 增强代码执行安全隔离
- 支持更复杂的软件开发任务


---

## Future Work

探索大语言模型在软件开发流程自动化中的应用：

- 自动代码审查
- 自动 Bug 修复
- AI 辅助程序设计
- 自动化测试生成