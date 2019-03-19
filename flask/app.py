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
from db import get_upvote_downvote_by_post as gudbp
from db import get_comment as gc1
from db import get_comment_liked as gcl1
from db import get_comment_disliked as gcdl1
from db import get_post as gp2
from db import create_subreddit as cs1
from datetime import datetime
from uuid import uuid1
import hashlib 
import json

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
    req=request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invaid cookie"
    else:
       # comment_id=req["comment_id"]
       #COMMENT ID TO BE CREATED BY HASH OF PARENT ID AND TIMESTAMP
        comment_content=req["comment_content"]
        # created_at=str(datetime.now())
        created_at=datetime.now()
        comment_id=hashlib.sha256(created_at)
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
        comment_id=["comment_id"]
        ret=icml(user_id,comment_id)
        #WRITE RETURN VALUE
        return "<h1>You Upvoted this comment</h1>"

@app.route("/comment_disliked",methods=["POST"])
def comment_disliked():
    req=request.headers
    cookie=req["cookie123"]
    user_id=gu1(cookie)
    if(user_id is None):
        return "Invaid cookie"
    else:
        comment_id=["comment_id"]
        ret=icmdl(user_id,comment_id)
        #WRITE RETURN VALUE
        return "<h1>You Downvoted this comment</h1>"


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

@app.route("/r/<sub_reddit>")
def get_all_posts(sub_reddit):
    print("Requested sub_reddit:", sub_reddit)
    POSTS = gudbp(sub_reddit)
    Posts = json.dumps(POSTS)
    return "<h6>{}</h6>".format(Posts)

app.run(debug=True,threaded=True)
