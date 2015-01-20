# -*- coding:utf-8 -*-


from httppack import weiboScaner


def control():
	values = weiboScaner.getRecent()
	

	
if __name__ == '__main__':
	print weiboScaner.getRecent()
	