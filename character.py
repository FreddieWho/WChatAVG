from utils import keyboard


class Player:
    def create(self, name, character, looks, appearance):
        name = input('你的名字是：')
        character = input('你的职业是：')
        looks = input('你的外形是：')
        appearance = input('你的长相是：')
        self.name = name
        self.character = character
        self.looks = looks
        self.appearance = appearance

