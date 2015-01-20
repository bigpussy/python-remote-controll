# -*- coding:utf-8 -*-


from weibo import APIClient
import webbrowser
from httpbasic import httpsmgr
import httplib, urllib
APP_KEY = '361868371'
APP_SECRET = '779131656f1b4bb0f0a6487327bb193d'
CALLBACK_URL = 'http://www.example.com/callback'

def list():
	#code = your.web.framework.request.get('abcd1234')
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()

	postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','withOfficalFlag':'0','ticket':'','state':'','from':'','userId':'18637124230','passwd':'tmwsdi5s'})
	with httpsmgr('api.weibo.com','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'}) as resp:
		
	#https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//www.example.com/callback&response_type=code&client_id=361868371
	#https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//www.example.com/callback&response_type=code&client_id=361868371
	#webbrowser.open_new(url)
	# r = client.request_access_token(code)  #f1c58d3da9e7153bd6d2c53b006a2cfe
	# access_token = r.access_token
	# expires_in = r.expires_in
	# print access_token,expires_in

	
if __name__=='__main__'
	print 'aa'