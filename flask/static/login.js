function setCookie(cname,cvalue,exdays) {
    var d = new Date();  
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function LOGIN() {
    var user1 = document.getElementById("l_user").value;
    var password1 = document.getElementById("l_password").value;
    ret1={  "user_id": user1,
            "pass1": password1, 
        };

    console.log(ret1);
    // console.log(ret2);
    ajaxy=$.ajax({
        url: "http://localhost:5000/login",
        method: "POST",
        dataType: "json",
        data: ret1,   
    });
    ajaxy.always(function(jqXHR, xhr, data, response){
        recv = jqXHR.responseText;
        var n = recv.search("<h>");
        if(n==-1){
            setCookie("Login_cookie",recv, 1);
        }else{
            document.getElementById("l_form").innerHTML=recv;
        }
    });
}

// function getCookie(cname) {
//   var name = cname + "=";
//   var decodedCookie = decodeURIComponent(document.cookie);
//   var ca = decodedCookie.split(';');
//   for(var i = 0; i < ca.length; i++) {
//     var c = ca[i];
//     document.write(c+"<br/>")
//     while (c.charAt(0) == ' ') {
//       c = c.substring(1);
//     }
//     if (c.indexOf(name) == 0) {
//       document.write("FINAL:"+c+"<br/>")     
//       return c.substring(name.length, c.length);
//     }
//   }
//   return "";
// }

// function checkCookie() {
//   var d = new Date();
//   document.write(d.getTime());
//  var user=getCookie("user");
//   if (user != "") {
//    alert("Welcome again " + user);
//   } else 
//   {
//      user = prompt("Please enter your name:","");
//      if (user != "" && user != null) {
//        setCookie("user", user, 30);
//      }
//   }
// }