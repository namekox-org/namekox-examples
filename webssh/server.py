#! -*- coding: utf-8 -*-

# author: forcemain@163.com


import os
import sys
import json


from werkzeug import Response
from logging import getLogger
from eventlet.websocket import WebSocketWSGI
from werkzeug.middleware.shared_data import SharedDataMiddleware
from namekox_webserver.core.entrypoints.app.server import WebServer as BaseWebServer
from namekox_webserver.core.entrypoints.app.handler import WebServerHandler as BaseWebServerHandler
from namekox_websocket.core.entrypoints.app.handler import WebSocketHandler as BaseWebSocketHandler


from minissh import MiniSSH


logger = getLogger(__name__)


class WebServer(BaseWebServer):
    def get_wsgi_app(self):
        app = super(WebServer, self).get_wsgi_app()
        exp = {'/static': os.path.join(os.path.dirname(__file__), 'static')}
        app = SharedDataMiddleware(app, exp)
        return app


class WebServerHandler(BaseWebServerHandler):
    server = WebServer()


class WebSocketHandler(BaseWebSocketHandler):
    def handle_connect(self, request, sock_id, ws_sock):
        ssh_instance = MiniSSH(request.args)
        ssh_instance.connect()
        width = request.args.get('width', 0) or 80
        height = request.args.get('height', 0) or 24
        ssh_instance.get_pty(
            width=int(width),
            height=int(height)
        )
        return ssh_instance

    def handle_request(self, request):
        def handler(ws_sock):
            ssh_instance = None
            sock_id = self.server.add_websocket(ws_sock)
            try:
                ssh_instance = self.handle_connect(request, sock_id, ws_sock)
                self.container.spawn_manage_thread(ssh_instance.forward, args=(ws_sock,))
                while self.accpted:
                    try:
                        data = ws_sock.wait()
                        resp = json.loads(data)
                    except Exception:
                        continue
                    code = resp['code']
                    data = resp['data']
                    if code == 0:
                        data = data.replace('\r', '\n')
                        if not data:
                            break
                        ssh_instance.channel.send(data)
                        self.handle_message(request, sock_id, data)
                    if code == 1:
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


web_app = type(__name__, (object,), {'web': WebServerHandler.decorator})
wss_app = type(__name__, (object,), {'wss': WebSocketHandler.decorator})


class WebSSH(object):
    name = 'webssh'

    storage = {}

    @web_app.web('/', methods=['GET'])
    def index(self, request, **kwargs):
        curpath = os.path.dirname(__file__)
        fileobj = open(os.path.join(curpath, 'index.html'))
        return Response(fileobj.read(), mimetype='text/html')

    @wss_app.wss('/', methods=['GET'])
    def monitor(self, request, sock_id, data):
        if data != '\n':
            sock_id not in self.storage and self.storage.setdefault(sock_id, [])
            self.storage[sock_id].append(data)
            return
        data = ''.join(self.storage.get(sock_id, []))
        logger.debug('ws_sock:{} input: {}'.format(sock_id, data))
        self.storage.pop(sock_id, None)
