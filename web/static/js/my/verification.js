token = getFromStorage('token');
if (!token){
	window.location.href = "/login";
}

getUserData(token).then(function(data){
	if(data.status != 200){
		delFromStorage('user_id');
		delFromStorage('token');
		delFromStorage('email');
		window.location.href = "/login";
	}
	// localStorage.setItem('user_id', data.data.id);
	// localStorage.setItem('email', data.data.email);
	setToStorage('user_id', data.data.id);
	setToStorage('email', data.data.email);
	
});