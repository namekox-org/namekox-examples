# Running
> config.yaml
```yaml
WEBSERVER:
  host: 0.0.0.0
  port: 80
```
> namekox run facade
```shell script
2020-12-09 11:31:35,435 DEBUG load container class from namekox_core.core.service.container:ServiceContainer
2020-12-09 11:31:35,436 DEBUG starting services ['gateway']
2020-12-09 11:31:35,436 DEBUG starting service gateway entrypoints [gateway:namekox_webserver.core.entrypoints.app.server.WebServer:server, gateway:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:dispatch]
2020-12-09 11:31:35,438 DEBUG spawn manage thread handle gateway:namekox_webserver.core.entrypoints.app.server:handle_connect(args=(), kwargs={}, tid=handle_connect)
2020-12-09 11:31:35,438 DEBUG service gateway entrypoints [gateway:namekox_webserver.core.entrypoints.app.server.WebServer:server, gateway:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:dispatch] started
2020-12-09 11:31:35,438 DEBUG starting service gateway dependencies [gateway:namekox_context.core.dependencies.ContextHelper:ctx, gateway:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk]
2020-12-09 11:31:35,440 INFO Connecting to 127.0.0.1:2181
2020-12-09 11:31:35,441 DEBUG Sending request(xid=None): Connect(protocol_version=0, last_zxid_seen=0, time_out=10000, session_id=0, passwd='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', read_only=None)
2020-12-09 11:31:35,468 INFO Zookeeper connection established, state: CONNECTED
2020-12-09 11:31:35,469 DEBUG Sending request(xid=1): GetChildren(path='/namekox', watcher=<bound method ChildrenWatch._watcher of <kazoo.recipe.watchers.ChildrenWatch object at 0x10e0cac90>>)
2020-12-09 11:31:35,476 DEBUG Received response(xid=1): []
2020-12-09 11:31:35,491 DEBUG Sending request(xid=2): Exists(path='/namekox', watcher=None)
2020-12-09 11:31:35,496 DEBUG Received response(xid=2): ZnodeStat(czxid=74, mzxid=74, ctime=1606123632647, mtime=1606123632647, version=0, cversion=476, aversion=0, ephemeralOwner=0, dataLength=0, numChildren=0, pzxid=985)
2020-12-09 11:31:35,497 DEBUG Sending request(xid=3): Create(path='/namekox/gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4', data='{"port": 80, "address": "127.0.0.1"}', acl=[ACL(perms=31, acl_list=['ALL'], id=Id(scheme='world', id='anyone'))], flags=1)
2020-12-09 11:31:35,505 DEBUG Received EVENT: Watch(type=4, state=3, path=u'/namekox')
2020-12-09 11:31:35,506 DEBUG Sending request(xid=4): GetChildren(path='/namekox', watcher=<bound method ChildrenWatch._watcher of <kazoo.recipe.watchers.ChildrenWatch object at 0x10e0cac90>>)
2020-12-09 11:31:35,507 DEBUG Received response(xid=3): u'/namekox/gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4'
2020-12-09 11:31:35,509 DEBUG service gateway dependencies [gateway:namekox_context.core.dependencies.ContextHelper:ctx, gateway:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk] started
2020-12-09 11:31:35,509 DEBUG Received response(xid=4): [u'gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4']
2020-12-09 11:31:35,510 DEBUG Sending request(xid=5): GetData(path='/namekox/gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4', watcher=None)
2020-12-09 11:31:35,510 DEBUG services ['gateway'] started
2020-12-09 11:31:35,516 DEBUG Received response(xid=5): ('{"port": 80, "address": "127.0.0.1"}', ZnodeStat(czxid=988, mzxid=988, ctime=1607484695498, mtime=1607484695498, version=0, cversion=0, aversion=0, ephemeralOwner=72084539296317623, dataLength=36, numChildren=0, pzxid=988))
2020-12-09 11:31:45,365 DEBUG Received EVENT: Watch(type=4, state=3, path=u'/namekox')
2020-12-09 11:31:45,368 DEBUG Sending request(xid=6): GetChildren(path='/namekox', watcher=<bound method ChildrenWatch._watcher of <kazoo.recipe.watchers.ChildrenWatch object at 0x10e0cac90>>)
2020-12-09 11:31:45,374 DEBUG Received response(xid=6): [u'scheduler.53fe9437-6cd0-473f-a3dc-04d1cc490f8b', u'gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4']
2020-12-09 11:31:45,374 DEBUG Sending request(xid=7): GetData(path='/namekox/scheduler.53fe9437-6cd0-473f-a3dc-04d1cc490f8b', watcher=None)
2020-12-09 11:31:45,377 DEBUG Received response(xid=7): ('{"port": 5000, "address": "127.0.0.1"}', ZnodeStat(czxid=990, mzxid=990, ctime=1607484705361, mtime=1607484705361, version=0, cversion=0, aversion=0, ephemeralOwner=72084539296317624, dataLength=38, numChildren=0, pzxid=990))
2020-12-09 11:31:45,378 DEBUG Sending request(xid=8): GetData(path='/namekox/gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4', watcher=None)
2020-12-09 11:31:45,379 DEBUG Received response(xid=8): ('{"port": 80, "address": "127.0.0.1"}', ZnodeStat(czxid=988, mzxid=988, ctime=1607484695498, mtime=1607484695498, version=0, cversion=0, aversion=0, ephemeralOwner=72084539296317623, dataLength=36, numChildren=0, pzxid=988))
2020-12-09 11:32:51,970 DEBUG spawn manage thread handle gateway:namekox_webserver.core.entrypoints.app.server:handle_request(args=(<eventlet.greenio.base.GreenSocket object at 0x10e0cab90>, ('127.0.0.1', 57992)), kwargs={}, tid=handle_request)
2020-12-09 11:32:51,975 DEBUG spawn worker thread handle gateway:dispatch(args=(<Request 'http://127.0.0.1/api/dispatch/' [POST]>,), kwargs={}, context={})
127.0.0.1 - - [09/Dec/2020 11:32:52] "POST /api/dispatch/ HTTP/1.1" 200 237 0.109379
2020-12-09 11:33:14,926 DEBUG Received EVENT: Watch(type=4, state=3, path=u'/namekox')
2020-12-09 11:33:14,927 DEBUG Sending request(xid=9): GetChildren(path='/namekox', watcher=<bound method ChildrenWatch._watcher of <kazoo.recipe.watchers.ChildrenWatch object at 0x10e0cac90>>)
2020-12-09 11:33:14,930 DEBUG Received response(xid=9): [u'gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4']
2020-12-09 11:33:14,931 DEBUG Sending request(xid=10): GetData(path='/namekox/gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4', watcher=None)
2020-12-09 11:33:14,937 DEBUG Received response(xid=10): ('{"port": 80, "address": "127.0.0.1"}', ZnodeStat(czxid=988, mzxid=988, ctime=1607484695498, mtime=1607484695498, version=0, cversion=0, aversion=0, ephemeralOwner=72084539296317623, dataLength=36, numChildren=0, pzxid=988))
^C2020-12-09 11:33:19,047 DEBUG stopping services ['gateway']
2020-12-09 11:33:19,048 DEBUG stopping service gateway entrypoints [gateway:namekox_webserver.core.entrypoints.app.server.WebServer:server, gateway:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:dispatch]
2020-12-09 11:33:19,049 DEBUG wait service gateway entrypoints [gateway:namekox_webserver.core.entrypoints.app.server.WebServer:server, gateway:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:dispatch] stop
2020-12-09 11:33:19,049 DEBUG service gateway entrypoints [gateway:namekox_webserver.core.entrypoints.app.server.WebServer:server, gateway:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:dispatch] stopped
2020-12-09 11:33:19,049 DEBUG stopping service gateway dependencies [gateway:namekox_context.core.dependencies.ContextHelper:ctx, gateway:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk]
2020-12-09 11:33:19,050 DEBUG Sending request(xid=11): Close()
2020-12-09 11:33:19,053 DEBUG Received EVENT: Watch(type=4, state=3, path=u'/namekox')
2020-12-09 11:33:19,054 INFO Closing connection to 127.0.0.1:2181
2020-12-09 11:33:19,054 INFO Zookeeper session lost, state: CLOSED
2020-12-09 11:33:19,054 DEBUG service gateway dependencies [gateway:namekox_context.core.dependencies.ContextHelper:ctx, gateway:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk] stopped
2020-12-09 11:33:19,055 DEBUG services ['gateway'] stopped
2020-12-09 11:33:19,055 DEBUG killing services ['gateway']
2020-12-09 11:33:19,056 DEBUG service gateway already stopped
2020-12-09 11:33:19,056 DEBUG services ['gateway'] killed
```