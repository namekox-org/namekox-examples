# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from marshmallow import Schema, fields


class RequestCreateSchema(Schema):
    path = fields.String(required=True)
    args = fields.String(missing='[]')
    data = fields.String(missing='{}')
    time = fields.Integer(attribute='__timeout__', missing=None, allow_none=True)
