#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created: 2014-07-19
#
# All mongodb operations
#
__author__ = 'Derek (Jing Luo), luojing.derek@gmail.com'
__pychecker__ = 'no-callinit no-classattr'

SUCC_CODE = {200: '正确返回', }

ERR_CODE = {300: '用户登陆失败',
            310: '该操作需先登陆',
            700: '缺少必填参数',
            710: '不能识别的参数值 ', }