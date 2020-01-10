# # -*- coding:utf-8 -*-
# from sms01.utils.public.toolkit import check_user_privileges
# from sms01.utils.public.errno_utils import ServiceStatusCode
# import datetime
# from django.shortcuts import render_to_response
# from sms01.utils.public.response_utils import json_response
# from typing import Optional
# import functools
# from sms01.utils.public.sighauth import SignAuthentication
#
#
# class CheckSession(object):
#     @classmethod
#     def get_username(cls, request):
#         cls.request = request
#         if 'username' in request.session:
#             cls.username = request.session['username']
#             logger.debug('{0}请求{1} '.format(cls.username,
#                                             cls.request.META.get('PATH_INFO')))
#             return cls.username
#         else:
#             return False
#
#     @staticmethod
#     def check_privileges(username, field_name):
#         if check_user_privileges(username, field_name):
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def check_state():  # 查看最后一笔维护记录,比较开始维护时间
#         maintain_obj = NamMaintainLog.objects.order_by('-n_id')[0]
#         if datetime.datetime.now() > maintain_obj.d_start_time and maintain_obj.n_finish_state == 0:
#             return False
#         else:
#             return True
#
#
# def check_state(func):
#     """ 装饰器用于验证是否在维护状态"""
#
#     @functools.wraps(func)
#     def wrapper(self, *args, **kwargs):
#         if CheckSession.check_state():
#             return func(self, *args, **kwargs)
#         else:
#             return render_to_response('close.html')
#
#     return wrapper
#
#
# def check_session(exclude_action: Optional[list] = None):
#     """
#         装饰器用于验证请求是否有session
#         有权限的用户就会把用户名复制给 self.username
#     """
#
#     def deco(func):
#
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             if len(args) >= 2:
#                 _, action, *__ = args
#                 self.username = 'anonymous'
#                 if exclude_action:
#                     if action in exclude_action:
#                         return func(self, *args, **kwargs)
#
#             self.username = CheckSession.get_username(self.request)
#             if self.username:
#                 return func(self, *args, **kwargs)
#             else:
#                 return json_response(ServiceStatusCode.HTTP_NO_SESSION_ERROR)
#
#         return wrapper
#
#     return deco
#
#
# def check_public_authenticated(func):
#     """
#         开放接口认证装饰器
#     """
#
#     @functools.wraps(func)
#     def wrapper(self, *args, **kwargs):
#         try:
#             self.username = SignAuthentication(self.request).auth()
#             return func(self, *args, **kwargs)
#         except Exception as e:
#             return json_response(ServiceStatusCode.REQUEST_ERROR, msg=str(e))
#
#     return wrapper
#
#
# def debug_request(ldap_user: Optional[str] = None):
#     def deco(func):
#         """
#             装饰器用于使用第三方工具测试请求
#         """
#
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             if ldap_user:
#                 self.username = ldap_user
#             else:
#                 self.username = 'Namtest'
#                 return func(self, *args, **kwargs)
#
#         return wrapper
#
#     return deco
#
#
# def check_privileges(field_name, exclude_action: Optional[list] = None):
#     def deco(func):
#         """
#             装饰器用于验证接口请求是否有认证
#             有权限的用户就会把用户名赋值给 self.username
#             且还能验证该用户的权限是否符合
#             exclude_action 表示排除一些接口的认证, 不需要进行session和权限验证的情况
#         """
#
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             if len(args) >= 2:
#                 _, action, *__ = args
#                 self.username = 'anonymous'
#                 if exclude_action:
#                     if action in exclude_action:
#                         return func(self, *args, **kwargs)
#
#             self.username = CheckSession.get_username(self.request)
#             if self.username:
#                 if check_user_privileges(self.username, field_name):
#                     return func(self, *args, **kwargs)
#                 else:
#                     return json_response(ServiceStatusCode.NO_PRIVILEGE_ERROR)
#             else:
#                 return json_response(ServiceStatusCode.HTTP_NO_SESSION_ERROR)
#
#         return wrapper
#
#     return deco
#
#
# def check_html_privileges(html_dir, field_name=None):
#     def deco(func):
#         """
#             装饰器用于验证页面的url请求是否有认证
#             有权限的用户就会把用户名赋值给 self.username
#         """
#
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             if CheckSession.check_state():
#                 self.username = self.session.get('username')
#                 if self.username:
#                     if field_name:
#                         is_admin = True if 'admin/' in html_dir else False
#                         if check_user_privileges(self.username, field_name):
#                             return render_to_response(html_dir, {'username': self.username, 'debug': DEBUG})
#                         else:
#                             if is_admin:
#                                 return render_to_response("admin/403.html")
#                             else:
#                                 return render_to_response("403.html")
#                     else:
#                         return render_to_response(html_dir, {'username': self.username, 'debug': DEBUG})
#                 else:
#                     return render_to_response('login.html')
#             else:
#                 return render_to_response('close.html')
#
#         return wrapper
#
#     return deco
#
