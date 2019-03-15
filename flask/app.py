from flask import Flask
from flask import render_template
from flask import request
from db import insert_user as is1
from db import insert_contact as ic1
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def main(name=None):
    return render_template('index.html', name=name)

@app.route("/registration")
def new_user():
	if (request.method == 'POST'):
		req=request.args.to_dict()
		is1(user_id=req["user_id"],name=req["name"],pass1=req["pass1"],created_at=datetime.now(),email_id=req["email_id"],date_of_birth=req["date_of_birth"],city=req["city"],state=req["state"])
		ic1(user_id=req["user_id"],phone_no=req["phone_no"])
		return render_template('success.html')
	else:
		return render_template('failure.html')

@app.route("/apoorva")
def hello():
    return "<h2>jQuery and AJAX is FUN!</h2>"

app.run(debug=True,threaded=True)
