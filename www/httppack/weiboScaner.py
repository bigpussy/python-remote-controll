# -*- coding:utf-8 -*-


from weibo import APIClient
import webbrowser
from httpbasic import getmgr
import httplib, urllib
APP_KEY = '361868371'
APP_SECRET = '779131656f1b4bb0f0a6487327bb193d'
CALLBACK_URL = 'http://www.example.com/callback'

def list():
	#code = your.web.framework.request.get('abcd1234')
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()
	print url
	page = urllib.urlopen(url)
	html = page.read()
	print html
	print dir(page)
	print page.geturl()
	print page.getcode()
	#https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//www.example.com/callback&response_type=code&client_id=361868371
	#webbrowser.open_new(url)
	# r = client.request_access_token(code)  #f1c58d3da9e7153bd6d2c53b006a2cfe
	# access_token = r.access_token
	# expires_in = r.expires_in
	# print access_token,expires_in
	
if __name__=='__main__':
	list()