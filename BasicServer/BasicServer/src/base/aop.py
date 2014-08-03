#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# Decorator
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'
__revision__ = '0.1'


import functools

from django.utils import simplejson
from BasicServer.src.base.utils import build_error_response
from BasicServer.src.base.enum import ERR_CODE


def required_login(func=None):
    """
    usage: 
    @required_login
    def func_defination():
        pass

    The decorator assumes that the first arguments of the function 
    is *HttpRequest*, and the session will be used.
    """
    def decorator(func):
        """
        The real decorator that must accept the target function as argument
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]
            
            if request.method == 'POST':
                req_post_data = simplejson.loads(request.raw_post_data)
                if 'token' in req_post_data and 'token' in request.session \
                  and req_post_data['token'] == request.session['token']:
                    return func(*args, **kwargs)

            if request.method == 'GET':
                if 'token' in request.GET and 'token' in request.session \
                  and request.GET['token'] == request.session['token']:
                    return func(*args, **kwargs)
                
            return build_error_response(request, 310, ERR_CODE[310])
        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)

def transform_id(func):
    pass

