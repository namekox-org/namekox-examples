# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import json


from namekox_webserver.core.request import JsonRequest
from namekox_webserver.constants import DEFAULT_WEBSERVER_H_PREFIX


from .. import exceptions
from .xmlrpc.proxy import XMLRpcProxy


class Dispatcher(object):
    def __init__(self, service):
        self.service = service

    @staticmethod
    def get_transport_name(request):
        name = 'http-{}-transport'.format(DEFAULT_WEBSERVER_H_PREFIX).upper().replace('-', '_')
        return request.environ.get(name, None)

    def __call__(self, request):
        transport_name = self.get_transport_name(request)
        transport_klss = TRANSPORTS_MAP.get(transport_name, XMLRpcDispatcher)
        return transport_klss(self.service, request)


class BaseDispatcher(object):
    name = None

    def __init__(self, service, request):
        self.service = service
        self.request = request

    def get(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def post(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def put(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def patch(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def delete(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def head(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def options(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def trace(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(self.name)

    def dispatch(self, *args, **kwargs):
        name = self.request.method.lower()
        func = getattr(self, name)
        return func(self.request, *args, **kwargs)


class XMLRpcDispatcher(BaseDispatcher):
    name = 'xmlrpc'

    def post(self, request, *args, **kwargs):
        rspdata = request.get_json()
        reqpath = rspdata['path']
        # compatible old version
        reqpath = reqpath.replace('.', '/')
        service_name, method_name = reqpath.strip('/').split('/', 1)
        reqargs = json.loads(rspdata.get('args', '[]'))
        reqdata = json.loads(rspdata.get('data', '{}'))
        rspfunc = XMLRpcProxy(self.service).__getattr__(service_name).__getattr__(method_name)
        return rspfunc(*reqargs, **reqdata)

    def dispatch(self, *args, **kwargs):
        request = JsonRequest(self.request)
        request.is_valid(raise_exception=True)
        name = request.method.lower()
        func = getattr(self, name)
        return func(request, *args, **kwargs)


TRANSPORTS_KEY = [XMLRpcDispatcher.name]
TRANSPORTS_VAL = []
TRANSPORTS_MAP = dict(zip(TRANSPORTS_KEY, TRANSPORTS_VAL))
