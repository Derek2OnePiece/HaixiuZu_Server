#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# All user operations
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'

#　import os
import json

from django.http import HttpResponse
#　from bson.objectid import ObjectId
from BasicServer import dbtools
from BasicServer.src.base.utils import build_error_response
from BasicServer.src.base.utils import generate_token
from BasicServer.src.base.enum import ERR_CODE
from BasicServer.src.base.enum import SUCC_CODE
from BasicServer.src.base.aop import required_login

db = dbtools.DB()


def login_action(request):
    third_party_id = None
    third_party_id_type = None
    if 'third_party_id' in request.POST:
        third_party_id = request.POST['third_party_id']
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    if 'third_party_id_type' in request.POST:
        third_party_id_type = request.POST['third_party_id_type']
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    
        
    if 'DOUBAN' == third_party_id_type:
        douban_id = third_party_id
        user_id_map = db.get_user_map_by_douban_id(douban_id)
        if user_id_map is None:
            # first login
            first_login = 1
            user_id = db.add_shadow_user()
            if not db.add_douban_id_to_user_map(user_id, douban_id):
                return build_error_response(request, 300, ERR_CODE[300])
        else:
            first_login = 0
            user_id = user_id_map['user_id']
            # success login
            
    else:
        return build_error_response(request, 710, ERR_CODE[710])
    
    # set session
    token = generate_token(user_id)
    request.session['token'] = token
    
    # success response
    res = {'code': 200,
           'msg': SUCC_CODE[200],
           'uid': user_id,
           'third_party_id': third_party_id,
           'third_party_id_type': third_party_id_type,
           'first_login': first_login,
           'token': token,
           }
    return HttpResponse(json.dumps(res), )
    
@required_login
def logout_action(request):
    try:
        del request.session['token']
        res = {'code': 200, 'msg': SUCC_CODE[200]}
        return HttpResponse(json.dumps(res), )
    except KeyError:
        return build_error_response(request, 710, ERR_CODE[710])
