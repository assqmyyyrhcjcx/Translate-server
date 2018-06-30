#encoding: utf-8

import requests
import json
from models import Language

class DataTool(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data
        self.headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

    def getCallbackData(self):
        if self.method.upper() == 'GET':
            response = requests.get(self.url, headers=self.headers, params=self.data)
        else:
            response = requests.post(self.url, headers=self.headers, data=self.data)

        result_json = json.loads(response.content.decode(),encoding='utf-8')
        return result_json

class LanguageEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Language):
            return obj.name, obj.alias
        return json.JSONEncoder.default(self, obj)


