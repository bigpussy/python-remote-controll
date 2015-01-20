# -*- coding:utf-8 -*-


from flask import Flask, request, render_template
import business
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def viewlist():
	pageNo = 1
	if 'pageNo' in request.args:
		pageNo = int(request.args['pageNo'])

	pageSize = 10
	if 'pageSize' in request.args:
		pageSize = int(request.args['pageSize'])
	
	processedFlag = 2
	if 'processedFlag' in request.args:
		processedFlag = int(request.args['processedFlag'])
	if processedFlag == 2:
		sheets = business.listSheets(pageNo, pageSize)
	else:
		sheets = business.listSheets(pageNo, pageSize,processedFlag=int(request.args['processedFlag']))

	return render_template('acceptlist.html',sheets=sheets,pageNo=pageNo,pageSize=pageSize,processedFlag=processedFlag)
	
@app.route('/deleteSheet', methods=['GET', 'POST'])
def deleteSheet():
	id = 0
	if 'id' in request.args:
		id = int(request.args['id'])
	print type(id)
	business.deleteSheet(int(id))
	return viewlist()

@app.route('/userlist', methods=['GET', 'POST'])
def userlist():
	opt = 'list'
	if 'opt' in request.args:
		opt = request.args['opt']
	if 'update'==opt:
		id = int(request.args['id'])
		name = request.args['name']
		email = request.args['email']
		business.updateUser(id,name,email)
	if 'del'==opt:
		id = int(request.args['id'])
		business.deleteUser(id)
	if 'add'==opt:
		name = request.args['name']
		email = request.args['email']
		business.addUser(name,email)
		
	users = business.listUsers()
	return render_template('userlist.html', users=users)
	

@app.route('/setting', methods=['GET', 'POST'])
def setting():
	work1 = business.getWork(1)
	work2 = business.getWork(2)
	return render_template('setting.html',work1=work1,work2=work2)
	
@app.route('/setwork', methods=['GET', 'POST'])
def setWork():
	if 'work1' in request.args:
		business.setWork(1,int(request.args['work1']))
	if 'work2' in request.args:
		business.setWork(2,int(request.args['work2']))
	return ''
	

	
if __name__ == '__main__':
	business.startWork1()
	business.startWork2()
	business.startWork3()
	app.run(host='0.0.0.0', port=9898)
	