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