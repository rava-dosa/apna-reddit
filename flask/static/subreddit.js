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
  // ajaxy.always(function(jqXHR,xhr,data,response){
  //   // console.log(ajaxy.responseText);
  //   // var a=JSON.parse(ajaxy.responseText);
  //   // create_comment(a);
  //   return ajaxy;

  // });
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
$(document).ready(function(){

  $("#post_btn").click(function(){
    var txt=document.getElementById("post_id").value;
	var x=window.location.href;
    var x0=x.split("/");
    var subreddit_name=x0[4];
    data1={'post':txt,'subreddit':subreddit_name};
    ajaxy=post1(parent_url+"createpost",data1)
    ajaxy.always(function(){
    	console.log(ajaxy.responseText);
    })
  });
});
function create_post_helper(key,a){
  // var a= document.createElement("a");
  // a.setAttribute("href",parent_url+"post/"+key)
  var para = document.createElement("P");
  para.setAttribute("class","h4");
  var para1 = document.createElement("P");
  para1.innerHTML="Upvotes: "+a["likes"]+" Dislikes: "+a["dislikes"]
  console.log(a);
  para.innerHTML=a["text"];
  var div= document.createElement("div");
  div.setAttribute("id",key);
  // div.setAttribute("borderColor","red");
  // div.style.borderColor ="red";
  div.appendChild(para);
  div.appendChild(para1);
  var a= document.createElement("a");
  a.setAttribute("href",parent_url+"post/"+key);
  // a.setAttribute("class","btn btn-secondary");
  a.innerHTML="See discussion"
  div.appendChild(a);
  // div.style.border = "thin solid #00FFFF"
  div.setAttribute("class","card text-center mb-2 mt-2 mx-auto");
  div.style="width: 50rem;";
  // div.setAttribute("margin","10px");
  // div.setAttribute("flex-flow","column wrap");
  // a.appendChild(div);
  document.getElementById("all_post").appendChild(div);
}

function create_post(a){
  keys=Object.keys(a);
  // console.log("aayamein");
  for(i=0;i<keys.length;i++){
    create_post_helper(keys[i],a[keys[i]]);
    // console.log(keys[i],a[keys[i]]);

  }
}
function foo(url1){
var ajaxy = $.ajax({
		    	url: url1,
		    	method: "get",
		    	});
ajaxy.always(function(jqXHR,xhr,data,response){
	var a=JSON.parse(ajaxy.responseText);
	create_post(a);
});
}

var x = window.location.href;
var x0 = x.split("/");
// console.log(x0[4]);
document.body.style.backgroundColor = "#4d4d4d";
foo("http://localhost:5000/r_render/"+x0[4])