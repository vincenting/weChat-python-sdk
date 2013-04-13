# coding=utf-8
__author__ = 'Vincent Ting'

from base import BaseClient
import urllib2
import urllib
import json
import time


class Client(BaseClient):
    def sendTextMsg(self, sendTo, content):
        """
        给用户发送文字内容，成功返回True，使用时注意两次发送间隔，不能少于2s
        :param sendTo:
        :param content:
        :return:
        """
        if type(sendTo) == type([]):
            for _sendTo in sendTo:
                self.sendTextMsg(_sendTo, content)
                time.sleep(2)
            return

        self.opener.addheaders = [('Referer', 'http://mp.weixin.qq.com/cgi-bin/singlemsgpage?fromfakeid={0}'
                                              '&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'.format(sendTo))]
        send_url = "http://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN"
        body = (
        ('type', 1), ('content', content), ('error', 'false'), ('token', self.token), ('tofakeid', sendTo), ('ajax', 1))
        try:
            msg = json.loads(self.opener.open(send_url, urllib.urlencode(body), timeout=5).read())['msg']
        except urllib2.URLError:
            return self.sendTextMsg(sendTo, content)
        return msg == 'ok'

