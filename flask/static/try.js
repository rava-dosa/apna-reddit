data1={"podu":"pada"};
$(document).ready(function(){

  $("button").click(function(){
    $.ajax({
    	url: "http://localhost:5000/apoorva",
    	method: "POST",
    	dataType: "json",
    	data: data1,
    	success: function(result){
    		console.log(result)
      $("#div1").append(result);
    }});
  });

  // $("")

});