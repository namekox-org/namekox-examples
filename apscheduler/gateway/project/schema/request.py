# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from marshmallow import Schema, fields


from ..constants import DEFAULT_DISPATCH_TIMEOUT


class RequestCreateSchema(Schema):
    path = fields.String(required=True)
    args = fields.String(missing='[]')
    data = fields.String(missing='{}')
    time = fields.Float(attribute='__timeout__', missing=DEFAULT_DISPATCH_TIMEOUT)
