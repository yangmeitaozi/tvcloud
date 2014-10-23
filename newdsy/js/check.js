//javaScript Document


function validataNonEmpty(inputField,helpText){
	if(inputField.value.length == 0){
		if(helpText != null){
			helpText.innerHTML = "请检查输入的值";
			return false;
		}
		else{
			if(helpText != null){
				helpText.innerHTML = "";
			}
		}
	}
	return true;
}

function setdisabled(inputField){
	if(document.getElementById('types').value == 2){
		document.getElementById('url').setAttribute('disabled','disabled');
		document.getElementById('channel').removeAttribute('disabled');
	}
	if(document.getElementById('types').value == 1){
		document.getElementById('channel').setAttribute('disabled','disabled');
		document.getElementById('url').removeAttribute('disabled');
	}
}

function placeOrder(form){
	if(validataNonEmpty(form['alias'],form['alias_help']) &&
	validataNonEmpty(form['appname'],form['appname_help']) &&
	validataNonEmpty(form['logo'],form['logo_help']) &&
	validataNonEmpty(form['url'],form['url_help'])){
		form.submit();
	}
	else{
		alert('请检查输入的值');
	}
	
}