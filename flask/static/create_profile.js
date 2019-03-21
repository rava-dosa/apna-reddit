// data={'post':txt};
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

  $("#post_btn_subreddit").click(function(){
    var txt=document.getElementById("subreddit_id").value;
    data1={'subreddit_name':txt};
    cookie=getCookie("Login_cookie");
    ajaxy=post1(parent_url+"createsubreddit",data1);
  });
});
function create_hyperlink(parent_div,text,url){
  var aTag = document.createElement('a');
  aTag.setAttribute('href',url);
  // aTag.setAttribute('class',"text-primary");
  aTag.className = "h3"
  aTag.innerHTML=text;
  var p = document.createElement('p');
  document.getElementById(parent_div).appendChild(aTag);
  document.getElementById(parent_div).appendChild(p);
}
function create_subreddit_url(text1){
  console.log(text1);
  json1=JSON.parse(text1);
  // console.length(json1.length);
  for(i=0;i<json1.length;i++){
    var temp='r/'+json1[i][0]
    create_hyperlink("all_subreddit",temp,parent_url+temp)
  }
}

function get_subreddit(){
  url1=parent_url+"get/all_subreddit";
  var ajaxy=get(url1);
  ajaxy.always(function(){
    create_subreddit_url(ajaxy.responseText);
  })
  // ajaxy.always()
  // console.log(ajaxy.responseText);
}
function get_recent_comment(){
  url1=parent_url+"get/all_comment";
  var ajaxy=get(url1);
  ajaxy.always(function(){
    console.log(ajaxy.responseText);
  })
  // ajaxy.always()
  // console.log(ajaxy.responseText);
}
function get_recent_likes(){
  url1=parent_url+"get/all_likes";
  var ajaxy=get(url1);
  ajaxy.always(function(){
    console.log(ajaxy.responseText);
  })
  // ajaxy.always()
  // console.log(ajaxy.responseText);
}
function get_recent_dislikes(){
  url1=parent_url+"get/all_dislikes";
  var ajaxy=get(url1);
  ajaxy.always(function(){
    console.log(ajaxy.responseText);
  })
  // ajaxy.always()
  // console.log(ajaxy.responseText);
}

get_subreddit();
get_recent_comment();
get_recent_likes();
get_recent_dislikes();
// <a href="url">link text</a>