import utils.keyboard 


class Player:
    def create(self):
        if hasattr(self,'Name'):
            print(u'你已经创建了角色')
        else:
            print(u'Welcome To The Oasis')
            print(u'你的名字是：')
            self.Name = keyboard.input()
            print(u'你的职业是：')
            self.Character = keyboard.input()
            print(u'你的外形是：：')
            self.Look = keyboard.input()
            print(u'你的长相是：')
            self.Appearence = keyboard.input()
            
            print(u'角色创建完成')


    
 
