# Createdb
> CREATE DATABASE scheduler_service CHARACTER SET utf8 COLLATE utf8_general_ci;

# Migration
> namekox alembic revision --autogenerate -m "init"
```shell script
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'jobs'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_jobs_next_run_time' on '['next_run_time']'
INFO  [alembic.autogenerate.compare] Detected added table 'locks'
INFO  [alembic.autogenerate.compare] Detected added table 'logs'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_logs_finished' on '['finished']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_logs_run_time' on '['run_time']'
Generating apscheduler/scheduler/alembic/versions/53008ca8b6d8_init.py ...  done
```
> namekox alembic upgrade head
```shell script
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 53008ca8b6d8, init
```

# Running
> config.yaml
```yaml
XMLRPC:
  host: 0.0.0.0
  port: 5000
ZOOKEEPER:
  ping:
    hosts: 127.0.0.1:2181
COMMAND:
  - namekox_sqlalchemy.cli.subcmd.migration:Alembic
DATABASE:
  scheduler: mysql+pymysql://${MYSQL_USER:root}:${MYSQL_PASS:toor}@${MYSQL_HOST:127.0.0.1}:${MYSQL_PORT:3306}/scheduler_service?charset=utf8
APSCHEDULER:
  job_store_cfg:
    pool_pre_ping: true
  job_store_uri: mysql+pymysql://${MYSQL_USER:root}:${MYSQL_PASS:toor}@${MYSQL_HOST:127.0.0.1}:${MYSQL_PORT:3306}/scheduler_service?charset=utf8
```
> namekox run facade
```shell script
2020-12-09 11:31:45,279 DEBUG load container class from namekox_core.core.service.container:ServiceContainer
2020-12-09 11:31:45,281 DEBUG starting services ['scheduler']
2020-12-09 11:31:45,282 DEBUG starting service scheduler entrypoints [scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:pause_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.server.XMLRpcServer:server, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:search_job_logs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_all_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:add_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:reschedule_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:resume_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:modify_job]
2020-12-09 11:31:45,283 DEBUG spawn manage thread handle scheduler:namekox_xmlrpc.core.entrypoints.rpc.server:start_server(args=(), kwargs={}, tid=start_server)
2020-12-09 11:31:45,283 DEBUG service scheduler entrypoints [scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:pause_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.server.XMLRpcServer:server, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:search_job_logs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_all_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:add_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:reschedule_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:resume_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:modify_job] started
2020-12-09 11:31:45,283 DEBUG starting service scheduler dependencies [scheduler:namekox_sqlalchemy.core.dependencies.Database:db, scheduler:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk, scheduler:namekox_apscheduler.core.dependencies.APSchedulerHelper:apscheduler, scheduler:namekox_context.core.dependencies.ContextHelper:ctx]
2020-12-09 11:31:45,333 DEBUG spawn manage thread handle scheduler:namekox_apscheduler.core.dependencies:_run(args=(), kwargs={}, tid=_run)
2020-12-09 11:31:45,334 INFO Scheduler started
2020-12-09 11:31:45,334 DEBUG Looking for jobs to run
2020-12-09 11:31:45,337 INFO Connecting to 127.0.0.1:2181
2020-12-09 11:31:45,338 DEBUG Sending request(xid=None): Connect(protocol_version=0, last_zxid_seen=0, time_out=10000, session_id=0, passwd='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', read_only=None)
2020-12-09 11:31:45,343 INFO Zookeeper connection established, state: CONNECTED
2020-12-09 11:31:45,344 DEBUG Sending request(xid=1): GetChildren(path='/namekox', watcher=<bound method ChildrenWatch._watcher of <kazoo.recipe.watchers.ChildrenWatch object at 0x105597050>>)
2020-12-09 11:31:45,349 DEBUG Received response(xid=1): [u'gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4']
2020-12-09 11:31:45,349 DEBUG Sending request(xid=2): GetData(path='/namekox/gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4', watcher=None)
2020-12-09 11:31:45,355 DEBUG Received response(xid=2): ('{"port": 80, "address": "127.0.0.1"}', ZnodeStat(czxid=988, mzxid=988, ctime=1607484695498, mtime=1607484695498, version=0, cversion=0, aversion=0, ephemeralOwner=72084539296317623, dataLength=36, numChildren=0, pzxid=988))
2020-12-09 11:31:45,356 DEBUG Sending request(xid=3): Exists(path='/namekox', watcher=None)
2020-12-09 11:31:45,358 DEBUG Received response(xid=3): ZnodeStat(czxid=74, mzxid=74, ctime=1606123632647, mtime=1606123632647, version=0, cversion=477, aversion=0, ephemeralOwner=0, dataLength=0, numChildren=1, pzxid=988)
2020-12-09 11:31:45,360 DEBUG Sending request(xid=4): Create(path='/namekox/scheduler.53fe9437-6cd0-473f-a3dc-04d1cc490f8b', data='{"port": 5000, "address": "127.0.0.1"}', acl=[ACL(perms=31, acl_list=['ALL'], id=Id(scheme='world', id='anyone'))], flags=1)
2020-12-09 11:31:45,364 DEBUG Received EVENT: Watch(type=4, state=3, path=u'/namekox')
2020-12-09 11:31:45,366 DEBUG Received response(xid=4): u'/namekox/scheduler.53fe9437-6cd0-473f-a3dc-04d1cc490f8b'
2020-12-09 11:31:45,370 DEBUG Sending request(xid=5): GetChildren(path='/namekox', watcher=<bound method ChildrenWatch._watcher of <kazoo.recipe.watchers.ChildrenWatch object at 0x105597050>>)
2020-12-09 11:31:45,371 DEBUG service scheduler dependencies [scheduler:namekox_sqlalchemy.core.dependencies.Database:db, scheduler:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk, scheduler:namekox_apscheduler.core.dependencies.APSchedulerHelper:apscheduler, scheduler:namekox_context.core.dependencies.ContextHelper:ctx] started
2020-12-09 11:31:45,373 DEBUG services ['scheduler'] started
2020-12-09 11:31:45,376 DEBUG No jobs; waiting until a job is added
2020-12-09 11:31:45,376 DEBUG Received response(xid=5): [u'scheduler.53fe9437-6cd0-473f-a3dc-04d1cc490f8b', u'gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4']
2020-12-09 11:31:45,376 DEBUG Sending request(xid=6): GetData(path='/namekox/scheduler.53fe9437-6cd0-473f-a3dc-04d1cc490f8b', watcher=None)
2020-12-09 11:31:45,378 DEBUG Received response(xid=6): ('{"port": 5000, "address": "127.0.0.1"}', ZnodeStat(czxid=990, mzxid=990, ctime=1607484705361, mtime=1607484705361, version=0, cversion=0, aversion=0, ephemeralOwner=72084539296317624, dataLength=38, numChildren=0, pzxid=990))
2020-12-09 11:31:45,379 DEBUG Sending request(xid=7): GetData(path='/namekox/gateway.8eed80f5-3cd8-44f5-9543-4574e4ada3f4', watcher=None)
2020-12-09 11:31:45,380 DEBUG Received response(xid=7): ('{"port": 80, "address": "127.0.0.1"}', ZnodeStat(czxid=988, mzxid=988, ctime=1607484695498, mtime=1607484695498, version=0, cversion=0, aversion=0, ephemeralOwner=72084539296317623, dataLength=36, numChildren=0, pzxid=988))
2020-12-09 11:32:51,989 DEBUG spawn worker thread handle scheduler:add_job(args=[], kwargs={'seconds': 15, 'trigger': 'interval', 'id': 'project.tasks.ping', 'func': 'project.tasks:ping'}, context={'call_id_stack': ['57cc46d8-b7e4-490f-8f17-3f9a8982e07f']})
2020-12-09 11:32:52,077 INFO Added job "ping" to job store "default"
2020-12-09 11:32:52,078 DEBUG Looking for jobs to run
127.0.0.1 - - [09/Dec/2020 11:32:52] "POST /RPC2 HTTP/1.1" 200 -
2020-12-09 11:32:52,090 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 14.921912 seconds)
2020-12-09 11:33:07,013 DEBUG Looking for jobs to run
2020-12-09 11:33:07,020 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,021 DEBUG Looking for jobs to run
2020-12-09 11:33:07,025 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,025 DEBUG Looking for jobs to run
2020-12-09 11:33:07,029 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,030 DEBUG Looking for jobs to run
2020-12-09 11:33:07,034 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,034 DEBUG Looking for jobs to run
2020-12-09 11:33:07,041 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,042 DEBUG Looking for jobs to run
2020-12-09 11:33:07,046 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,046 DEBUG Looking for jobs to run
2020-12-09 11:33:07,050 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,050 DEBUG Looking for jobs to run
2020-12-09 11:33:07,054 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,054 DEBUG Looking for jobs to run
2020-12-09 11:33:07,060 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,061 DEBUG Looking for jobs to run
2020-12-09 11:33:07,067 DEBUG Next wakeup is due at 2020-12-09 03:33:07+00:00 (in 0.000000 seconds)
2020-12-09 11:33:07,068 DEBUG Looking for jobs to run
2020-12-09 11:33:07,071 INFO Running job "ping (trigger: interval[0:00:15], next run at: 2020-12-09 03:33:07 UTC)" (scheduled at 2020-12-09 03:33:07.062754+00:00)
2020-12-09 11:33:07,084 DEBUG acquire distributed dblock ping succ
2020-12-09 11:33:07,090 DEBUG release distributed dblock ping succ
2020-12-09 11:33:07,090 INFO Job "ping (trigger: interval[0:00:15], next run at: 2020-12-09 03:33:22 UTC)" executed successfully
2020-12-09 11:33:07,107 DEBUG Next wakeup is due at 2020-12-09 03:33:22+00:00 (in 14.931922 seconds)
^C2020-12-09 11:33:14,910 DEBUG stopping services ['scheduler']
2020-12-09 11:33:14,911 DEBUG stopping service scheduler entrypoints [scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:pause_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.server.XMLRpcServer:server, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:search_job_logs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_all_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:add_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:reschedule_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:resume_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:modify_job]
2020-12-09 11:33:14,913 DEBUG wait service scheduler entrypoints [scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:pause_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.server.XMLRpcServer:server, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:search_job_logs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_all_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:add_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:reschedule_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:resume_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:modify_job] stop
2020-12-09 11:33:14,913 DEBUG service scheduler entrypoints [scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:pause_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.server.XMLRpcServer:server, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:search_job_logs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:get_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_all_jobs, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:remove_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:add_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:reschedule_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:resume_job, scheduler:namekox_xmlrpc.core.entrypoints.rpc.handler.XMLRpcHandler:modify_job] stopped
2020-12-09 11:33:14,913 DEBUG stopping service scheduler dependencies [scheduler:namekox_sqlalchemy.core.dependencies.Database:db, scheduler:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk, scheduler:namekox_apscheduler.core.dependencies.APSchedulerHelper:apscheduler, scheduler:namekox_context.core.dependencies.ContextHelper:ctx]
2020-12-09 11:33:14,915 DEBUG Sending request(xid=8): Close()
2020-12-09 11:33:14,916 INFO Scheduler has been shut down
2020-12-09 11:33:14,924 DEBUG Looking for jobs to run
2020-12-09 11:33:14,926 DEBUG Received EVENT: Watch(type=4, state=3, path=u'/namekox')
2020-12-09 11:33:14,929 INFO Closing connection to 127.0.0.1:2181
2020-12-09 11:33:14,929 INFO Zookeeper session lost, state: CLOSED
2020-12-09 11:33:14,940 DEBUG Next wakeup is due at 2020-12-09 03:33:22+00:00 (in 7.075696 seconds)
2020-12-09 11:33:15,573 DEBUG service scheduler dependencies [scheduler:namekox_sqlalchemy.core.dependencies.Database:db, scheduler:namekox_zookeeper.core.dependencies.ZooKeeperHelper:zk, scheduler:namekox_apscheduler.core.dependencies.APSchedulerHelper:apscheduler, scheduler:namekox_context.core.dependencies.ContextHelper:ctx] stopped
2020-12-09 11:33:15,573 DEBUG services ['scheduler'] stopped
2020-12-09 11:33:15,573 DEBUG killing services ['scheduler']
2020-12-09 11:33:15,573 DEBUG service scheduler already stopped
2020-12-09 11:33:15,574 DEBUG services ['scheduler'] killed
```
