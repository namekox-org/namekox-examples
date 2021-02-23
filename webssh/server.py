#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import os


from werkzeug import Response
from logging import getLogger
from handler import WebSocketHandler
from namekox_webserver.core.entrypoints.app.handler import WebServerHandler


logger = getLogger(__name__)


app = type(__name__, (object,), {'web': WebServerHandler.decorator, 'wss': WebSocketHandler.decorator})


class WebSSH(object):
    name = 'webssh'

    storage = {}

    @app.web('/', methods=['GET'])
    def index(self, request, **kwargs):
        curpath = os.path.dirname(__file__)
        fileobj = open(os.path.join(curpath, 'index.html'))
        return Response(fileobj.read(), mimetype='text/html')

    @app.wss('/', methods=['GET'])
    def monitor(self, request, sock_id, data):
        if data != '\n':
            sock_id not in self.storage and self.storage.setdefault(sock_id, [])
            self.storage[sock_id].append(data)
            return
        data = ''.join(self.storage.get(sock_id, []))
        logger.debug('ws_sock:{} input: {}'.format(sock_id, data))
        self.storage.pop(sock_id, None)
