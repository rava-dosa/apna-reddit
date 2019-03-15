import psycopg2

def insert_user(user_id=None,name=None,pass1=None,created_at=None,email_id=None,date_of_birth=None,city=None,state=None):
	conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
	cur = conn.cursor()
	cur.execute("INSERT INTO USER1(user_id,name,pass,created_at,email_id,date_of_birth,city,state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(user_id,name,pass1,created_at,email_id,date_of_birth,city,state))
	conn.commit()
	return 1
def insert_contact(user_id=None,phone_no=None):
	conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
	cur = conn.cursor()
	cur.execute("INSERT INTO contact_numbers(user_id,phone_no) VALUES(%s,%s)",(user_id,phone_no))
	conn.commit()
	return 1

def insert_subreddit(name=None,subreddit_created_at=None,user_id=None):
	conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
	cur = conn.cursor()
	cur.execute("INSERT INTO subreddit(name,subreddit_created_at,user_id) VALUES(%s,%s,%s)",(name,subreddit_created_at,user_id))
	conn.commit()
	return 1

def insert_post(post_id=None,content=None,post_created_at=None,user_id=None,subreddit_name=None):
	conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
	cur = conn.cursor()
	cur.execute("INSERT INTO subreddit(post_id,content,post_created_at,user_id,subreddit_name) VALUES(%s,%s,%s,%s,%s)",(post_id,content,post_created_at,user_id,subreddit_name))
	conn.commit()
	return 1

def get_password(user_id=None):
	conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
	cur = conn.cursor()
	# cur.execute("Select pass from user1 where user_id='{}'")
	cur.execute("Select pass from user1 where user_id='{}'".format(user_id))
	pass_ret=cur.fetchone()[0]
	conn.commit()
	return pass_ret

def insert_cookie(user_id=None, cookie=None):
	conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
	cur = conn.cursor()
	cur.execute("INSERT INTO cookie(user_id,cookie) VALUES(%s,%s)",(user_id,cookie))
	conn.commit()
	return 1

def get_userid(cookie=None):
	conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
	cur = conn.cursor()
	cur.execute("Select user_id from cookie where user_id='{}'".format(cookie))
	user_ret=cur.fetchone()[0]
	conn.commit()
	return user_ret

