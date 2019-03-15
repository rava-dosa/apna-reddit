// data={'post':txt};
$(document).ready(function(){

  $("#post_btn").click(function(){
    var txt=document.getElementById("post_id").value;
    data1={'post':txt};
    $.ajax({
    	url: "http://localhost:5000/recvPostCmnt",
    	method: "POST",
    	dataType: "json",
    	data: data1
    }
    );
  });

  // $("")

});


