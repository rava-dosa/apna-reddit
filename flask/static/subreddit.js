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
       location.reload();
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
  console.log(a);
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

function check_subs(){
  cookie=getCookie("Login_cookie");
  URL = parent_url+"check_subscription";
  var x = window.location.href;
  var x0 = x.split("/");
  SR_name = x0[4];
  console.log(SR_name);
  console.log(URL);
  ajaxy=$.ajax({
    url: URL,
    method: "POST",
    dataType: "json",
    headers:{"cookie123":cookie},
    data: {"subreddit_name":SR_name}
  });
  ajaxy.always(function(jqXHR,xhr,data,response){
    var a=ajaxy.responseText;
    console.log(a);
    if(a=="YES"){
      document.getElementById('subs').innerHTML="UNSUBSCRIBE";
    }else if(a=="NO"){
      document.getElementById('subs').innerHTML="SUBSCRIBE";        
    }
  });
}


function subs_unsubs(){
    cookie = getCookie("Login_cookie");
    URL = parent_url;
    var x = window.location.href;
    var x0 = x.split("/");
    SR_name = x0[4];
    text = document.getElementById('subs').innerHTML
    if(text == "UNSUBSCRIBE"){
      URL = URL + "unsubscribe";
      
    }else if(text == "SUBSCRIBE"){
      URL = URL + "subscribe";
    }
    ajaxy=$.ajax({
      url: URL,
      method: "POST",
      dataType: "json",
      headers:{"cookie123":cookie},
      data: {"subreddit_name":SR_name}
    });
    ajaxy.always(function(jqXHR,xhr,data,response){
      var a=ajaxy.responseText;
      console.log(a);
      if(a =="success"){
        if(text == "UNSUBSCRIBE"){
          document.getElementById('subs').innerHTML="SUBSCRIBE";       
        }else if(text == "SUBSCRIBE"){
          document.getElementById('subs').innerHTML="UNSUBSCRIBE";
        }
      }
    });
}

var x = window.location.href;
var x0 = x.split("/");
// console.log(x0[4]);
document.body.style.backgroundColor = "#C0C0C0";
foo("http://localhost:5000/r_render/"+x0[4]);
check_subs();