$(document).ready(function(){
  $("button").click(function(){
    $.ajax({url: "http://localhost:5000/apoorva", success: function(result){
      $("#div1").append(result);
    }});
  });
});