# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from namekox_xmlrpc.core.entrypoints import xmlrpc
from namekox_zookeeper.core.allotter import Allotter
from namekox_xmlrpc.constants import DEFAULT_XMLRPC_PORT
from namekox_apscheduler.core.jobstore import DBJobStore
from namekox_sqlalchemy.core.dependencies import Database
from namekox_context.core.dependencies import ContextHelper
from namekox_zookeeper.core.dependencies import ZooKeeperHelper
from namekox_apscheduler.core.dependencies import APSchedulerHelper
from namekox_zookeeper.constants import DEFAULT_ZOOKEEPER_SERVICE_ROOT_PATH


from .log import LogHelper
from ..models.base import Model


class Scheduler(object):
    name = 'scheduler'

    ctx = ContextHelper()
    db = Database(name, Model, engine_options={'pool_pre_ping': True})
    zk = ZooKeeperHelper(
        name,
        allotter=Allotter(),
        roptions={'port': DEFAULT_XMLRPC_PORT},
        watching=DEFAULT_ZOOKEEPER_SERVICE_ROOT_PATH
    )
    # https://apscheduler.readthedocs.io/en/latest/userguide.html#configuring-the-scheduler
    apscheduler = APSchedulerHelper(jobstores={'default': DBJobStore()})

    @staticmethod
    def get_job_status(job):
        if hasattr(job, 'next_run_time'):
            status = 'running' if job.next_run_time else 'paused'
        else:
            status = 'pending'
        return status

    @xmlrpc.rpc()
    def add_job(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/add_job/",
            "data": "{\"func\":\"project.tasks:ping\",\"trigger\":\"interval\",\"id\":\"project.tasks.ping\",\"seconds\":15}"
        }
        """
        if 'args' in kwargs and isinstance(kwargs['args'], (tuple, list)):
            kwargs['args'] = (self.__class__,) + tuple(kwargs['args'])
        else:
            kwargs['args'] = (self.__class__,)
        self.apscheduler.scheduler.add_job(*args, **kwargs)

    @xmlrpc.rpc()
    def get_job(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/get_job/",
            "data": "{\"job_id\": \"project.tasks.ping\"}"
        }
        """
        job = self.apscheduler.scheduler.get_job(*args, **kwargs)
        job_status = self.get_job_status(job)
        return {'job_id': job.id, 'func': job.func_ref, 'status': job_status}

    @xmlrpc.rpc()
    def get_jobs(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/get_jobs/",
            "data": "{}"
        }
        """
        jobs = self.apscheduler.scheduler.get_jobs(*args, **kwargs)
        return [{'job_id': job.id, 'func': job.func_ref, 'status': self.get_job_status(job)} for job in jobs]

    @xmlrpc.rpc()
    def pause_job(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/pause_job/",
            "data": "{\"job_id\": \"project.tasks.ping\"}"
        }
        """
        self.apscheduler.scheduler.pause_job(*args, **kwargs)

    @xmlrpc.rpc()
    def resume_job(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/resume_job/",
            "data": "{\"job_id\": \"project.tasks.ping\"}"
        }
        """
        self.apscheduler.scheduler.resume_job(*args, **kwargs)

    @xmlrpc.rpc()
    def modify_job(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/modify_job/",
            "data": "{\"job_id\": \"project.tasks.ping\", \"next_run_time\": null}"
        }
        """
        self.apscheduler.scheduler.modify_job(*args, **kwargs)

    @xmlrpc.rpc()
    def reschedule_job(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/reschedule_job/",
            "data": "{\"job_id\": \"project.tasks.ping\", \"trigger\": \"interval\", \"seconds\": 5}"
        }
        """
        self.apscheduler.scheduler.reschedule_job(*args, **kwargs)

    @xmlrpc.rpc()
    def remove_job(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/remove_job/",
            "data": "{\"job_id\": \"project.tasks.ping\"}"
        }
        """
        self.apscheduler.scheduler.remove_job(*args, **kwargs)

    @xmlrpc.rpc()
    def remove_all_jobs(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/remove_all_jobs/",
            "data": "{}"
        }
        """
        self.apscheduler.scheduler.remove_all_jobs()

    @xmlrpc.rpc()
    def search_job_logs(self, *args, **kwargs):
        """
        http://127.0.0.1/api/dispatch/
        -
        POST
        -
        {
            "path": "/scheduler/search_job_logs/",
            "data": "{\"conditions\": {\"job_id\": \"project.tasks.ping\"}, \"offset\": 0, \"limit\": 15}"
        }
        """
        return LogHelper(self).search(*args, **kwargs)
