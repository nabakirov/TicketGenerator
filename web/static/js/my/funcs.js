// <li>
// <div class="card">
//   <div class="card-content">
//     <p>I am a very simple card. I am good at containing small bits of information.
//           I am convenient because I require little markup to use effectively.</p>
//   </div>
// </div>
// </li>
function appendQuestion(data){
	// var li = document.createElement('li');
	// li.setAttribute('dbid', data.id);

	var Cont = document.getElementById('content');
	console.log(Cont);
		
	Cont.childNodes.forEach(function(data, index, arr){
		Cont.removeChild(data);
	});
	
	var qlist = document.createElement('div');

	qlist.setAttribute('id', 'qlist');
	data.forEach(function(data, index, arr){
		var card = document.createElement('div');
		card.setAttribute('class', 'card');
		var content = document.createElement('div');
		content.setAttribute('class', 'card-content');
		var text = document.createTextNode(data.text);
		var p = document.createElement('p');
		p.appendChild(text);
		content.appendChild(p);
		card.appendChild(content);
		qlist.appendChild(card);

	});
	Cont.insertBefore(qlist, Cont.childNodes[0]);
}


function getUserData(token){
		
	return axios({
		method: 'post',
		url: '/api/verify',
		data: {
			token: token
		}
	}).then(function(response){
		return response.data;
	}).catch(error =>{
		return error.response.data;
	});
	
}
function getSubjects(uid, token){
	api = '/api/'
	return axios({
		method: 'get',
		url: api.concat(uid),
		params: {
			token: token
		}
	}).then(function(response){
		return response.data;
	}).catch(error =>{
		return error.response.data;
	});
}
function getQuestions(uid, sid, token){
	
	return axios({
		method: 'get',
		url: '/api/' + uid + '/' + sid,
		params: {
			token: token
		}
	}).then(function(response){
		return response.data;
	}).catch(error =>{
		return error.response.data;
	});
}

function loadQuestions(sid){
	uid = getFromStorage('user_id');
	token = getFromStorage('token');
	getQuestions(uid, sid, token).then(function(data){
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

			appendQuestion(data.data);
		}
	});
}


function logout(){
	delFromStorage('token');
	delFromStorage('email');
	delFromStorage('user_id');
	window.location.href = "/login";
}



