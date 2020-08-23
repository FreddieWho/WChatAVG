import sys


class keyboard:
    @staticmethod
    def next():
        print(u'(---敲击任意键继续---)')
        input()

    @staticmethod
    def confirm():
        print(u'(---按Y确认, 按其他键跳过---)')
        user_input = input().strip()
        if str(user_input).lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def input():
        print(u'(---请输入---)')
        user_input = input().strip()