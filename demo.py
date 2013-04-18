# coding=utf-8
"""
首先需要在微信公共平台申请帐号 mp.weixin.qq.com
之后才可以使用下事例
"""
__author__ = 'Vincent Ting'

from weChat.client import Client

client = Client(email='xx@gmail.com', password='yourPsw')

#demo  推送文字信息,其中sendto为关注该帐号的某用户的fakeId

client.sendTextMsg('xxxxxxx', 'Hello world')

#demo  推送图片信息,其中sendto为关注该帐号的某用户的fakeId，img为图片的文件路径

client.sendImgMsg('xxxxxxx', 'E:/demo.png')