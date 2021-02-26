#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


from logging import getLogger
from werkzeug.utils import redirect
from namekox_webserver.core.entrypoints.app import WebServerHandler


from .common.handler import WebSocketHandler


logger = getLogger(__name__)

web = WebServerHandler.decorator
wss = WebSocketHandler.decorator


class WebSSH(object):
    name = 'webssh'

    storage = {}

    @web('/', methods=['GET'])
    def index(self, request):
        qstr = request.query_string
        page = '/frontend/index.html'
        return redirect(page + '?' + qstr)

    @wss('/', methods=['GET'])
    def monitor(self, request, sock_id, data):
        if data != '\n':
            sock_id not in self.storage and self.storage.setdefault(sock_id, [])
            self.storage[sock_id].append(data)
            return
        data = ''.join(self.storage.get(sock_id, []))
        logger.debug('ws_sock:{} input: {}'.format(sock_id, data))
        self.storage.pop(sock_id, None)
