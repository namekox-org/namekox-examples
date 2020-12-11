# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import json


from namekox_webserver.core.request import JsonRequest
from namekox_webserver.constants import DEFAULT_WEBSERVER_H_PREFIX


from .. import schema, exceptions
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
        transport_klss = TRANSPORTS_MAP.get(transport_name, XMLRPCDispatcher)
        return transport_klss(self.service, request)


class BaseDispatcher(object):
    name = None

    def __init__(self, service, request):
        self.service = service
        self.request = request

    def dispatch(self, *args, **kwargs):
        raise NotImplementedError

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

    def is_login(self, request):
        raise exceptions.AuthenticateFailed(self.name)

    def has_perm(self, request):
        raise exceptions.PermissionDenied(self.name)


class XMLRPCDispatcher(BaseDispatcher):
    name = 'xmlrpc'

    def req_json(self):
        data = self.request.get_json()
        return schema.RequestCreateSchema(strict=True).load(data).data

    def req_user(self):
        return

    def req_path(self):
        return self.req_json()['path']

    def req_args(self):
        data = self.req_json()['args']
        return json.loads(data)

    def req_data(self):
        data = self.req_json()['data']
        return json.loads(data)

    def req_time(self):
        return self.req_json()['time']

    def is_login(self, request):
        return True

    def has_perm(self, request):
        return True

    def dispatch(self, *args, **kwargs):
        request = JsonRequest(self.request)
        request.is_valid(raise_exception=True)
        self.request = request
        self.has_perm(request)
        name = request.method.lower()
        func = getattr(self, name)
        return func(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        service_name, method_name = self.req_path().strip('/').split('/', 1)
        service = getattr(XMLRpcProxy(self.service, timeout=self.req_time()), service_name)
        reqfunc = getattr(service, method_name)
        return reqfunc(*self.req_args(), **self.req_data())


TRANSPORTS_KEY = [XMLRPCDispatcher.name]
TRANSPORTS_VAL = [XMLRPCDispatcher]
TRANSPORTS_MAP = dict(zip(TRANSPORTS_KEY, TRANSPORTS_VAL))
