# coding=utf-8
__author__ = 'Vincent Ting'

from base import BaseClient
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
        file_id = self._uploadImg(img)
        time.sleep(1)
        msg = self._sendMsg(sendTo, {
            'type': 2,
            'content': '',
            'fid': file_id,
            'fileid': file_id
        })
        time.sleep(1)
        #删除上传图片
        self._delImg(file_id)
        return msg == 'ok'