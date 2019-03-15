from flask import Flask
from flask import render_template
from flask import request
from db import insert_user as is1
from db import insert_contact as ic1
from db import get_password as gp1
from db import insert_cookie as ic1
from db import get_userid as gu1
from db import delete_cookie as dc1
from datetime import datetime
from uuid import uuid1

app = Flask(__name__)

@app.route("/")
def main(name=None):
    return render_template('index.html', name=name)

@app.route("/registration",methods=['GET', 'POST'])
def new_user():
    if (request.method == 'POST'):
        req=request.form.to_dict()
        is1(user_id=req["user_id"],name=req["name"],pass1=req["pass1"],created_at=datetime.now(),email_id=req["email_id"],date_of_birth=req["date_of_birth"],city=req["city"],state=req["state"])
        ic1(user_id=req["user_id"],phone_no=req["phone_no"])
        return render_template('success.html')
    else:
        return render_template('failure.html')

@app.route("/apoorva",methods=['GET', 'POST'])
def hello():
    # import pdb;pdb.set_trace()
    req=request.form.to_dict()
    print(req["podu"])
    return "<h2>jQuery and AJAX is FUN!</h2>"


@app.route("/testreg")
def test_reg():
    return render_template('registration.html')
    # return "poijhgf"

@app.route("/testpost")
def Post_cmnt():
    return render_template('create_post.html')

@app.route("/createpost",methods=['GET', 'POST'])
def recv_post_cmnt():
    if (request.method == 'POST'):
        # import pdb;pdb.set_trace()
        req=request.form.to_dict()
        print(req["post"])
        return "<h>Apoorva</h>"

@app.route("/login",methods=['POST'])
def login():
	req = request.form.to_dict()
	user_id=req["user_id"]
	password=req["pass1"]
	if(user_id is None):
		return "<h>Empty user_id</h>"
	else:
		pass_database=gp1(user_id)
		if(pass_database is None):
			return "<h>User id not found</h>"
		else:
			if(pass_database==password):
				cookie=str(uuid1())
				ret=ic1(user_id,cookie)
				return cookie
			else:
				return "<h>wrong password</h>"

@app.route("/logout",methods=["POST"])
def logout():
	req = request.headers.to_dict()
	cookie=req["cookie"]
	dc1(cookie)
	return "<h>Logged out</h>"

app.run(debug=True,threaded=True)

