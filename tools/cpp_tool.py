import subprocess
import os

def run_cpp(filename,input_data=""):
    source = os.path.join("workspace", filename)

    exe = os.path.join("workspace", "temp.exe")

    compile_result = subprocess.run(
        ["g++", source, "-o", exe],
        capture_output = True,
        text = True
    )

    if compile_result.returncode != 0:
        return "编译错误：\n" + compile_result.stderr

    run_result = subprocess.run(
        [exe],
        input = input_data,
        capture_output = True,
        text = True
    )

    return (
        "运行输出：\n"
        + run_result.stdout
        + "\n错误信息："
        + run_result.stderr
    )
