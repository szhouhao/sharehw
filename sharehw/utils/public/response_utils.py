# -*- coding: utf-8 -*-

try:
    import json
except ImportError:
    import simplejson as json

from django.utils.translation import ugettext as _
from rest_framework.response import Response

from sharehw.utils.public.errno_utils import ServiceStatusCode


def json_response(status_code=ServiceStatusCode.UNKNOW, data=None, msg=None):
    if data is None:
        data = {}

    if msg:
        if isinstance(msg, dict):
            msg = json.dumps(msg)
        return Response({
            'code': status_code,
            'msg': msg,
            'data': data
        })
    else:
        return Response({
            'code': status_code,
            'msg': _(status_code.message),
            'data': data
        })
