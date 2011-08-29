#!/usr/bin/env python
# coding:utf-8

import web
import logging
from handlers import Index,Callback,Processer

logging.basicConfig(level=0,format="%(asctime)s %(levelname)s %(message)s")

urls = ('/','Index',
        '/process','Processer',
        '/callback','Callback')

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
        logging.info("%r" % ex)

if __name__ == '__main__':
    main()
