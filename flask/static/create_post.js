// data={'post':txt};
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


$(document).ready(function(){

  $("#post_btn").click(function(){
    var txt=document.getElementById("post_id").value;
    data1={'post':txt,'subreddit':'r/dbms'};
    cookie=getCookie("Login_cookie");
    $.ajax({
    	url: "http://localhost:5000/createpost",
    	method: "POST",
    	dataType: "json",
      headers:{"cookie":cookie},
    	data: data1
    });


  });

  // $("")

});


