alert('haha its working');
function getToken(){
	token = null
	try{
		token = localStorage.getItem('token');
	}
	catch(e){
		token = null;
	}
	return token;
}
function setToken(token){
	ok = false;
	try{
		localStorage.setItem('token', token);
		ok = true;
	}
	catch(e){
		ok = false;
	}
	return ok;
}