$(function(){
	    $("#myform").submit(function(e){
			        $(':input','#myform').not(':submit').val('');
					$checked = $('input[type="checkbox"]:checked');
					if($checked.length == 0){
						alert("at least one get");
						e.preventDefault();
						}
					$checked.each(function(a,b){
						var index = a;
					    var $tds = $(b).parent().siblings();
			        $tds.each(function(a,b){
						var $input = $(b).children();
						var id = $input.attr("name");
						var $id = $("#"+id);
						var value = $id.val()+","+$input.val();
						if(value.trim() != '' && index == 0){
							   value = value.substring(1);
							                       }
						$("#"+id).val(value);
						 });
					});
				});
})