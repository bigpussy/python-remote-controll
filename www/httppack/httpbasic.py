# -*- coding:utf-8 -*-

import httplib, urllib


class getmgr:
	def __init__(self, baseurl, suburl, port=80, **params):
		self.__baseurl = baseurl
		print baseurl
		self.__suburl = suburl
		self.__port =port
		self.__params = urllib.urlencode(params)
		self.__httpclient = None
		
	def __enter__(self):
		self.__httpclient = httplib.HTTPConnection(self.__baseurl, self.__port, timeout=30)
		self.__httpclient.request('GET', self.__suburl, self.__params)
		response = self.__httpclient.getresponse()
		return response
		
	def __exit__(self, mytype, myvalue, tb):
		if self.__httpclient:
			self.__httpclient.close()
			
class postmgr:
	def __init__(self, baseurl, suburl, port=80, params = {}, headers = {}):
		self.__baseurl = baseurl
		self.__suburl = suburl
		self.__port =port
		self.__params = urllib.urlencode(params)
		self.__headers = headers
		self.__httpclient = None

	def __enter__(self):
		
		self.__httpclient = httplib.HTTPConnection(self.__baseurl, self.__port, timeout=30)
		self.__httpclient.request('POST', self.__suburl, self.__params, self.__headers)
		response = self.__httpclient.getresponse()
		return response
	
	def __exit__(self, mytype, myvalue, tb):
		if self.__httpclient:
			self.__httpclient.close()
