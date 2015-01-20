# -*- coding:utf-8 -*-


from weibo import APIClient
import webbrowser
from httpbasic import httpsmgr
import  urllib, urlparse
APP_KEY = '361868371'
APP_SECRET = '779131656f1b4bb0f0a6487327bb193d'
CALLBACK_URL = 'http://www.example.com/callback'

def getRecent():
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()

	postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','withOfficalFlag':'0','ticket':'','state':'','from':'','userId':'18637124230','passwd':'tmwsdi5s'})
	with httpsmgr('api.weibo.com','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'}) as response:
		query = urlparse.urlparse(response.msg['Location']).query
		code = query.split('=')[1]
		r = client.request_access_token(code)
		access_token = r.access_token
		expires_in = r.expires_in
		client.set_access_token(access_token, expires_in)
		lists = client.statuses.user_timeline.get()
		return lists['statuses'][0]['text']
		
def send(content):
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()

	postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','withOfficalFlag':'0','ticket':'','state':'','from':'','userId':'18637124230','passwd':'tmwsdi5s'})
	with httpsmgr('api.weibo.com','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'}) as response:
		query = urlparse.urlparse(response.msg['Location']).query
		code = query.split('=')[1]
		r = client.request_access_token(code)
		access_token = r.access_token
		expires_in = r.expires_in
		client.set_access_token(access_token, expires_in)
		client.statuses.update.post(status=content)
		
	

if __name__=='__main__':
	#send('0:1:0:0:1')
	print getRecent()