#coding: utf-8
__author__ = 'xiewen'


import unittest
import requests

class TestInitial(unittest.TestCase):

    def setUP(self):
        """

        :return:
        """
        print('i am start')

    def tearDown(self):
        """

        :return:
        """
        print('i am down')

    def test_initial_header(self):
        """

        :return:
        """
        h = requests.utils.default_headers()  # 默认产生的user-agent是 'python-requests/version-num' 这个不太好
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        h.update(user_agent)
        return h