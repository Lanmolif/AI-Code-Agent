import subprocess
import os


def compile_cpp(filename):

    filepath = os.path.join(
        "workspace",
        filename
    )

    output_file = filepath.replace(
        ".cpp",
        ".exe"
    )


    command = [
        "g++",
        filepath,
        "-o",
        output_file
    ]


    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )


        if result.returncode == 0:

            return "编译成功"


        else:

            return (
                "编译失败:\n"
                + result.stderr
            )


    except Exception as e:

        return f"编译异常:{e}"
