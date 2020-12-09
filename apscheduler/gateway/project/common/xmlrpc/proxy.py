# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from namekox_xmlrpc.core.client import ServerProxy
from namekox_xmlrpc.core.messaging import gen_message_headers


class XMLRpcProxy(object):
    def __init__(self, service, protocol='http', timeout=None):
        self.service = service
        self.timeout = timeout
        self.protocol = protocol

    def __call__(self, protocol='http', timeout=None):
        self.timeout = timeout
        self.protocol = protocol

    def __getattr__(self, target_service):
        return XMLRpcService(self, target_service)


class XMLRpcService(object):
    def __init__(self, proxy, target_service):
        self.proxy = proxy
        self.target_service = target_service

    def __getattr__(self, target_method):
        return XMLRpcMethod(self.proxy, self.target_service, target_method)


class XMLRpcMethod(object):
    def __init__(self, proxy, target_service, target_method):
        self.proxy = proxy
        self.target_service = target_service
        self.target_method = target_method

    def __call__(self, *args, **kwargs):
        server = self.proxy.service.zk.allotter.get(self.target_service)
        uri = '{}://{}:{}'.format(self.proxy.protocol, server['address'], server['port'])
        transport_timeout = self.proxy.timeout
        transport_headers = gen_message_headers(self.proxy.service.ctx.data)
        target = ServerProxy(uri, transport_timeout=transport_timeout, transport_headers=transport_headers)
        return target.__getattr__(self.target_method)(*args, **kwargs)
