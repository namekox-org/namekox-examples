# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from namekox_xmlrpc.core.client import ServerProxy
from namekox_xmlrpc.core.messaging import gen_message_headers
from namekox_xmlrpc.constants import DEFAULT_XMLRPC_CALL_MODE_ID, DEFAULT_XMLRPC_TB_CALL_MODE, DEFAULT_XMLRPC_YB_CALL_MODE


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
        self.target_method = target_method
        server = proxy.service.zk.allotter.get(target_service)
        uri = '{}://{}:{}'.format(proxy.protocol, server['address'], server['port'])
        transport_timeout = proxy.timeout
        transport_headers = gen_message_headers(proxy.service.ctx.data)
        self.target_service = ServerProxy(uri, transport_timeout=transport_timeout, transport_headers=transport_headers)

    def call_async(self, *args, **kwargs):
        kwargs.setdefault(DEFAULT_XMLRPC_CALL_MODE_ID, DEFAULT_XMLRPC_YB_CALL_MODE)
        return self.target_service.__getattr__(self.target_method)(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        kwargs.setdefault(DEFAULT_XMLRPC_CALL_MODE_ID, DEFAULT_XMLRPC_TB_CALL_MODE)
        return self.target_service.__getattr__(self.target_method)(*args, **kwargs)
