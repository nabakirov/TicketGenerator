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

function newSubject(name, uid, token){
	return axios({
		method: 'post',
		url: '/api/' + uid,
		data: {
			token: token,
			'name': name
		}
	}).then(function(response){
		return response.data;
	}).catch(error =>{
		return error.response.data;
	});
}

function updateSubject(name, id, uid, token){
	return axios({
		method: 'post',
		url: '/api/' + uid,
		data: {
			token: token,
			'id': id,
			'name': name
		}
	}).then(function(response){
		return response.data;
	}).catch(error =>{
		return error.response.data;
	});
}

function newQuestion(text, hardness, uid, sid, token){
	return axios({
		method: 'post',
		url: '/api/' + uid + '/' + sid,
		data: {
			'token': token,
			'text': text,
			'hardness': hardness
		}
	}).then(function(response){
		return response.data;
	}).catch(error =>{
		return error.response.data;
	});
}

function toGenerate(t_cnt, q_cnt, uid, sid, token){
	return axios({
		method: 'post',
		url: '/api/generate/' + uid + '/' + sid,
		data: {
			'token': token,
			'ticket_cnt': t_cnt,
			'question_cnt': q_cnt
		}
	}).then(function(response){
		return response.data;
	}).catch(error =>{
		return error.response.data;
	});
}

function toDownload(download, token){
	window.open(download+'&token='+token, '_blank')
	
	// return axios({
	// 	method: 'post',
	// 	url: '/api/download',
	// 	data: {
	// 		'token': token,
	// 		'file_path': file_path
	// 	}
	// }).then(function(response){
	// 	return response;
	// }).catch(error =>{
	// 	return error.response.data;
	// });
}