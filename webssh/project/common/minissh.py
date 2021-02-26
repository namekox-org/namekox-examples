#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


import paramiko


from namekox_core.core.friendly import ignore_exception, AsLazyProperty


class MiniSSH(object):
    def __init__(self, options=None):
        self.client = None
        self._running = True
        options = options or {}
        self.hostport = options.get('port', 22)
        self.hostport = int(self.hostport)
        self.username = options.get('user', 'root')
        self.password = options.get('pass', 'root')
        self.hostname = options.get('host', '127.0.0.1')

    @AsLazyProperty
    def channel(self):
        return self.transport.open_session()

    @AsLazyProperty
    def transport(self):
        return self.client.get_transport()

    def connect(self, **kwargs):
        allow_agent = kwargs.pop('allow_agent', False)
        lookforkeys = kwargs.pop('look_for_keys', False)
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            port=self.hostport,
            username=self.username,
            password=self.password,
            hostname=self.hostname,
            allow_agent=allow_agent,
            look_for_keys=lookforkeys,
            **kwargs
        )

    def forward(self, to, chunk=4096):
        self.channel.invoke_shell()
        while self._running:
            data = self.channel.recv(chunk)
            if not data:
                break
            to.send(data)

    def get_pty(self, **kwargs):
        self.channel.get_pty(**kwargs)

    def set_pty(self, **kwargs):
        self.channel.resize_pty(**kwargs)

    def close(self):
        self._running = False
        ignore_exception(self.client.close)()
