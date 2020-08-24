from utils.keyboard import * 


class Player:
    def create(self, name, character, looks, appearance):
        print(u'Welcome To The Oasis')
        print(u'你的名字是：')
        self.name = keyboard.input()
        print(u'你的职业是：')
        self.name = keyboard.input()
        print(u'你的外形是：：')
        self.name = keyboard.input()
        print(u'你的长相是：')
        self.name = keyboard.input()

        print(u'角色创建完成')