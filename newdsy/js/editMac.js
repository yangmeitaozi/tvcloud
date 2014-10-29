$(function(){
			$("input#checkbox").click(function(){	
	$checked = $('input[type="radio"]:checked');
     if($checked.length != 0){	
		 $("#submit").removeAttr("disabled");	
		 $("#delt").removeAttr("disabled");		
        }
					});
				
	    $("#myform").submit(function(e){
        $(':input','#myform').not(':submit').val('');
        var $checked = $('input[type="radio"]:checked');		
        if($checked.length == 0){            
            e.preventDefault();     
            $("#submit").attr("disabled","disabled"); 	
			$("#delt").attr("disabled","disabled");			
            alert("请至少选择一项");   
			return false;   
            }	      
				
        $checked.each(function(a,b){
            var index = a;
            //var $tds = $(b).parent().siblings();
			$("#"+$(b).attr("name")).val($(b).val());
			var $tds = $(b).parent().siblings();
            $tds.each(function(a,b){
                var $input = $(b).children();
                var id = $input.attr("name");
                $("#"+id).val($input.val());				             
                    });			
               
                });
            });
			return true;
 });
	