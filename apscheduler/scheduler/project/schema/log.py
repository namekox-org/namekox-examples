# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from marshmallow import Schema, fields


class JobListSchema(Schema):
    id = fields.String(required=True)
    job_id = fields.String(required=True)
    status = fields.Integer(required=True)
    run_time = fields.DateTime(required=True, allow_none=True)
    finished = fields.DateTime(required=True, allow_none=True)
    duration = fields.Float(required=True, allow_none=True)
    ret_value = fields.String(required=True, allow_none=True)
    exception = fields.String(required=True, allow_none=True)
    traceback = fields.String(required=True, allow_none=True)
