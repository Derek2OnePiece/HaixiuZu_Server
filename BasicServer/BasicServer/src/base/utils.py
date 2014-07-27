#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# Utils
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'
__revision__ = '0.1'

import json
import time
import hashlib

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def build_error_response(request, err_code, err_msg):
    return HttpResponse(json.dumps({'code': err_code, 'msg': err_msg }))

def get_md5(src):
    base_md5 = hashlib.md5()
    base_md5.update(src)
    return base_md5.hexdigest()

def generate_token(user_id):
    return get_md5(str(user_id) + str(time.time()))

