#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import sys
import json


from logging import getLogger
from eventlet.websocket import WebSocketWSGI
from namekox_websocket.core.entrypoints.app.handler import WebSocketHandler as BaseWebSocketHandler


from .minissh import MiniSSH


logger = getLogger(__name__)


class WebSocketHandler(BaseWebSocketHandler):
    def handle_connect(self, request, sock_id, ws_sock):
        ssh_instance = MiniSSH(request.args)
        ssh_instance.connect()
        height = request.args.get('height', 24)
        width = request.args.get('width', 80)
        ssh_instance.get_pty(
            width=int(width),
            height=int(height)
        )
        return ssh_instance

    def handle_request(self, request):
        def handler(ws_sock):
            ssh_instance = None
            sock_id = self.server.hub.add_wsock(ws_sock)
            try:
                ssh_instance = self.handle_connect(request, sock_id, ws_sock)
                self.container.spawn_manage_thread(ssh_instance.forward, args=(ws_sock,))
                while self.accpted:
                    data = ws_sock.wait()
                    resp = json.loads(data)
                    code = resp['code']
                    data = resp['data']
                    if str(code) == '0':
                        data = data.replace('\r', '\n')
                        if not data:
                            break
                        ssh_instance.channel.send(data)
                        self.handle_message(request, sock_id, data)
                    if str(code) == '1':
                        ssh_instance.set_pty(**data)
            except Exception as e:
                msg = 'ws_sock:{} send msg error {}'.format(sock_id, e.message)
                logger.error(msg)
            finally:
                exc_info = sys.exc_info()
                ssh_instance and ssh_instance.close()
                self.handle_sockclose(request, sock_id, exc_info)
        response = WebSocketWSGI(handler)
        return response

    def handle_response(self, request, context, result):
        pass

    def handle_exception(self, request, context, exc_info):
        pass
