# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


class BaseHelper(object):
    def __init__(self, service):
        self.service = service

    def _raise(self, exc, errs=None):
        raise (exc() if errs is None else exc(errs))

    def filter(self, uid):
        pass
