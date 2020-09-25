#! -*- coding: utf-8 -*-

# author: forcemain@163.com


import os


from werkzeug.middleware.shared_data import SharedDataMiddleware


class SharedData(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, obj):
        cur = os.path.join(os.path.dirname(__file__), 'static')
        return SharedDataMiddleware(self.app, {'/static': cur})
