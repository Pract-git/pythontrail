import re


class Extract:
    def __init__(self, logpath):
        self.logpath = logpath


class Reg_Match1(Extract):
    def __init__(self, logpath):
        super().__init__(logpath)

    def work(self):
        pattern = "^(.*?(\bERROR\b)[^$]*)$"
        str1 = self.logpath
        match = re.match(pattern, str1)
        return match


m = Reg_Match1('some text containing ERROR and some not')
print(m.logpath)
print(m.work())
