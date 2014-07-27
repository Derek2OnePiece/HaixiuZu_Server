"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

import unittest

from django.http import HttpRequest
from django.http import HttpResponse

from CoSeeking.aop import required_login, transform_id

class AOPTest(unittest.TestCase):
    def test_login(self):
        @required_login(err_msg="{'msg':0}")
        def login(request):
            return HttpResponse("{'msg':1}")
        request=HttpRequest()
        request.session={}
        self.assertEqual("{'msg':0}", login(request).content)
        request.session['user_id']='qiao'
        self.assertEqual("{'msg':1}", login(request).content)

    def test_creator(self):
        @required_login(creator=True, err_msg="creator not found")
        def creator(request):
            return HttpResponse("{'msg':1}")
        request=HttpRequest()
        request.session={}
        request.session['user_id']='qiao'
        self.assertEqual("creator not found", creator(request).content)
        request.session['creator']='qiao'
        self.assertEqual("{'msg':1}", creator(request).content)

    def test_transform_id(self):
        from pymongo.objectid import ObjectId
        @transform_id
        def use_id(user_id, project_id = '4d1444f29b4cea5182000000', other = True):
            self.assertTrue(isinstance(user_id, basestring))
            self.assertTrue(isinstance(project_id, ObjectId))
            self.assertTrue(isinstance(other, bool))
        use_id('qiaomuf@gmail.com', '4d1444f29b4cea5182000000', True)
        use_id('4d1444f29b4cea5182000000', ObjectId('4d1444f29b4cea5182000000'))


if __name__=="__main__":
    unittest.main()
