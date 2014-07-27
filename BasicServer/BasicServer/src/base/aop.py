#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# All user operations
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'
__revision__ = '0.1'

import functools

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
        real decorator that must accept the target function as argument
        """
        @functools.wraps(func)
        def wrapper(*args,  **kwargs):
            """
            use func's doc string
            """
            import inspect
            
            arg_spec = inspect.getargspec(func)
            request = args[0]
            session = request.session
            
            # TODO: check whether or not contains key 'token'
            for key in kwargs:
                if key == 'token' and kwargs[key] != session['token']:
                    return build_error_response(request, 310, ERR_CODE[310])
            for i, value in enumerate(args):
                if arg_spec.args[i] and arg_spec.args[i] == 'token'\
                  and value != session['token']:
                    return build_error_response(request, 310, ERR_CODE[310])
            
            return func(*args,  **kwargs)
        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)

def transform_id(func):
    pass

