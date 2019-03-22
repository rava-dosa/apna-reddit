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
    cur.execute("INSERT INTO post(post_id,content,post_created_at,user_id,subreddit_name) VALUES(%s,%s,%s,%s,%s)",(post_id,content,post_created_at,user_id,subreddit_name))
    conn.commit()
    return "Success"

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
    # import pdb;pdb.set_trace()
    cur.execute("Select user_id from cookie where cookie='{}'".format(cookie))
    user_ret=cur.fetchone()[0]
    conn.commit()
    return user_ret

def delete_cookie(cookie=None):
    conn = psycopg2.connect(dbname="mydb", user="myuser", password="mypass",host="localhost")
    cur = conn.cursor()
    cur.execute("DELETE from cookie where cookie='{}'".format(cookie))
    conn.commit()
    return 1

def insert_comment(comment_id=None, user_id=None, comment_content=None,created_at=None,parent_id=None,post_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("INSERT INTO comment(comment_id,user_id,comment_content,created_at,parent_id,post_id) VALUES(%s,%s,%s,%s,%s,%s)",(comment_id,user_id,comment_content,created_at,parent_id,post_id))
	con.commit()
	return 1


def get_comment(comment_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("SELECT comment_content,comment_id from comment where comment_id='{}'".format(comment_id))
	data=cur.fetchall()
	con.commit()
	return data
def get_comment_liked(comment_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("SELECT user_id from cmt_liked where comment_id='{}'".format(comment_id))
	data=cur.fetchall()
	con.commit()
	return data
def get_comment_disliked(comment_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("SELECT user_id from cmt_disliked where comment_id='{}'".format(comment_id))
	data=cur.fetchall()
	con.commit()
	return data

def get_post(post_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("SELECT content from post where post_id='{}'".format(post_id))
	# data=cur.fetchone()[0]
	data=cur.fetchall()
	con.commit()
	return data

def get_upvote_downvote_by_post(subreddit=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("select post.post_id, post.content from subreddit, post where post.subreddit_name = subreddit.name and subreddit.name='{}' order by post.post_created_at desc".format(subreddit))
	post_ids = cur.fetchall()
	POSTS = dict()
	for i,text  in post_ids:
		POSTS[i] = dict()
		Num_likes = 0
		Num_dislikes = 0
		try:
			cur.execute("select count(*) as post_liked from post_liked where post_id='{}' group by post_id".format(i))
			Num_likes = cur.fetchone()[0]
		except:
			pass
		
		try:
			cur.execute("select count(*) as post_disliked from post_disliked where post_id='{}' group by post_id".format(i))
			Num_dislikes = cur.fetchone()[0]
		except:
			pass
		
		POSTS[i]["likes"] = Num_likes
		POSTS[i]["dislikes"] = Num_dislikes
		POSTS[i]["text"] = text
	return POSTS

def create_subreddit(name1=None,subreddit_created_at=None,user_id=None):
    con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
    cur=con.cursor()
    cur.execute("INSERT INTO subreddit (name,subreddit_created_at,user_id) VALUES(%s,%s,%s)",(name1,subreddit_created_at,user_id))
    con.commit()
    return 1

def get_subreddit():
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("select name,user_id from subreddit order by subreddit_created_at desc");
	ret=cur.fetchall()
	con.commit()
	return ret;

def insert_cmt_liked(user_id=None,comment_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	liked = 0
	try:
		# Check if like already exist
		cur.execute("select * from cmt_liked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from cmt_liked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
		liked = 0
	except:
		# otherwise insert into table
		cur.execute("INSERT INTO cmt_liked(user_id,comment_id) VALUES(%s,%s)",(user_id,comment_id))
		liked = 1
	try:
		# Check if dislike already exist then remove it
		cur.execute("select * from cmt_disliked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from cmt_disliked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
	except:
		pass
	con.commit()
	return liked

def insert_cmt_disliked(user_id=None,comment_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	disliked = 0
	try:
		# Check if dislike already exist
		cur.execute("select * from cmt_disliked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from cmt_disliked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
		disliked = 0
	except:
		# otherwise insert into table
		cur.execute("INSERT INTO cmt_disliked(user_id,comment_id) VALUES(%s,%s)",(user_id,comment_id))
		disliked = 1
	try:
		# Check if like already exist then remove it
		cur.execute("select * from cmt_liked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from cmt_liked where user_id='{}' and comment_id='{}'".format(user_id, comment_id))	
	except:
		pass
	con.commit()
	return disliked

def insert_post_liked(user_id=None, comment_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	liked = 0
	try:
		# Check if like already exist
		cur.execute("select * from post_liked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from post_liked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
		liked = 0
	except:
		# otherwise insert into table
		cur.execute("INSERT INTO post_liked(user_id,post_id) VALUES(%s,%s)",(user_id,comment_id))
		liked = 1
	try:
		# Check if dislike already exist then remove it
		cur.execute("select * from post_disliked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from post_disliked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
	except:
		pass
	con.commit()
	return liked

def insert_post_disliked(user_id=None, comment_id=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	disliked = 0
	try:
		# Check if dislike already exist
		cur.execute("select * from post_disliked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from post_disliked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
		disliked = 0
	except:
		# otherwise insert into table
		cur.execute("INSERT INTO post_disliked(user_id,post_id) VALUES(%s,%s)",(user_id,comment_id))
		disliked = 1
	try:
		# Check if like already exist then remove it
		cur.execute("select * from post_liked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
		cur.fetchone()[0]
		cur.execute("delete from post_liked where user_id='{}' and post_id='{}'".format(user_id, comment_id))	
	except:
		pass
	con.commit()
	return disliked

def get_all_comments_by_user(user_id=None):
	con = psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur = con.cursor()
	try:
		cur.execute("select comment_id, post_id, comment_content from comment where user_id='{}' order by created_at DESC".format(user_id))
		ans = cur.fetchall()
		con.commit()
		return ans
	except:
		pass 
	return []

def get_all_likes_by_user(user_id=None):
	con = psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur = con.cursor()
	ANS = dict()
	ans = ""
	ans2 = ""
	try:
		cur.execute("select C.comment_id, C.comment_content, C.post_id from cmt_liked as CL, comment as C where C.comment_id=CL.comment_id and CL.user_id='{}'".format(user_id))
		ans = cur.fetchall()
	except:
		pass
	try:
		cur.execute("select P.post_id, P.content from post_liked as PL, post as P where P.post_id=PL.post_id and PL.user_id='{}'".format(user_id))
		ans2 = cur.fetchall()
	except:
		pass
	ANS["comments_liked"]=ans
	ANS["posts_liked"]=ans2
	con.commit()
	return ANS

def get_all_dislikes_by_user(user_id=None):
	con = psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur = con.cursor()
	ANS = dict()
	ans = ""
	ans2 = ""
	try:
		cur.execute("select C.comment_id, C.comment_content, C.post_id from cmt_disliked as CL, comment as C where C.comment_id=CL.comment_id and CL.user_id='{}'".format(user_id))
		ans = cur.fetchall()
	except:
		pass
	try:
		cur.execute("select P.post_id, P.content from post_disliked as PL, post as P where P.post_id=PL.post_id and PL.user_id='{}'".format(user_id))
		ans2 = cur.fetchall()
	except:
		pass
	ANS["comments_disliked"]=ans
	ANS["posts_disliked"]=ans2
	con.commit()
	return ANS


def get_cmt_ld_count_of_post_by_user(user_id=None, post_id=None):
	con = psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur = con.cursor()
	ANS = dict()
	p_liked = 0
	p_disliked = 0
	# Post_Num_likes = 0
	# Post_Num_dislikes = 0
	try:
		cur.execute("select * from post_liked where user_id='{}' and post_id='{}'".format(user_id, post_id))
		cur.fetchone()[0]
		p_liked = 1
	except:
		p_liked = 0

	try:
		cur.execute("select * from post_disliked where user_id='{}' and post_id='{}'".format(user_id, post_id))
		cur.fetchone()[0]
		p_disliked = 1 
	except:
		p_disliked = 0

	ANS["has_liked_post"] = p_liked
	ANS["has_disliked_post"] = p_disliked
	ANS["cmt_liked"] = []
	ANS["cmt_disliked"] = []

	try:
		cur.execute("select C.comment_id from cmt_liked as CL, comment as C where CL.comment_id=C.comment_id and C.post_id='{}' and CL.user_id='{}'".format(post_id, user_id))		
		res = cur.fetchall()
		print(res)
		ANS["cmt_liked"] = res
	except:
		pass

	try:
		cur.execute("select C.comment_id from cmt_disliked as CL, comment as C where CL.comment_id=C.comment_id and C.post_id='{}' and CL.user_id='{}'".format(post_id, user_id))
		res = cur.fetchall()
		print(res)
		ANS["cmt_disliked"] = res
	except:
		pass

	con.commit()
	return ANS

def get_post_data(post_id):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("select post_id,count(*) from post_disliked where post_id='{}' group by post_id".format(post_id))
	ret=cur.fetchone()
	if(ret is None):
		post_dislike=0
	else:
		post_dislike=ret[1]
	cur.execute("select post_id,count(*) from post_liked where post_id='{}' group by post_id".format(post_id))
	ret=cur.fetchone()
	if(ret is None):
		post_like=0
	else:
		post_like=ret[1]
	print(post_like,post_dislike)
	cur.execute("select content from post where post_id='{}'".format(post_id))
	post_text=cur.fetchone()[0]
	return [post_text,post_like,post_dislike]

def get_comment_updown(comment_id):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("select count(*) from (select comment_id from cmt_disliked where comment_id='{}') as foo".format(comment_id))
	dis_l=cur.fetchone()[0]
	cur.execute("select count(*) from (select comment_id from cmt_liked where comment_id='{}') as foo".format(comment_id))
	l=cur.fetchone()[0]
	return [l,dis_l]	

def get_comment_data(post_id):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("select comment_id from comment where post_id='{}'".format(post_id))
	ret=cur.fetchall()
	l=[]
	for x in range(0,len(ret)):
		temp=get_comment_updown(ret[x][0])
		cur.execute("select comment_content from comment where comment_id='{}'".format(ret[x][0]))
		ret1=cur.fetchone()[0]
		temp.append(ret1)
		temp.append(ret[x][0])
		l.append(temp)
	return l

def SUBSCRIBE(user_id=None, subreddit_name=None, created_at=None):
	try:
		con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
		cur=con.cursor()
		cur.execute("INSERT into subscribers VALUES(%s,%s,%s)",(subreddit_name, user_id, created_at))
		con.commit()
		return 1
	except:
		return 0

def UNSUBSCRIBE(user_id=None, subreddit_name=None):
	try:
		con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
		cur=con.cursor()
		cur.execute("DELETE from subscribers where subreddit_name='{}' and user_id='{}'".format(subreddit_name, user_id))
		con.commit()
		return 1
	except:
		return 0

def check_sub(user_id=None, subreddit_name=None):
	con=psycopg2.connect(dbname="mydb",user="myuser",password="mypass",host="localhost")
	cur=con.cursor()
	cur.execute("select * from subscribers where user_id='{}' and subreddit_name='{}'".format(user_id, subreddit_name))
	try:
		cur.fetchone()[0]
		con.commit()
		return "YES"
	except:
		con.commit()
		return "NO"