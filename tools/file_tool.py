import os

def read_file(filename):
    path = os.path.join("workspace", filename)

    with open(path, "r", encoding = "utf-8") as f:
        return f.read()
