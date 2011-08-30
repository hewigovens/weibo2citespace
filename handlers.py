
#!/usr/bin/env python
# coding:utf-8
import web

render=web.template.render('templates/')
db =web.database(dbn='sqlite',db="storages.db")


class Index:
    def GET(self):
        return render.index()

class Callback:
    def GET(self):
        return render.error_404()

class Processer:
    '''process all requests'''
    def GET(self):
        indata=web.input()
        weibo_type=indata.get("type",None)
        if weibo_type:
            return self.checkBinding(weibo_type)
        else:
            return '''<?xml version="1.0" encoding="UTF-8"?><Binding>false</Binding>'''

    def checkBinding(self,weibo_type):
        print weibo_type
        tokens = db.select('tokens')
        print tokens
        return '''<?xml version="1.0" encoding="UTF-8"?><Binding>false</Binding>'''

class AuthRequest():
    def GET(self):
        pass