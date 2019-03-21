var parent_url="http://localhost:5000/"
var x=window.location.href;
var x0=x.split("/");
console.log(x0);
post_id=x0[4];

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

function post1(url1,data1){
  cookie=getCookie("Login_cookie");
    ajaxy=$.ajax({
      url: url1,
      method: "POST",
      dataType: "json",
        headers:{"cookie123":cookie},
      data: data1
    });
    return ajaxy;
}
function cc_helper(id1,text1,upvote,downvote){
  var para = document.createElement("P");
  var t = document.createTextNode(text1);
  para.appendChild(t);
  para.setAttribute("class","h5 p-2");
  var ubtn = document.createElement("button");
  ubtn.setAttribute("id","upvote")
  ubtn.setAttribute("class","btn btn-outline-primary col-1 ml-5");
  // ubtn.setAttribute("type","button")
  // ubtn.setAttribute("onclick","u()")
  ubtn.innerHTML="upvote: "+upvote;
  var dbtn = document.createElement("button");
  dbtn.setAttribute("id","downvote")
  dbtn.setAttribute("class","btn btn-outline-primary col-1 ml-2");
  // dbtn.setAttribute("onclick","d()")
  dbtn.innerHTML="downvote: "+downvote;
  var reply = document.createElement("button");
  reply.setAttribute("id","reply")
  reply.setAttribute("class","btn btn-outline-primary col-1 ml-2");
  reply.innerHTML="reply"
  var div1=document.createElement("div");
  div1.setAttribute("id", id1+"y");
  var div2=document.createElement("div");
  div2.setAttribute("id",id1);
  div1.appendChild(para);
  div2.appendChild(ubtn); 
  div2.appendChild(dbtn);
  div2.appendChild(reply);
  div1.setAttribute("class","card mb-2 ml-5");
  div1.appendChild(div2);
  div1.style.border = "thick solid #00FFFF"
  div1.style="width: 100rem;";
  div1.style.backgroundColor = "#d8d8d8";
  document.getElementById("comments").appendChild(div1);
}

function cc_helper_post(id1,text1,upvote,downvote){
  var para = document.createElement("P");
  var t = document.createTextNode(text1);
  para.appendChild(t);
  para.setAttribute("class","h4 p-2");
  var ubtn = document.createElement("button");
  ubtn.setAttribute("id","upvote_post")
  ubtn.setAttribute("class","btn btn-outline-primary col-1 ml-3");
  // ubtn.setAttribute()
  // ubtn.setAttribute("type","button")
  // ubtn.setAttribute("onclick","u()")
  ubtn.innerHTML="upvote: "+upvote;
  var dbtn = document.createElement("button");
  dbtn.setAttribute("id","downvote_post")
  dbtn.setAttribute("class","btn btn-outline-primary col-1 ml-2");

  // dbtn.setAttribute("onclick","d()")
  dbtn.innerHTML="downvote: "+downvote;
  var reply = document.createElement("button");
  reply.setAttribute("id","reply_post")
  reply.setAttribute("class","btn btn-outline-primary col-1 ml-2");
  reply.innerHTML="reply"
  var div1=document.createElement("div");
  // div1.setAttribute("class","card mb-2 mt-2 mx-auto");
  var div2=document.createElement("div");
  div2.setAttribute("class","row");
  div2.setAttribute("id",id1);
  div1.setAttribute("id", id1+"y");
  div1.appendChild(para);
  div2.appendChild(ubtn); 
  div2.appendChild(dbtn);
  div2.appendChild(reply);
  div1.appendChild(div2);
  // div1.style.border = "thick solid #00FFFF"
  div1.setAttribute("class","card mb-2 ml-3");
  div1.style="width: 100rem;";
  document.getElementById("post").appendChild(div1);
}
function create_textbox(parent_id){
  var parent=document.createElement("DIV");
  parent.setAttribute("id","replybox");
  var x = document.createElement("INPUT");
  x.setAttribute("type", "text");
  x.setAttribute("id", "myText");
  var button=document.createElement("BUTTON");
  button.setAttribute("id","replyon");
  button.innerHTML="Submit";
  // button.setAttribute("onclick","create_comment()");
  parent.appendChild(x);
  parent.appendChild(button);
  document.getElementById(parent_id).appendChild(parent);
}

$(document).on("click","#upvote_post",function(){
  var id = $(this).closest("div").prop("id");
  // background-color: ;
  $(this).css("background","#4CAF50")
  // var data1={"comment_id":id};
  dic1={"post_id":post_id};
  ajaxy=post1(parent_url+"post_liked",dic1)
  ajaxy.always(function(){
    console.log(ajaxy);
  });
  console.log("upvote"+id);
});

$(document).on("click","#upvote",function(){
  var id = $(this).closest("div").prop("id");
  // background-color: ;
  $(this).css("background","#4CAF50")
  var data1={"comment_id":id};
  ajaxy=post1(parent_url+"comment_liked",data1)
  ajaxy.always(function(){
    console.log(ajaxy);
  });
  console.log("upvote"+id);
});

$(document).on("click","#downvote_post",function(){
  var id = $(this).closest("div").prop("id");
  $(this).css("background","red")
  // var data1={"comment_id":id};
  dic1={"post_id":post_id};
  ajaxy=post1(parent_url+"post_disliked",dic1)
  ajaxy.always(function(){
    console.log(ajaxy);
  }); 
  console.log("downvote")
});

$(document).on("click","#downvote",function(){
  var id = $(this).closest("div").prop("id");
  $(this).css("background","red")
  var data1={"comment_id":id};
  ajaxy=post1(parent_url+"comment_disliked",data1)
  ajaxy.always(function(){
    console.log(ajaxy);
  }); 
  console.log("downvote")
});

$(document).on("click","#reply_post",function(){
  var test=document.getElementById("replybox");
  if(test != null){
    test.remove();
  }
  var id = $(this).closest("div").prop("id");
  create_textbox(id);
  $(document).on("click","#replyon",function(){
    text=document.getElementById("myText").value;
    var data1={"parent_id":id,"comment_content":text,"post_id":post_id};
    ajaxy1=post1(parent_url+"comment",data1)
    ajaxy1.always(function(){
      console.log(ajaxy1);
    })
  })
  
});

$(document).on("click","#reply",function(){
  var test=document.getElementById("replybox");
  if(test != null){
    test.remove();
  }
  var id = $(this).closest("div").prop("id");
  create_textbox(id);
  $(document).on("click","#replyon",function(){
    text=document.getElementById("myText").value;
    var data1={"parent_id":id,"comment_content":text,"post_id":post_id};
    ajaxy1=post1(parent_url+"comment",data1)
    ajaxy1.always(function(){
      console.log(ajaxy1);
    })
  })
  
});

function get_post(){
  dic1={"post_id":post_id};
  ajaxy=post1(parent_url+"get/post_ka_data",dic1);
  ajaxy.always(function(){
    ret1=ajaxy.responseText;
    console.log(ret1);
    retstr1=JSON.parse(ret1);
    cc_helper_post(post_id,retstr1[0],retstr1[1],retstr1[2])
  })
}
function create_comment(a){
  var i;
  console.log("apoorva",a,a.length);
  for(i=0;i<a.length;i++){
    // console.log(a[i].ctext);
    cc_helper(a[i][3],a[i][2],a[i][0],a[i][1]);
  }
}

function get_comments(){
  dic1={"post_id":post_id};
  ajaxy1=post1(parent_url+"get/comment_ka_data",dic1);
  ajaxy1.always(function(){
    ret=ajaxy1.responseText;
    retstr=JSON.parse(ret);
    create_comment(retstr)
    console.log(ret);
  })
}
// body=document.getElementsByTagName("BODY")[0]; 
// body.setAttribute("backgroundColor","#4d4d4d");
document.body.style.backgroundColor = "#4d4d4d";
get_comments();
get_post();
