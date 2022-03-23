import os
import re


class FileWriter:
    # 将字符串写出到文件
    @staticmethod
    def write_result(path, result):
        path_dir = re.sub(r"[^/\\]+[/\\]*$", "", path)
        if not os.path.isdir(path_dir):
            os.makedirs(path_dir)

        file_to_write = open(path, "x", encoding="utf-8")
        file_to_write.write(result)
        file_to_write.close()
