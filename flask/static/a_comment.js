var parent_url="http://localhost:5000/"
function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function get(url1) {
  cookie=getCookie("Login_cookie");
  var ajaxy = $.ajax({
            url: url1,
            method: "get",
            headers: {"cookie123":cookie}
            });
  return ajaxy;
}

function get_a_comment(){
  	// console.log("doneA");
  	url1=parent_url+"get_a_comment";
  	cookie=getCookie("Login_cookie");
	var x = window.location.href;
	var x0 = x.split("/");
	ajaxy = $.ajax({
        url: url1,
        method: "POST",
        headers: {"cookie123":cookie},
    	data: {"postid":x0[4], "commentid":x0[5]}
    });
  	ajaxy.always(function(){
    	// console.log(ajaxy.responseText);
		ret = ajaxy.responseText;
    	retstr = JSON.parse(ret);
    	retkey = Object.keys(retstr);
    	// console.log(retkey)
    	create_content(retstr["post"], retstr["comment"], retstr["post_id"], retstr["comment_id"], retstr["upvote"], retstr["downvote"]);   
  	});
}

function create_content(post,comment,post_id,comment_id,upvote,downvote){
	var post_box=document.createElement("div");
	
	post_box.setAttribute("id",post_id);

	bold = document.createElement("h4");
	bold.innerHTML=post;
	hr = document.createElement("hr");
	empty = document.createElement("p");
	post_box.appendChild(bold);

	var cmnt=document.createElement("div");
	cmnt.innerHTML=comment;
	cmnt.setAttribute("id",comment_id);
	var upbtn=document.createElement("button");
	upbtn.innerHTML="upvote";
	upbtn.setAttribute("id","upvote");
	upbtn.setAttribute("onclick","UPVOTE()");
	var Upvote=document.createElement("span");
	Upvote.setAttribute("id","up");
	Upvote.innerHTML=upvote;
	var downbtn=document.createElement("button");
	downbtn.innerHTML="downvote";
	downbtn.setAttribute("id","downvote");
	downbtn.setAttribute("onclick","DOWNVOTE()");
	var Downvote=document.createElement("span");
	Downvote.setAttribute("id","down");
	
	Downvote.innerHTML=downvote;
	// var reply=document.createElement("button");
	// reply.setAttribute("id","reply")
	// reply.innerHTML="reply"

	var div1=document.createElement("div");
	div1.appendChild(post_box);
	div1.appendChild(hr);
	div1.appendChild(empty);
	div1.appendChild(cmnt);
	div1.appendChild(upbtn);
	div1.appendChild(Upvote);
	div1.appendChild(downbtn);
	div1.appendChild(Downvote);
	// div1.appendChild(reply);
	div1.style.border = "thick solid #00FFFF"
	document.getElementById("comments").appendChild(div1);
	check_color();
}
function UPVOTE(){
	url1=parent_url+"comment_liked";
  	cookie=getCookie("Login_cookie");
	var x = window.location.href;
	var x0 = x.split("/");
	ajaxy = $.ajax({
        url: url1,
        method: "POST",
        headers: {"cookie123":cookie},
    	data: {"comment_id":x0[5]}
    });
  	ajaxy.always(function(){
  		check_color();
	    window.location.reload(true);
	});
}
function DOWNVOTE(){
	url1=parent_url+"comment_disliked";
  	cookie=getCookie("Login_cookie");
	var x = window.location.href;
	var x0 = x.split("/");
	ajaxy = $.ajax({
        url: url1,
        method: "POST",
        headers: {"cookie123":cookie},
    	data: {"comment_id":x0[5]}
    });
    ajaxy.always(function(){
	    check_color();
	    window.location.reload(true);
	});
}

// url1 = parent_url + "get/Post_comments_count_user"


function check_color(){
	// console.log("done1");
	var x = window.location.href;
	var x0 = x.split("/");
	url1 = parent_url + "get/Post_comments_count_user";
		ajax2 = $.ajax({
		        url: url1,
		        method: "POST",
		        headers: {"cookie123":cookie},
		    	data: {"post_id":x0[4], "comment_id":x0[5]}
		    });
	liked = 0;
	disliked = 0;
	ajax2.always(function(){
		var a = ajax2.responseText;
		retstr = JSON.parse(a);
		cmt_liked = retstr["cmt_liked"];
		cmt_disliked = retstr["cmt_disliked"];
		for (i=0; i<cmt_liked.length; i++) {
			// console.log(cmt_liked[i]);
			if(cmt_liked[i]==x0[5]){
				// console.log("REALLY LIKED");
				liked = 1;
			}
		}
		for (i=0; i<cmt_disliked.length; i++) {
			console.log(cmt_disliked[i]);
			if(cmt_disliked[i]==x0[5]){
				// console.log("REALLY DISLIKED");
				disliked = 1;
			}
		}
		if(liked==1){
			(document.getElementById('upvote')).style.backgroundColor = "#258C2B";
			(document.getElementById('upvote')).style.width = "85px";
			(document.getElementById('upvote')).style.height = "35px";
			(document.getElementById('upvote')).style.borderRadius = "25px";	    	
	    	(document.getElementById('upvote')).blur();
	    	(document.getElementById('downvote')).style.backgroundColor = "";
	    	(document.getElementById('downvote')).style.backgroundColor = "";
			(document.getElementById('downvote')).style.width = "";
			(document.getElementById('downvote')).style.height = "";
			(document.getElementById('downvote')).style.borderRadius = "";	    	
	    	(document.getElementById('downvote')).blur();
		}else{
			(document.getElementById('upvote')).style.backgroundColor = "";
			(document.getElementById('upvote')).style.width = "";
			(document.getElementById('upvote')).style.height = "";
			(document.getElementById('upvote')).style.borderRadius = "";	    	
	    	(document.getElementById('upvote')).blur();
		}
		if(disliked==1){
	  		(document.getElementById('downvote')).style.backgroundColor = "#258C2B";
			(document.getElementById('downvote')).style.width = "110px";
			(document.getElementById('downvote')).style.height = "35px";
			(document.getElementById('downvote')).style.borderRadius = "25px";	    	
	    	(document.getElementById('downvote')).blur();
	    	(document.getElementById('upvote')).style.backgroundColor = "";
	    	(document.getElementById('upvote')).style.backgroundColor = "";
			(document.getElementById('upvote')).style.width = "";
			(document.getElementById('upvote')).style.height = "";
			(document.getElementById('upvote')).style.borderRadius = "";	    	
	    	(document.getElementById('upvote')).blur();
		}
		else{
	    	(document.getElementById('downvote')).style.backgroundColor = "";
			(document.getElementById('downvote')).style.width = "";
			(document.getElementById('downvote')).style.height = "";
			(document.getElementById('downvote')).style.borderRadius = "";	    	
	    	(document.getElementById('downvote')).blur();
		}
	});
	// console.log("done2");
}

get_a_comment();
