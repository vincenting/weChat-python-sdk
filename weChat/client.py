# coding=utf-8
__author__ = 'Vincent Ting'

from base import BaseClient
import poster
import urllib2
import urllib
import re
import time


class Client(BaseClient):
    def sendTextMsg(self, sendTo, content):
        """
        给用户发送文字内容，成功返回True，使用时注意两次发送间隔，不能少于2s
        :param sendTo:
        :param content:
        :return:
        """
        msg = self._sendMsg(sendTo, {
            'type': 1,
            'content': content
        })
        return msg == 'ok'

    def sendImgMsg(self, sendTo, img):
        """主动推送图片信息
        :param sendTo:
        :param img:图片文件路径
        :return:
        """
        params = {'uploadfile': open(img, "rb")}
        data, headers = poster.encode.multipart_encode(params)
        request = urllib2.Request('http://mp.weixin.qq.com/cgi-bin/uploadmaterial?'
                                  'cgi=uploadmaterial&type=2&token=447813932&t=iframe-uploadfile&'
                                  'lang=zh_CN&formId=file_from_1366206762106', data, headers)
        result = urllib2.urlopen(request)
        find_id = re.compile("\d+")
        file_id = find_id.findall(result.read())[-1]
        time.sleep(1)
        msg = self._sendMsg(sendTo, {
            'type': 2,
            'content': '',
            'fid': file_id,
            'fileid': file_id
        })
        time.sleep(1)
        #删除上传图片
        self.opener.open('http://mp.weixin.qq.com/cgi-bin/modifyfile?oper=del&lang=zh_CN&t=ajax-response',
                         urllib.urlencode({'fileid': file_id,
                                           'token': self.token,
                                           'ajax': 1}))
        return msg == 'ok'