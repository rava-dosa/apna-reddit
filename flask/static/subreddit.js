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


function foo(url1){
var ajaxy = $.ajax({
		    	url: url1,
		    	method: "get",
		    	});
ajaxy.always(function(jqXHR,xhr,data,response){
	var a=JSON.parse(ajaxy.responseText);
});
}

var x = window.location.href;
var x0 = x.split("/");
// console.log(x0[4]);
foo("http://localhost:5000/r_render/"+x0[4])