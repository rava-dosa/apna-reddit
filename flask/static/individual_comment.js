function create_content(post,comment,post_id,comment_id,num_of_upvote){
	var post_box=document.createElement("div");
	post_box.innerHTML=post;
	post_box.setAttribute("id",post_id);
	var cmnt=document.createElement("div");
	cmnt.innerHTML=comment;
	cmnt.setAttribute("id",comment_id);
	var upbtn=document.createElement("button");
	upbtn.innerHTML="upvote";
	upbtn.setAttribute("id","upvote");
	var num_vote=document.createElement("span");
	num_vote.innerHTML=num_of_upvote;
	var downbtn=document.createElement("button");
	downbtn.innerHTML="downvote";
	downbtn.setAttribute("id","downvote");
	var reply=document.createElement("button");
	reply.setAttribute("id","reply")
	reply.innerHTML="reply"

	var div1=document.createElement("div");
	div1.appendChild(post_box);
	div1.appendChild(cmnt);
	div1.appendChild(upbtn);
	div1.appendChild(num_vote);
	div1.appendChild(downbtn);
	div1.appendChild(reply);
	div1.style.border = "thick solid #00FFFF"
	document.getElementById("comments").appendChild(div1);
}


function fun(url1){
var ajaxy = $.ajax({
		    	url: url1,
		    	method: "get",
		    	});
ajaxy.always(function(jqXHR,xhr,data,response){
	// console.log(ajaxy.responseText);
	var a=JSON.parse(ajaxy.responseText);
	create_content(a["post"],a["comment"],a["post_id"],a["comment_id"],a["total_upvote"]);

});
}
var x=window.location.href;
var x0=x.split("/");
// console.log(postid);
fun("http://localhost:5000/comments/"+x0[4]+"/"+x0[5])