
#!/usr/bin/env python
# coding:utf-8
import web

render=web.template.render('templates/')

class Index:
    def GET(self):
        return render.index()

class Callback:
    def GET(self):
        return render.error_404()

class Processer:
    def GET(self):
        return render.error_404()