#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# All mongodb operations
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'

import pymongo
import time

from datetime import datetime
from bson.objectid import ObjectId


class DB:
    _server_address = "115.28.130.170"
    _port = 27017
    _db_name = "server"

    def __init__(self, address=_server_address, port=_port):
        self.connection = pymongo.Connection(address, port)
        # self.setup_index()

    #==========================================================================
    # base operations
    #==========================================================================
    def get_db(self, name=_db_name):
        return self.connection[name]

    def get_collection(self, name):
        return self.get_db()[name]
    '''
    def setup_index(self):
        """
        ensure index according to data model
        should be called only once before any of the methods is invoked
        """
        self.get_collection('query').ensure_index([('project_id', 1),
                                                     ('user_id', 1),
                                                     ('timestamp',
                                                      pymongo.DESCENDING)])
        self.get_collection('query').ensure_index([('projcet_id', 1), ('user_id', 1),
                                                   ('keyword', 1)], unique=True)
        self.get_collection('notification').ensure_index([('project_id', 1),
                                                          ('user_id', 1),
                                                          ('type', 1),
                                                          ('recommend_help_type', 1),
                                                          ('timestamp',
                                                           pymongo.DESCENDING)])
    '''
    #==========================================================================
    # user
    #
    #    _id
    #    email           || int       ||
    #    password        || int       ||
    #    name            || string    || 昵称
    #    user_type       || string    || 0-学生；1-校友；2-教师
    #    is_admin        || int       || 默认0；0-普通用户；1-管理员
    #    avater_sub_url  || string    || 头像文件相对路径
    #    phone           || string    ||
    #    sid             || string    || 学号 or 教师号
    #    gender          || int       || 默认0；0-male；1-female
    #    signature       || string    || 个性签名
    #    reg_timestamp   || long      || 注册时间
    #
    #==========================================================================
    
    def add_user(self, 
                 email, 
                 password, 
                 name, 
                 user_type, 
                 is_admin = 0,
                 avatar_sub_url = r'', 
                 phone = r'', 
                 sid = r'',
                 gender = 0, 
                 signature = r''):
        user = {'email':email,
                'password':password,
                'name': name,
                'user_type': user_type, 
                'is_admin': is_admin, 
                'avatar_sub_url': avatar_sub_url, 
                'phone': phone,
                'sid': sid,
                'gender': gender,
                'signature': signature,
                 'reg_timestamp':  long(time.time()), }
        return self.get_collection('user').insert(user)

    def check_user_exist_by_email(self, email):
        return self.get_collection('user')\
                 .find_one({'email': email}) is not None

    def login(self, email, password):
        return self.get_collection('user').find_one({'email': email, 
                                                     'password': password})
    

    #==========================================================================
    # topic
    #
    #    _id
    #    news_type                || int       || 0-article；1-video
    #    title                    || string    ||
    #    abstract                 || string    || 摘要 less than 20 words
    #    author                   || string    || 用于显示的作者
    #    module                   || int       || 版块id > 0
    #    created_timestamp        || long      || 
    #    last_modify_timestamp    || long      ||
    #    pub_timestamp            || long      ||
    #    pub_status               || int       || 默认0；0-未发布； 1-发布
    #    is_delete                || int       || 默认0；0-不删除； 1-删除
    #    delete_timestamp         || long      ||
    #    body                     || string    || 
    #    inner_pic_sub_url        || string    || 文章配图的链接地址
    #    video_target_url         || string    ||
    #
    #==========================================================================
   
      
    #==========================================================================
    # comment
    #
    #    _id                
    #    user_id            || ObjectId      || 发布者id
    #    news_id            || ObjectId      || 关联的新闻id
    #    pub_timestamp      || long          || 发布时间
    #    msg                || string        ||
    #
    #==========================================================================


        
        
        
        
        
        
        
        
        
    