#!/usr/bin/env python
# coding:utf-8

import web
from handlers import Index,Callback,Processer,AuthRequest

urls = ('/','Index',
        '/process','Processer',
        '/callback','Callback',
        '/authrequest','AuthRequest')

#render=web.template.render('templates/')

app = web.application(urls,globals())

if web.config.get("_session") is None:
    session=web.session.Session(app,web.session.DiskStore("webbo2citespace_session"))
    web.config._session=session
else:
    session=web.config._session

def main():
    try:
        app.run()
    except Exception,ex:
        print ex

if __name__ == '__main__':
    main()
