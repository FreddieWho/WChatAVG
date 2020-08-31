import json


class read():
    @staticmethod
    def read(dict):
        return json.load(dict, 'r', encoding='utf8')
