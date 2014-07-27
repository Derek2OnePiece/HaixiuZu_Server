#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# All mongodb operations
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'

import time
import pymongo

from bson.objectid import ObjectId


class DB:
    _server_address = "182.92.105.106"
    _port = 27017
    _db_name = "hxz_server"

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
    
    #==========================================================================
    # user
    # user_map
    #==========================================================================
    def add_shadow_user(self, user_level = 5):
        user = {'created_ts': long(time.time()),
                'user_level': user_level,
                
                'name': None,
                'avatar': None,
                'avatar_tiny': None,
                'photo_wall': None,
                'photo_wall_tiny': None,
                
                'loc_city_id': None,
                'loc_city_name': None,
                'geo_enabled': 0,
                }
        return self.get_collection('user').insert(user)
    
    def get_user_map_by_douban_id(self, douban_id):
        return self.get_collection('user_map')\
            .find_one({'douban_id': douban_id})
    
    def add_douban_id_to_user_map(self, user_id, douban_id):
        # TODO: generate app_id auto increment
        # TODO: check user_id exist fisrt 
        # TODO: make sure user_id been key value
        user_id_map = {'user_id': user_id,
                       'app_id': None,
                       'douban_id': douban_id,
                       'weibo_id': None,
                       'qq_id': None,
                       }
        return self.get_collection('user_map').insert(user_id_map) is not None
    

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


        
        
        
        
        
        
        
        
        
    