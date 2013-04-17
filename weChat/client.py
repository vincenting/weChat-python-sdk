# coding=utf-8
__author__ = 'Vincent Ting'

from base import BaseClient
import poster
import urllib2
import time
import re


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

        msg = self._sendMsg(sendTo, {
            'type': 1,
            'content': content
        })
        return msg == 'ok'

    def sendImgMsg(self, sendTo, img):
        """

        :param sendTo:
        :param img:
        :return:
        """
        if type(sendTo) == type([]):
            for _sendTo in sendTo:
                self.sendTextMsg(_sendTo, img)
                time.sleep(2)
            return
        params = {'uploadfile': open(img, "rb")}
        data, headers = poster.encode.multipart_encode(params)
        request = urllib2.Request('http://mp.weixin.qq.com/cgi-bin/uploadmaterial?'
                                  'cgi=uploadmaterial&type=2&token=447813932&t=iframe-uploadfile&'
                                  'lang=zh_CN&formId=file_from_1366206762106', data, headers)
        result = urllib2.urlopen(request)
        find_id = re.compile("\d+")
        file_id = find_id.findall(result.read())[-1]
        msg = self._sendMsg(sendTo, {
            'type': 2,
            'content': '',
            'fid': file_id,
            'fileid': file_id
        })
        return msg == 'ok'