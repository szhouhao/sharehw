# -*- coding: utf-8 -*-
from typing import Optional, Any


class APIActionClass(object):
    def __init__(self, cls=None, get_api: Optional[dict] = None, post_api: Optional[dict] = None):
        self.cls = cls
        self.get_api_dict = get_api if get_api else {}
        self.get_post_dict = post_api if post_api else {}

    def get_func(self, uri: str) -> Any:
        func = self.get_api_dict.get(uri)
        if func:
            return getattr(self.cls, func)
        else:
            raise AssertionError('无法找到该接口')

    def post_func(self, uri: str) -> Any:
        func = self.get_post_dict.get(uri)
        if func:
            return getattr(self.cls, func)
        else:
            raise AssertionError('无法找到该接口')
