#! -*- coding: utf-8 -*-

# author: forcemain@163.com


import os


from werkzeug.middleware.shared_data import SharedDataMiddleware


class StaticServerMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        basedir = os.path.dirname(__file__)
        mapping = {
            '/static': os.path.join(basedir, 'static'),
        }
        handler = SharedDataMiddleware(self.app, mapping)
        return handler(environ, start_response)
