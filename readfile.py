class ReadFile:
    def __init__(self, file_path, st):
        self.st = st
        self.file_path = file_path

    def search_str(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
            find = content.find(self.st)
            print(find.__index__())


ro = ReadFile(r"C:/Users/MPrabhakar/Documents/catalina.2022-09-27.log", "ERROR")
ro.search_str()
