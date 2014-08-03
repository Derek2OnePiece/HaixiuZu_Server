#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# All topic operations
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'
__revision__ = '0.1'


import json

from django.http import HttpResponse
from django.utils import simplejson
from bson.objectid import ObjectId
from BasicServer import dbtools
from BasicServer.src.base.utils import build_error_response
from BasicServer.src.base.enum import ERR_CODE
from BasicServer.src.base.enum import SUCC_CODE
from BasicServer.src.base.aop import required_login


db = dbtools.DB()


@required_login
def pub_topic_action(request):
    # receive request data
    req_post_data = None
    if request.method == 'POST':
        req_post_data = simplejson.loads(request.raw_post_data)
    
    # required parameters
    user_id = None
    title = None
    content = None
    if 'uid' in req_post_data:
        user_id = ObjectId(req_post_data['uid'])
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    if 'title' in req_post_data:
        title = req_post_data['title']
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    if 'content' in req_post_data:
        content = req_post_data['content']
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    
    # optional parameters
    topic_photos = None
    topic_photos_tiny = None
    burn_ts = None
    if 'topic_photos' in req_post_data:
        topic_photos = req_post_data['topic_photos']
    if 'topic_photos_tiny' in req_post_data:
        topic_photos_tiny = req_post_data['topic_photos_tiny']
    if 'burn_timestamp' in req_post_data:
        burn_ts = req_post_data['burn_timestamp']
    
    # first add shadow topic
    topic_id = db.add_shadow_topic()
    # TODO: add exception
    
    # second update topic detail
    author_profile = db.get_user_by_user_id(user_id)
    author = {'uid': author_profile['_id'],
              'name': author_profile['name'],
              'avatar': author_profile['avatar'],
              'avatar_tiny': author_profile['avatar_tiny'],
              'user_level': author_profile['user_level'], }
    try:
        db.update_topic_by_topic_id(
          topic_id, author, title, content, 
          topic_photos, topic_photos_tiny, burn_ts)
        res = {'code': 200, 
               'msg': SUCC_CODE[200],
               'topic_id': str(topic_id), }
        return HttpResponse(json.dumps(res), mimetype='application/json')
    except:
        return build_error_response(request, 400, ERR_CODE[400])  

@required_login
def update_topic_action(request):
    # receive request data
    req_post_data = None
    if request.method == 'POST':
        req_post_data = simplejson.loads(request.raw_post_data)
    
    # required parameters
    topic_id = None
    if 'topic_id' in req_post_data:
        topic_id = ObjectId(req_post_data['topic_id'])
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    
    cur_topic_detail = db.get_topic_by_topic_id(topic_id)
    title = cur_topic_detail['title']
    content = cur_topic_detail['content']
    if 'title' in req_post_data:
        title = req_post_data['title']
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    if 'content' in req_post_data:
        content = req_post_data['content']
    else:
        return build_error_response(request, 700, ERR_CODE[700])
    
    # optional parameters
    topic_photos = None
    topic_photos_tiny = None
    if 'topic_photos' in req_post_data:
        topic_photos = req_post_data['topic_photos']
    if 'topic_photos_tiny' in req_post_data:
        topic_photos_tiny = req_post_data['topic_photos_tiny']





