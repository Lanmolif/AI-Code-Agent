import os

def write_file(filename, content):

    filepath = os.path.join(
        "workspace",
        filename
    )

    try:

        with open(
            filepath,
            "w",
            encoding = "utf-8"
        ) as f:

            f.write(content)

        return f"{filename}修改成功"


    except Exception as e:

        return f"修改失败：{e}"
