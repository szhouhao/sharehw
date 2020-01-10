# -*- coding: utf-8 -*-
import sys
from kkconst import BaseConst, ConstIntField
from django.utils.translation import ugettext_lazy as _


class BaseStatusCode(BaseConst):
    class Meta:
        allow_duplicated_value = False


class StatusCodeField(ConstIntField):
    def __init__(self, status_code, message=''):
        ConstIntField.__init__(status_code, verbose_name=message)
        self.message = message

class ServiceStatusCode(BaseStatusCode):
    UNKNOW = StatusCodeField(-999, _("未知返回"))
    COMING_SOON = StatusCodeField(-2, _("敬请期待"))
    UNAVAILABLE = StatusCodeField(-1, _("服务不可用"))
    REQUEST_SUCCESS = StatusCodeField(0, _("请求成功"))
    REQUEST_ERROR = StatusCodeField(1, _("请求错误或超时"))
    FILE_IO_ERROR = StatusCodeField(2, _("文件操作错误"))
    NO_PARAMS = StatusCodeField(3, _("缺少参数"))
    PARAMS_ERROR = StatusCodeField(4, _("参数错误"))
    IN_PROGRESS_ERROR = StatusCodeField(5, _("任务执行中"))
    NO_SUPPORTED_ERROR = StatusCodeField(6, _("无法找到对应接口"))
    NO_PRIVILEGE_ERROR = StatusCodeField(7, _("权限不足"))
    HTTP_NO_SUPPORTED_ERROR = StatusCodeField(8, _("不支持此HTTP请求"))
    HTTP_NO_SESSION_ERROR = StatusCodeField(9, _("未认证请求,请登录后再试!"))


class AuthStatusCode(BaseStatusCode):
    AUTH_ERROR = StatusCodeField(2001, _("authkey验证失败"))
    AUTH_INVALID_ERROR = StatusCodeField(2002, _("签名无效(invalid sign)"))
    AUTH_SECRETID_NOT_FOUND = StatusCodeField(2003, _("缺少secretid参数(secretid not found)"))
    AUTH_TIMESTAMP_NOT_FOUND = StatusCodeField(2004, _("缺少timestamp参数(timestamp not found)"))
    AUTH_SIGN_NOT_FOUND = StatusCodeField(2005, _("缺少sign参数(sign not found)"))
    AUTH_REQUEST_EXPIRED = StatusCodeField(2006, _("请求已过期(request expired)"))

