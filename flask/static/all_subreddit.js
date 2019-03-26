var parent_url="http://localhost:5000/"

function get(url1) {
  // cookie=getCookie("Login_cookie");
  var ajaxy = $.ajax({
            url: url1,
            method: "get",
            });
  // ajaxy.always(function(jqXHR,xhr,data,response){
  //   // console.log(ajaxy.responseText);
  //   // var a=JSON.parse(ajaxy.responseText);
  //   // create_comment(a);
  //   return ajaxy;

  // });
  return ajaxy;
}
function create_hyperlink(parent_div,text,url){
  var aTag = document.createElement('a');
  aTag.setAttribute('href',url);
  // aTag.setAttribute('class',"text-primary");
  aTag.className = "h4 ml-3 "
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
get_subreddit();