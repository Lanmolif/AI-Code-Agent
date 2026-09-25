import os
import json
from openai import OpenAI
from tools.file_tool import read_file
from tools.cpp_tool import run_cpp
from tools.compile_cpp import compile_cpp
from tools.write_file import write_file
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("DEEPSEEK_API_KEY"),
    base_url = "https://api.deepseek.com",
)

if not os.getenv("DEEPSEEK_API_KEY"):
    raise Exception("请配置 .env 文件中的 DEEPSEEK_API_KEY")

tools = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "读取workspace文件夹种的代码文件",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "要读取的文件名，例如 test.cpp",
                        }
                    },
                    "required": ["filename"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_cpp",
            "description": """
                            执行C++程序。
                            当用户要求运行、测试、验证代码，
                            或者需要查看程序实际输出时，
                            应该调用此工具。
                            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "要运行的C++文件名，例如test.cpp"
                    },
                    "input_data": {
                        "type": "string",
                        "description":  "程序运行时需要输入的数据"
                    }
            },
                "reqiured": ["filename"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "compile_cpp",
            "description": """
                编译c++代码。
                当用户要求检查代码是否能编译，
                或运行代码时调用。
                """,
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "c++文件名"
                    }
                },
                "reqiured": [
                    "filename"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": """
            修改workspace中的代码文件。

            当用户要求修复代码、
            修改代码内容时调用。

            filename表示文件名，
            content表示完整的新文件内容。
            """,
            "parameter": {
                "type": "object",
                "properties": {

                    "filename": {
                        "type": "string",
                        "description": "文件名，例如test.cpp"
                    },

                    "content": {
                        "type": "string",
                        "description": "修改后的完整代码"
                    }
                },
                "reqiured": [
                    "filename",
                    "content"
                ]
            }
        }
    }
]

messages = [
    {
        "role": "system",
        "content":
                    """
                    你是一个AI代码助手。

                    当用户要求分析代码时：

                    1. 首先使用 read_file 获取代码内容。
                    2. 如果需要检查语法或编译问题，调用 compile_cpp。
                    3. 如果程序需要测试运行，调用 run_cpp。
                    4. 根据工具返回结果生成详细分析。

                    不要猜测代码内容，必须通过工具获取。
                    """
    }
]

user_input = input("你：")

messages.append({
    "role": "user",
    "content": user_input,
})

while True:
    response = client.chat.completions.create(
        model = "deepseek-flash",
        messages = messages,
        tools = tools,
    )

    message = response.choices[0].message

    if not message.tool_calls:
        break

    messages.append({
        "role": "assistant",
        "content": None,
         "tool_calls": message.tool_calls
    })
    
    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("\nAI想调用工具：")
        print("工具名称：",tool_name)
        print("参数：",arguments)


        if tool_name == "read_file":

            result = read_file(
                arguments["filename"]
            )

        elif tool_name == "run_cpp":

            result = run_cpp(
                arguments["filename"],
                arguments.get("input_data", "")
            )

        elif tool_name == "compile_cpp":

             result = compile_cpp(
                 arguments["filename"]
                 )

        elif tool_name == "write_file":

            result = write_file(
                arguments["filename"],
                arguments["content"]
                )
        else:

            result = "未知工具"


        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        })


print("\nAI最终分析：")
print(message.content)














    








    
