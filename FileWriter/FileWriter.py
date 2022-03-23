class FileWriter:
    # 将字符串写出到文件
    @staticmethod
    def write_result(path, result):
        file_to_write = open(path, "w", encoding="utf-8")
        file_to_write.write(result)
        file_to_write.close()
