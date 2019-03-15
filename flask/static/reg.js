function REG_SUBMIT() {
    var name1 = document.getElementById("name1").value;
    var user1 = document.getElementById("user1").value;
    var password1 = document.getElementById("password1").value;
    var email1 = document.getElementById("email1").value;
    var date1 = document.getElementById("date1").value;
    var phone_num1 = document.getElementById("phone_num1").value;
    var city1 = document.getElementById("city1").value;
    var state1 = document.getElementById("state1").value;
    ret1={	"user_id": user1,
    		"name":  name1,
    		"pass1": password1, 
    		"email_id": email1, 
    		"city": city1,
    		"state": state1,
    		"date_of_birth": date1,
            "phone_no": phone_num1
    	};

    // console.log(ret1);
    // console.log(ret2);
    ajaxy=$.ajax({
        url: "http://localhost:5000/registration",
        method: "POST",
        dataType: "json",
        data: ret1,
        success: function(result){
            console.log(ret1)
      // $("#div1").append(result);
    }});    
}