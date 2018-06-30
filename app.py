#encoding: utf-8
from flask import Flask
import config
from models import Language
from exts import db
from normal import DataTool
import json
from flask import request
import pickle

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/getAssociateResult/', methods=["GET", "POST"])
def getAssociateResult():
    kw = request.get_data()
    url = 'http://fanyi.baidu.com/sug'
    method = 'post'
    data = json.loads(kw)
    tool = DataTool.DataTool(method, url, data)
    result = json.dumps(tool.getCallbackData())
    print(result)
    return result

@app.route('/getLanguage', methods=['GET', 'POST'])
def getLanguage():
    result = {}
    try:
        result['status'] = 200
        language = Language.query.all()
    except:
        result['status'] = 500
        language = None

    data = {}
    values = []
    for i in language:
        data[i.alias] = i.name
        values.append(i.alias)

    result['data'] = data
    result['values'] = values
    return json.dumps(result, cls=DataTool.LanguageEncoder)

@app.route('/translate', methods=['POST'])
def translate():
    url = 'http://fanyi.baidu.com/basetrans'
    method = 'post'
    data = json.loads(request.get_data())
    tool = DataTool.DataTool(method, url, data)
    result = json.dumps(tool.getCallbackData())
    print(result)
    return result


if __name__ == '__main__':
    app.run()
