# coding=utf-8
__author__ = 'Vincent Ting'

from base import BaseClient


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
        """
        主动推送图片信息
        :param sendTo:
        :param img:图片文件路径
        :return:
        """
        file_id = self._uploadImg(img)
        msg = self._sendMsg(sendTo, {
            'type': 2,
            'content': '',
            'fid': file_id,
            'fileid': file_id
        })
        self._delImg(file_id)
        return msg == 'ok'

    def sendAppMsg(self, sendTo, title, content, img, digest='', sourceurl=''):
        """
        主动推送图文
        :param sendTo:
        :param title: 标题
        :param content: 正文，允许html
        :param img:
        :param digest: 摘要
        :param sourceurl: 来源地址
        :return:
        """
        file_id = self._uploadImg(img)
        self._addAppMsg(title, content, file_id, digest, sourceurl)
        app_msg_id = self._getAppMsgId()
        msg = self._sendMsg(sendTo, {
            'type': 10,
            'fid': app_msg_id,
            'appmsgid': app_msg_id
        })
        self._delImg(file_id)
        self._delAppMsg(app_msg_id)
        return msg == 'ok'