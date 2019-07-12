#!/usr/bin/python
#coding=utf-8

import os
import sys
import json
import urllib2
import requests

class Ding():
	def __init__(self):
		self.url = 'https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'		# 钉钉机器人webhook
		self.rebot_url = 'http://www.tuling123.com/openapi/api'
		self.header = {"Content-Type":"application/json"}
		self.time = sys.argv[1]	# 获取脚本传递的参数，判断是上午还是下午
	def weather(self,day):
		if day == 'today':
			info = '今天北京天气'
		elif day == 'tomorrow':
			info = '明天北京天气'
		apikey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"		# 图灵机器人apikey
		data = {"key":apikey,"info":info,"userid":"abcd123456"}		# userid自定义即可
		jsondata = json.dumps(data)
		request = urllib2.Request(self.rebot_url,data = jsondata,headers = self.header)
		response = urllib2.urlopen(request)
		result = json.loads(response.read())['text'].replace(':',' ').replace(',',' ')
		return result
	def send(self):
		if self.time == '0':	# 0为上午，1为下午  自己使用，所以不做错误判断处理，计划任务自己传参，非0即为下午
			weather = self.weather('today').encode("utf-8")
			data = {
				"msgtype": "markdown",
				"markdown": {
					"title": "小伙伴打卡咯",
					"text": "### 小伙伴们早上好！上班打卡了\n" +
							">%s\n\n"%(weather) +
							">**1、请链接公司wifi，开启钉钉进行打卡。**\n\n" +
							">**2、如有外出的同事请打外勤卡。**\n\n" +
							">**3、如有忘记打卡的小伙伴们，请当天补卡。**\n\n" +
							">![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562911938757&di=8417c0896cd48969df5624b1d0963db2&imgtype=0&src=http%3A%2F%2Fww1.sinaimg.cn%2Fwap720%2F005VH4DZjw1f57ulwhkxxj30tm0hswfl.jpg)\n"
				},
			}
		else:
			weather = self.weather('tomorrow').encode("utf-8")
			data = {
				"msgtype": "markdown",
				"markdown": {
					"title": "小伙伴打卡咯",
					"text": "### 下班前温馨提示：下班打卡了\n" +
							">%s\n\n"%(weather) +
							">**1、请大家别忘了登录钉钉打卡下班。**\n\n" +
							">**2、离开公司请关闭电脑、切断电源、带走个人贵重物品。**\n\n" +
							">**3、18:00点以后离开公司的每位员工请随手关门。**\n\n" +
							">![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562912026144&di=5aff432875a5cfd03261f1633926e19c&imgtype=jpg&src=http%3A%2F%2Fphotocdn.sohu.com%2F20151230%2Fmp51266561_1451408740159_28.jpeg)\n"
				},
			}
		jsondata = json.dumps(data)
		request = urllib2.Request(self.url,data = jsondata,headers = self.header)
		response = urllib2.urlopen(request)
		result = response.read()
		return result
a = Ding()
a.send()
