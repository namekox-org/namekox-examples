# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from namekox_zookeeper.core.allotter import Allotter
from namekox_webserver.core.entrypoints.app import app
from namekox_context.core.dependencies import ContextHelper
from namekox_webserver.constants import DEFAULT_WEBSERVER_PORT
from namekox_zookeeper.core.dependencies import ZooKeeperHelper
from namekox_zookeeper.constants import DEFAULT_ZOOKEEPER_SERVICE_ROOT_PATH


from .. import constants
from ..common.dispatch import Dispatcher


class Gateway(object):
    name = 'gateway'

    ctx = ContextHelper()
    zk = ZooKeeperHelper(
        name,
        allotter=Allotter(),
        roptions={'port': DEFAULT_WEBSERVER_PORT},
        watching=DEFAULT_ZOOKEEPER_SERVICE_ROOT_PATH
    )

    # as gateway service
    @app.api('/api/dispatch/', methods=constants.DEFAULT_DISPATCH_METHODS)
    def dispatch(self, request):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "",
            "args": "[]",
            "data": "{}"
        }
        """
        return Dispatcher(self)(request).dispatch()
