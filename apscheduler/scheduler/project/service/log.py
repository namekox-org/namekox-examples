# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import sqlalchemy as sa


from namekox_sqlalchemy.core.condition import DynamicCondition


from .. import models, schema


class LogHelper(object):
    def __init__(self, service):
        self.service = service

    def search(self, conditions=None, offset=None, limit=None):
        conditions = {} if conditions is None else conditions
        conditions = DynamicCondition(models, models.Log).as_orm_condition(conditions)
        query = self.service.db.query(models.Log).filter(conditions)
        query = query.order_by(sa.desc(models.Log.run_time))
        total = query.count()
        query = query if offset is None and limit is None else query.offset(offset).limit(limit)
        data = []
        for role in query:
            role_data = schema.JobListSchema(strict=True).dump(role).data
            data.append(role_data)
        return data if offset is None and limit is None else {'total': total, 'records': data}
