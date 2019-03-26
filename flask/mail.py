import smtplib
import os
from db import getall_sub
def sendmail_helper(s,email_id,message):
	print(email_id)
	try:
		s.sendmail("apoorvakumar169@iitkgp.ac.in", email_id,message)
	except:
		print("failed",email_id,message)


def sendmail(s,subreddit,post_id):
	ret=getall_sub(subreddit)
	for x in range(0,len(ret)):
		# import pdb;pdb.set_trace()
		sendmail_helper(s,ret[x],"A new post was posted on {} , url is -> http://localhost:5000/post/{}".format(subreddit,str(post_id)))
	print(ret,subreddit,post_id)