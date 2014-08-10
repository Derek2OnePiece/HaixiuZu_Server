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
    def add_shadow_user(self, user_type = 0, user_level = 5):
        user = {'created_ts': long(time.time()),
                'user_type': user_type,
                'user_level': user_level,
                'email': None,
                'password': None,
                'name': None,
                'desc': None,
                'homepage': None,
                'avatar': None,
                'photo_wall': None,
                'photo_wall_tiny': None,
                'loc_city_id': None,
                'loc_city_name': None,
                'updated_ts': long(time.time()),
                'liked_topics': [],
                'commented_topics': [],
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
    
    def get_user_by_user_id(self, user_id):
        return self.get_collection('user').find_one({'_id': user_id})

    def update_user_profile_by_user_id(self, user_id, name, desc,
                                       avatar, avatar_tiny,
                                       photo_wall, photo_wall_tiny):
        return self.get_collection('user')\
            .update({'_id': user_id},
                    {'$set': {'name': name,
                              'desc': desc,
                              'avatar': avatar,
                              'avatar_tiny': avatar_tiny,
                              'photo_wall': photo_wall,
                              'photo_wall_tiny': photo_wall_tiny,
                              'updated_ts': long(time.time()), }})
            
    #==========================================================================
    # topic
    #==========================================================================
    def add_shadow_topic(self, topic_level = 5):
        topic = {'created_ts': long(time.time()),
                'topic_level': topic_level,
                
                'author': None,
                'title': None,
                'content': None,
                'topic_photos': None,
                'topic_photos_tiny': None,
                'burn_ts': None,
                'updated_ts': long(time.time()),
                
                'comment_count': 0,
                'like_users': [],
                'like_count': 0,
                
                'action_ts': long(time.time()),  
                }
        return self.get_collection('topic').insert(topic)
    
    def update_topic_by_topic_id(self, topic_id, author, title, content, 
                                 topic_photos, topic_photos_tiny,
                                 burn_ts):
        return self.get_collection('topic')\
            .update({'_id': topic_id},
                    {'$set': {'author': author,
                              'title': title,
                              'content': content,
                              'topic_photos': topic_photos,
                              'topic_photos_tiny': topic_photos_tiny,
                              'burn_ts': burn_ts,
                              'updated_ts': long(time.time()),
                              'action_ts': long(time.time()), }})
    
    def get_topic_by_topic_id(self, topic_id):
        return self.get_collection('topic').find_one({'_id': topic_id})
      
    #==========================================================================
    # comment
    #==========================================================================


        
        
        
        
        
        
        
        
        
    