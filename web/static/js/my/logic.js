
       
var user_id = getFromStorage('user_id');
var token = getFromStorage('token');

getSubjects(user_id, token).then(function(data){
	if(data.status == 401){
		delFromStorage('token');
		delFromStorage('user_id');
		delFromStorage('email');
		window.location.href = "/login";
	}
	else if(data.status != 200){
		alert(data.message);
	}
	else{
		var navbar = document.getElementById("usernavbar");
		var logout = document.createElement("li");
		var logoutBtn = document.createElement("a");
		logoutBtn.setAttribute('onclick', 'logout()');
		var logoutTxt = document.createTextNode("Выход");
		logoutBtn.appendChild(logoutTxt);
		logout.appendChild(logoutBtn);

		var user = document.createElement("li");
		var userEmail = document.createTextNode(getFromStorage("email"));
		user.appendChild(userEmail);

		navbar.appendChild(logout);
		navbar.appendChild(user);
		data.data.forEach(function(data, index, arr){
			appendSubject(data);
		});
	}
});


