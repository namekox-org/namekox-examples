#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


import os


from werkzeug.middleware.shared_data import SharedDataMiddleware


class StaticFilesMiddleware(object):
    def __init__(self, app):
        self.app = app
        self.path = '/frontend'

    def __call__(self, environ, start_response):
        cdir = os.path.os.path.dirname(__file__)
        path = os.path.join(os.path.dirname(cdir), 'frontend')
        app = SharedDataMiddleware(self.app, {self.path: path})
        return app(environ, start_response)
