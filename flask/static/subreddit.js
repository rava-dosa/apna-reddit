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