function cc_helper(id1,text1){
	var para = document.createElement("P");
	var t = document.createTextNode(text1);
	para.appendChild(t);
	var ubtn = document.createElement("button");
	ubtn.setAttribute("id","upvote")
	// ubtn.setAttribute("type","button")
	// ubtn.setAttribute("onclick","u()")
	ubtn.innerHTML="upvote"
	var dbtn = document.createElement("button");
	dbtn.setAttribute("id","downvote")
	// dbtn.setAttribute("onclick","d()")
	dbtn.innerHTML="downvote"
	var reply = document.createElement("button");
	reply.setAttribute("id","reply")
	reply.innerHTML="reply"
	var div1=document.createElement("div");
	div1.setAttribute("id", id1);
	div1.appendChild(para);
	div1.appendChild(ubtn); 
	div1.appendChild(dbtn);
	div1.appendChild(reply);
	div1.style.border = "thick solid #00FFFF"
	document.getElementById("comments").appendChild(div1);
}
function create_textbox(parent_id){
	var parent=document.createElement("DIV");
	parent.setAttribute("id","replybox");
	var x = document.createElement("INPUT");
	x.setAttribute("type", "text");
	x.setAttribute("id", "myText");
	var button=document.createElement("BUTTON");
	button.setAttribute("id",parent_id+'x');
	button.innerHTML="Submit";
	// button.setAttribute("onclick","create_comment()");
	parent.appendChild(x);
	parent.appendChild(button);
	document.getElementById(parent_id).appendChild(parent);
}
function create_comment(a){
	var i;
	for(i=0;i<a.length;i++){
		// console.log(a[i].ctext);
		cc_helper(a[i].cid,a[i].ctext);
	}
}
function get(url1) {
var ajaxy = $.ajax({
		    	url: url1,
		    	method: "get",
		    	});
ajaxy.always(function(jqXHR,xhr,data,response){
	// console.log(ajaxy.responseText);
	var a=JSON.parse(ajaxy.responseText);
	create_comment(a);

});
}
$(document).on("click","#upvote",function(){
	var id = $(this).closest("div").prop("id");
	console.log("upvote"+id);
});

$(document).on("click","#downvote",function(){
	console.log("downvote")
});
$(document).on("click","#reply",function(){
	var test=document.getElementById("replybox");
	if(test != null){
		test.remove();
	}
	var id = $(this).closest("div").prop("id");
	create_textbox(id);
	text=document.getElementById("myText").value;
	console.log(text);
	console.log("reply")
});

// function create_comment(){

// }
get("http://localhost:5000/dummyjson")