# coding=utf-8
__author__ = 'Vincent Ting'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Vincent Ting'

import cookielib
import urllib2
import urllib
import json
import hashlib


class BaseClient(object):
    def __init__(self, email=None, password=None):
        """
        登录公共平台服务器，如果失败将报客户端登录异常错误
        :param email:
        :param password:
        :raise:
        """
        if not email or not password:
            raise ValueError
        self.setOpener()
        url_login = "http://mp.weixin.qq.com/cgi-bin/login?lang=en_US"
        m = hashlib.md5(password[0:16])
        m.digest()
        password = m.hexdigest()
        body = (('username', email), ('pwd', password), ('imgcode', ''), ('f', 'json'))
        try:
            msg = json.loads(self.opener.open(url_login, urllib.urlencode(body), timeout=5).read())
        except urllib2.URLError:
            raise ClientLoginException
        if msg['ErrCode'] not in (0, 65202):
            raise ClientLoginException
        self.token = msg['ErrMsg'].split('=')[-1]

    def setOpener(self):
        """
        设置请求头部信息模拟浏览器
        """
        cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        self.opener.addheaders = [('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
        self.opener.addheaders = [('Accept-Charset', 'GBK,utf-8;q=0.7,*;q=0.3')]
        self.opener.addheaders = [('Accept-Encoding', 'gzip,deflate,sdch')]
        self.opener.addheaders = [('Cache-Control', 'max-age=0')]
        self.opener.addheaders = [('Connection', 'keep-alive')]
        self.opener.addheaders = [('Host', 'mp.weixin.qq.com')]
        self.opener.addheaders = [('Origin', 'mp.weixin.qq.com')]
        self.opener.addheaders = [('Referer', 'http://mp.weixin.qq.com/cgi-bin/loginpage?t=wxm-login&lang=zh_CN')]
        self.opener.addheaders = [('X-Requested-With', 'XMLHttpRequest')]
        self.opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 '
                                                 '(KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22')]


class ClientLoginException(Exception):
    pass