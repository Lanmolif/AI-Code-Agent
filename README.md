# AI-Code-Agent

基于大语言模型（LLM）Function Calling 的智能代码助手 Agent。

本项目通过调用大语言模型 API，实现了一个能够自主调用工具完成代码分析、编译检查、自动修复以及运行验证的 AI Coding Agent。

---

## 项目介绍

传统代码助手通常只能根据用户输入提供代码建议，而本项目尝试构建一个具备工具调用能力（Tool Calling）的 AI Agent。

用户提出代码相关需求后，Agent 可以根据任务自主选择工具：

- 读取代码文件
- 编译 C++ 程序
- 分析编译错误
- 修改代码文件
- 执行程序并验证结果

实现从代码分析到代码修复的自动化闭环。

---

## 技术栈

- Python
- Large Language Model API
- Function Calling
- C++
- subprocess
- 文件系统操作

---

## 项目结构

AI-Code-Agent

├── main.py                 Agent核心逻辑

├── tools                   Agent工具目录
│   ├── read_file.py        读取代码文件
│   ├── compile_cpp.py      C++编译检测
│   ├── run_cpp.py          C++程序运行
│   └── write_file.py       修改代码文件

├── workspace               工作目录
│   └── test.cpp

├── README.md

└── requirements.txt


---

## Agent架构

用户请求

↓

LLM Agent

↓

根据任务选择工具

↓

read_file
获取代码

↓

compile_cpp
检测编译错误

↓

write_file
修改代码

↓

run_cpp
运行验证

↓

AI生成分析报告


---

## 已实现功能

### 1. 代码读取

工具：

read_file(filename)

功能：

- 获取 workspace 中的源代码
- 将代码内容提供给大语言模型分析
- 避免用户手动复制代码


---

### 2. C++编译检测

工具：

compile_cpp(filename)

功能：

- 调用 g++ 编译 C++ 文件
- 获取编译器错误信息
- 将错误反馈给 Agent 分析


示例：

错误代码：

cout << i << " "

编译器返回：

expected ';' before '}'

Agent 可以根据错误信息定位代码问题。


---

### 3. 自动修改代码

工具：

write_file(filename, content)

功能：

- 根据模型生成结果修改代码
- 自动完成代码修复


---

### 4. 程序运行测试

工具：

run_cpp(filename, input_data)

功能：

- 执行 C++ 程序
- 获取标准输出
- 验证代码修改结果


---

## Agent工作流程

用户：

修复 test.cpp 的错误


Agent执行：

1. read_file

读取源代码

↓

2. compile_cpp

获取编译错误

↓

3. 分析错误原因

↓

4. write_file

修改代码

↓

5. compile_cpp

重新验证

↓

6. run_cpp

测试运行

↓

7. 输出修复报告


---

## 示例

用户输入：

修复 test.cpp 的错误


Agent执行：

AI调用:
read_file

AI调用:
compile_cpp

发现错误:
expected ';'

AI调用:
write_file

AI调用:
compile_cpp

AI调用:
run_cpp


最终输出：

修复成功

编译:
success

运行:
0 1 2 3 4


---

## 项目特点

- 基于 LLM Function Calling 实现 Agent 工具调用
- 实现代码读取、编译、修改、执行完整闭环
- 支持自动分析编译错误
- 模拟 AI Coding Assistant 基本工作流程


---

## 后续优化方向

- 增加代码 Diff 修改模式
- 增加 Git 版本管理
- 增加多语言支持
- 增加代码质量分析
- 引入更加安全的代码执行环境
- 支持更复杂的软件开发任务


---

## 安装运行

安装依赖：

pip install -r requirements.txt


运行：

python main.py


---

## Future Work

进一步探索大语言模型在软件开发流程自动化中的应用：

- 自动代码审查
- 自动 Bug 修复
- AI辅助程序设计
- 自动化测试生成