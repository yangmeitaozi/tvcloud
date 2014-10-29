function validateRegEx(regex, input, helpText, helpMessage){
		if(!regex.test(input)){
			// The data is invalid, so set the help message and return false
			if(helpText != null)
				helpText.innerHTML = helpMessage;
			return false;
			}
		else{
				// The data is OK, so clear the help message and return true
			if(helpText != null)
				helpText.innerHTML = "";
			return true;
			}
		}
		
	function validateNonEmpty(inputField, helpText){
	// See if the input value contains any text
	return validateRegEx(/.+/,inputField.value, helpText,"请输入一个值.");
	}
	  
	function valiosname(inputfield, helpText){	
		if(inputfield.value.length==0){
			if(helpText != null) 
				helpText.innerHTML = "请输入一个值";
			//alert('null');		
			return false;
		}
		else{
			if(helpText != null)
				helpText.innerHTML = "";
			return true;
		}	
	}
	
	function validateIp(inputField, helpText){
		// First see if the input value contains data
		if(!validateNonEmpty(inputField, helpText))
			return false;
		// Then see if the input value is a ZIP code
		return validateRegEx(/^\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/,inputField.value, helpText,"请输入类似这样的IP地址：127.0.0.1");
	}
	
	function validateMac1(inputField, helpText){
		// First see if the input value contains data
		if(!validateNonEmpty(inputField, helpText))
			return false;
		// Then see if the input value is a ZIP code
		if(validateRegEx(/^\w{12}/,inputField.value, helpText,"请输入类似这样的mac号：001A34CFF2C2 ")){
			if(document.getElementById("mac1").value > document.getElementById("mac2").value && document.getElementById("mac2").value.length != 0 ){
			//alert("there has wrong of mac1");
				helpText.innerHTML="mac1要小于等于mac2，请重新输入";
				return false;
			}
			else{
			return true;
			}
		}
		
	
	}
	
	function validateMac2(inputField, helpText){
		// First see if the input value contains data
		if(!validateNonEmpty(inputField, helpText))
			return false;
		// Then see if the input value is a ZIP code
		if(validateRegEx(/^\w{12}/,inputField.value, helpText,"请输入类似这样的mac号：001A34CFF2C2 ")){
			if(document.getElementById("mac1").value > document.getElementById("mac2").value && document.getElementById("mac2").value.length != 0 ){
			// alert("there has wrong of mac2");
			helpText.innerHTML="mac2要大于等于mac1，请重新输入";
			return false;		 
	 	}
		else{
			return true;
		}
	 }
	}
	function validatePort(inputField, helpText){
		// First see if the input value contains data
		if(!validateNonEmpty(inputField, helpText))
		return false;
		// Then see if the input value is a ZIP code
		return validateRegEx(/^\w{2,4}/,inputField.value, helpText,"请输入类似80或8080这样的端口号 ");
	 
	}
	function placeOrder1(form) {
		if(valiosname(form['osname'],form['osnamehelp'])){
			form.submit();
			alert("输入已提交");
		}
		else {
          alert("请检查输入的数据.");
        }
	}
	
	function placeOrder2(form) {
		if(validateIp(form['ip'],form['ip_help']) && validatePort(form['port'],form['port_help']) ){
			form.submit();
			alert("输入已提交");
		}
		else {
          alert("请检查输入的数据.");
        }
	}
	
	function placeOrder3(form) {
		if(validateMac1(form['mac1'],form['mac1_help']) && validateMac2(form['mac2'],form['mac2_help'])){
			form.submit();
			alert("输入已提交");
		}
		else {
		  alert("请检查输入的数据.");
		  return false;
          
		  
        }
	}
	
	function check(form){
		//aletr(form);
		if(!placeOrder3(form)){
			alert("文本框输入为空，不能提交表单！"); 
        	document.getElementById("mac1").focus; 
			document.getElementById("mac2").focus;
        	return false; 
		}
		
	}