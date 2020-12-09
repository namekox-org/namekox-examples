# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from namekox_apscheduler.core.dblock import distributed_lock


# distributed_lock supported:
# apscheduler.triggers.date or apscheduler.triggers.cron


@distributed_lock
def ping(cls):
    return 'pong'
