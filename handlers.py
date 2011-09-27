
#!/usr/bin/env python
# coding:utf-8
import web
import logging
import auth

logging.basicConfig(level=0,format="%(asctime)s %(levelname)s %(message)s")

render=web.template.render('templates/')
db =web.database(dbn='sqlite',db="storages.db")


class Index:
    """Index page"""
    def GET(self):
        return render.index()

class Callback:
    """OAuth callback"""
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
            return 'error'

    def checkBinding(self,weibo_type):
        logging.info("checking %s" % weibo_type)
        tokens=db.query("select auth_key from tokens where user_type='%s'" % weibo_type).list()

        if not tokens[0].auth_key:
            return 'false'
        else:
            return 'true'

class AuthRequest():
    def GET(self):
        indata=web.input()
        weibo_type=indata.get("type",None)

        if weibo_type:
            auth.do_oauth(weibo_type)

