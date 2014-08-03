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


#　import os
import json

from django.http import HttpResponse
from django.utils import simplejson
from bson.objectid import ObjectId
from BasicServer import dbtools
from BasicServer.src.base.utils import build_error_response
from BasicServer.src.base.utils import generate_token
from BasicServer.src.base.enum import ERR_CODE
from BasicServer.src.base.enum import SUCC_CODE
from BasicServer.src.base.aop import required_login


db = dbtools.DB()


# TODO check already login
def login_action(request):
    # receive request data
    req_post_data = None
    if request.method == 'POST':
        req_post_data = simplejson.loads(request.raw_post_data)
    third_party_id = None
    third_party_id_type = None
    if 'third_party_id' in req_post_data:
        third_party_id = req_post_data['third_party_id']
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    if 'third_party_id_type' in req_post_data:
        third_party_id_type = req_post_data['third_party_id_type']
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
    else:
        return build_error_response(request, 710, ERR_CODE[710])
    
    # set session
    if 'token' not in request.session:
        token = generate_token(user_id)
        request.session['token'] = token
    else:
        token = request.session['token']
    
    # success response
    res = {'code': 200,
           'msg': SUCC_CODE[200],
           'uid': str(user_id),
           'third_party_id': third_party_id,
           'third_party_id_type': third_party_id_type,
           'first_login': first_login,
           'token': token,
           }
    return HttpResponse(json.dumps(res), mimetype='application/json')
    
@required_login
def logout_action(request):
    try:
        del request.session['token']
        res = {'code': 200, 'msg': SUCC_CODE[200]}
        return HttpResponse(json.dumps(res), mimetype='application/json')
    except KeyError:
        return build_error_response(request, 710, ERR_CODE[710])

@required_login
def get_user_profile_action(request):
    # receive request data
    user_id = None
    if request.method == 'GET':
        if 'uid' in request.GET:
            user_id = ObjectId(request.GET['uid'])
        else:
            return build_error_response(request, 700, ERR_CODE[700])
    cur_user_profile = db.get_user_by_user_id(user_id)
    if cur_user_profile is not None:
        res = {'code': 200,
               'msg': SUCC_CODE[200],
               'uid': str(cur_user_profile['_id']),
               'name': cur_user_profile['name'],
               'desc': cur_user_profile['desc'],
               'avatar': cur_user_profile['avatar'],
               'avatar_tiny': cur_user_profile['avatar_tiny'],
               'photo_wall': cur_user_profile['photo_wall'],
               'photo_wall_tiny': cur_user_profile['photo_wall_tiny'],
               }
        return HttpResponse(json.dumps(res), mimetype='application/json')
    else:
        return build_error_response(request, 330, ERR_CODE[330])

@required_login
def update_user_profile_action(request):
    # receive request data
    req_post_data = None
    if request.method == 'POST':
        req_post_data = simplejson.loads(request.raw_post_data)
    user_id = None
    if 'uid' in req_post_data and req_post_data['uid'] != '':
        user_id = ObjectId(req_post_data['uid'])
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    
    cur_user_profile = db.get_user_by_user_id(user_id)
    
    # receive optional parameters of user profile
    # name
    # desc
    # avatar
    # avatar_tiny
    # photo_wall
    # photo_wall_tiny
    name = None
    desc = None
    avatar = None
    avatar_tiny = None
    photo_wall = None
    photo_wall_tiny = None
    if 'name' in req_post_data:
        name = req_post_data['name']
    else:
        name = cur_user_profile['name']
    if 'desc' in req_post_data:
        desc = req_post_data['desc']
    else:
        desc = cur_user_profile['desc']
    if 'avatar' in req_post_data:
        avatar = req_post_data['avatar']
    else:
        avatar = cur_user_profile['avatar']
    if 'avatar_tiny' in req_post_data:
        avatar_tiny = req_post_data['avatar_tiny']
    else:
        avatar_tiny = cur_user_profile['avatar_tiny']
    if 'photo_wall' in req_post_data:
        photo_wall = req_post_data['photo_wall']
    else:
        photo_wall = cur_user_profile['photo_wall']
    if 'photo_wall_tiny' in req_post_data:
        photo_wall_tiny = req_post_data['photo_wall_tiny']
    else:
        photo_wall_tiny = cur_user_profile['photo_wall_tiny']
    try:
        db.update_user_profile_by_user_id(
          user_id, name, desc, avatar, avatar_tiny, photo_wall, photo_wall_tiny)
        res = {'code': 200, 
               'msg': SUCC_CODE[200],
               'uid': str(user_id)}
        return HttpResponse(json.dumps(res), mimetype='application/json')
    except:
        return build_error_response(request, 320, ERR_CODE[320])
        
