from flask import Flask
from flask import render_template
from flask import request
from db import insert_user as is1
from db import insert_contact as ic1
from db import get_password as gp1
from db import insert_cookie as ic2
from db import get_userid as gu1
from db import delete_cookie as dc1
from db import insert_comment as icm
from db import insert_cmt_liked as icml
from db import insert_cmt_disliked as icmdl
from db import insert_post_liked as ipl
from db import insert_post_disliked as ipdl
from db import get_upvote_downvote_by_post as gudbp
from db import get_comment as gc1
from db import get_comment_liked as gcl1
from db import get_comment_disliked as gcdl1
from db import get_post as gp2
from db import create_subreddit as cs1
from db import get_subreddit as gs1
from db import insert_post as ip1
from db import get_all_comments_by_user as gacbu
from db import get_all_likes_by_user as galbu
from db import get_all_dislikes_by_user as gadlbu
from db import get_cmt_ld_count_of_post_by_user as gcldcopbu
from db import get_post_data
from db import get_comment_data
from db import check_sub
from db import SUBSCRIBE
from db import UNSUBSCRIBE

from mail import sendmail
from datetime import datetime
from uuid import uuid1
import hashlib 
import json


import smtplib
import os

app = Flask(__name__)

s = smtplib.SMTP('iitkgpmail.iitkgp.ac.in', 25)
password=os.getenv("pass_zimbra")
s.login("apoorvakumar169@iitkgp.ac.in",password)

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

@app.route("/createpost",methods=['POST'])
def recv_post_cmnt():
    req=request.form.to_dict()
    postid=str(uuid1())
    created_at=datetime.now()
    content=req["post"]
    user_id=gu1(request.headers["cookie123"])
    subreddit_name=req["subreddit"]
    if(user_id is not None):
        ret=ip1(postid,content,created_at,user_id,subreddit_name)
        sendmail(s,subreddit_name,postid)
        return ret
    return "<h>Failure</h>"

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
                ret=ic2(user_id,cookie)
                return cookie
            else:
                return "<h>wrong password</h>"

@app.route("/logout",methods=["POST"])
def logout():
    req = request.headers
    cookie=req["cookie123"]
    dc1(cookie)
    return "<h>Logged out</h>"

@app.route("/get_username",methods=["POST"])
def get_username():
    req = request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if (user_id is None):
        return "Invaid cookie"
    else:
        return user_id

@app.route("/comment",methods=["POST"])
def comment():
    req1=request.headers
    cookie=req1["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invalid cookie"
    else:
       # comment_id=req["comment_id"]
       #COMMENT ID TO BE CREATED BY HASH OF PARENT ID AND TIMESTAMP
        req=request.form.to_dict()
        comment_content=req["comment_content"]
        # created_at=str(datetime.now())
        created_at=datetime.now()
        comment_id=str(uuid1())
        parent_id=req["parent_id"]
        post_id=req["post_id"]
        ret=icm(comment_id,user_id,comment_content,created_at,parent_id,post_id)
        #WRITE RETURN VALUE
        return "<h>Succefully commentted</h>"

@app.route("/comment_liked",methods=["POST"])
def comment_liked():
    req=request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invaid cookie"
    else:
        req = request.form.to_dict()
        comment_id = req["comment_id"]
        ret = icml(user_id,comment_id)
        return str(ret)

@app.route("/comment_disliked",methods=["POST"])
def comment_disliked():
    req=request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invaid cookie"
    else:
        req = request.form.to_dict()
        comment_id = req["comment_id"]
        ret = icmdl(user_id,comment_id)
        return str(ret)

@app.route("/post_liked",methods=["POST"])
def post_liked():
    req=request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invaid cookie"
    else:
        req = request.form.to_dict()
        comment_id = req["post_id"]
        ret=ipl(user_id,comment_id)
        return str(ret)

@app.route("/post_disliked",methods=["POST"])
def post_disliked():
    req = request.headers
    cookie = req["cookie123"]
    user_id = gu1(cookie)
    if(user_id is None):
        return "Invaid cookie"
    else:
        req = request.form.to_dict()
        comment_id = req["post_id"]
        ret=ipdl(user_id,comment_id)
        return str(ret)

@app.route("/testcomment")
def test_comment():
    return render_template("comment.html")

@app.route("/dummyjson")
def dummyjson():
    dic1={"cid":1,"ctext":"hi there"}
    dic2={"cid":2,"ctext":"hi there1"}
    dic3={"cid":3,"ctext":"hi there2"}
    dic_master=[dic1,dic2,dic3]
    dump=json.dumps(dic_master)
    return dump

@app.route("/comments/<postid>/<commentid>")
def testapi_random(postid,commentid):
    # import pdb;pdb.set_trace();
    return render_template("a_comment.html")

@app.route("/get_a_comment", methods=["POST"])
def get_a_comm():
    req=request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invalid user"
    else:
        req = request.form.to_dict()
        postid = req["postid"]
        commentid = req["commentid"]
        post=gp2(postid)
        comment=gc1(commentid)
        comment_liked=gcl1(commentid)
        comment_disliked=gcdl1(commentid)
        num_of_upvotes=len(comment_liked)
        num_of_downvotes=len(comment_disliked)
        total_like=num_of_upvotes-num_of_downvotes
        dic={"post":post[0][0],"upvote":num_of_upvotes,"downvote":num_of_downvotes,"comment":comment[0][0],"post_id":postid,"comment_id":commentid}
        dump=json.dumps(dic)
        return dump

@app.route("/comm/<postid>/<commentid>")
def testapi_comment(postid,commentid):
    return render_template("individual_comment.html")

@app.route("/createsubreddit",methods=["POST"])
def create_subreddit():
    # import pdb;pdb.set_trace()
    req=request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invalid user"
    else:
        req1=request.form.to_dict()
        # import pdb;pdb.set_trace()
        subreddit_name=req1["subreddit_name"]
        ret=cs1(name1=subreddit_name,subreddit_created_at=datetime.now(),user_id=user_id)
        return "{} created Succefully".format(subreddit_name)

@app.route("/testsubreddit")
def ret_subreddit():
    return render_template("create_subreddit.html")

@app.route("/r_render/<sub_reddit>", methods=["GET"])
def get_all_posts(sub_reddit):
    POSTS = gudbp(sub_reddit)
    Posts = json.dumps(POSTS)
    return Posts

@app.route("/r/<sub_reddit>")
def r_subreddits(sub_reddit):
    return render_template("subreddit.html",name=sub_reddit)

@app.route("/profile")
def profile_template():
    return render_template("profile.html")

@app.route("/get/all_subreddit")
def get_all_subreddit():
    ret=gs1()
    str1=json.dumps(ret)
    return str1

@app.route("/get/all_comment_user")
def get_all_comment_user():
    head=request.headers
    user_id = gu1(head["cookie123"])
    if(user_id is None):
        return "failure"
    else:
        req = request.form.to_dict()
        ans = gacbu(user_id)
        return json.dumps(ans)

@app.route("/get/all_likes_user")
def get_all_likes_user():
    head = request.headers
    user_id = gu1(head["cookie123"])
    if(user_id is None):
        return "failure"
    else:
        req = request.form.to_dict()
        C_P_liked = galbu(user_id)
        C_P_liked = json.dumps(C_P_liked)
        return C_P_liked

@app.route("/get/all_dislikes_user")
def get_all_dislikes_user():
    head = request.headers
    user_id = gu1(head["cookie123"])
    if(user_id is None):
        return "failure"
    else:
        req = request.form.to_dict()
        C_P_disliked = gadlbu(user_id)
        C_P_disliked = json.dumps(C_P_disliked)
        return C_P_disliked

@app.route("/get/Post_comments_count_user", methods=["POST"])
def get_comment_post_count():
    head = request.headers
    user_id = gu1(head["cookie123"])
    if( user_id is None):
        return "failure"
    else:
        req = request.form.to_dict()
        post_id = req["post_id"]
        ANS = gcldcopbu(user_id,post_id)
        ANS = json.dumps(ANS)
        return ANS

@app.route("/post/<postid>")
def render_post(postid):
    return render_template("post.html")

@app.route("/get/post_ka_data",methods=["POST"])
def ret_post_data():
    req=request.form.to_dict()
    post_id=req["post_id"]
    ret=get_post_data(post_id)
    retstr=json.dumps(ret)
    # print(retstr)
    return retstr

@app.route("/get/comment_ka_data",methods=["POST"])
def ret_comment_data():
    req=request.form.to_dict()
    post_id=req["post_id"]
    # import pdb;pdb.set_trace()
    ret=get_comment_data(post_id)
    retstr=json.dumps(ret)
    return retstr

@app.route("/check_subscription", methods=["POST"])
def check_subs():
    req = request.headers
    cookie = req["cookie123"]
    user_id = gu1(cookie)
    if (user_id is None):
        return "Invaid cookie"
    else:
        req = request.form.to_dict()
        subreddit_name = req["subreddit_name"]
        ANS = check_sub(user_id,subreddit_name)
        return ANS

@app.route("/subscribe", methods=["POST"])
def subscribe():
    req = request.headers
    cookie = req["cookie123"]
    user_id = gu1(cookie)
    if (user_id is None):
        return "Invaid cookie"
    else:
        req = request.form.to_dict()
        subreddit_name = req["subreddit_name"]
        ans = SUBSCRIBE(user_id, subreddit_name, datetime.now())
        if (ans==1):
            return "success"
        else:
            return "ERROR"

@app.route("/unsubscribe", methods=["POST"])
def unsubscribe():
    req = request.headers
    cookie = req["cookie123"]
    user_id = gu1(cookie)
    if (user_id is None):
        return "Invaid cookie"
    else:
        req = request.form.to_dict()
        subreddit_name = req["subreddit_name"]
        ans = UNSUBSCRIBE(user_id, subreddit_name)
        if (ans==1):
            return "success"
        else:
            return "ERROR"

app.run(debug=True,threaded=True)