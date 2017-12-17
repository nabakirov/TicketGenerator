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
	if(Cont.childNodes.length > 0){

		Cont.childNodes.forEach(function(data, index, arr){
			Cont.removeChild(data);
		});
	}
	
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


function checkToAddQuestion(){
	subject = document.getElementById('listOfSubjects');
	subjectInd = subject.selectedIndex;
	text = document.getElementById('addNewSubjectText').value;

	if(subjectInd == 0 || !text){
		alert("Заполни");
	}
	else{

		sid = subject.options[subjectInd].value;
		uid = getFromStorage('user_id');
		token = getFromStorage('token');
		newQuestion(text, 1, uid, sid, token).then(function(data){
			if(data.status != 200){
				alert(data.message);
			}
			else{
				loadQuestions(sid);
			}
		});
	}
	
}

function addNewQuestion(){
	content = document.getElementById('content');
	if(content.childNodes.length > 0){
		
		content.childNodes.forEach(function(data, index, arr){
			content.removeChild(data);
		});
	}
	getSubjects(getFromStorage('user_id'), getFromStorage('token')).then(function(data){
		if(data.status != 200){
			alert(data.message);
		}
		else{
		 	selectDiv = document.createElement('div');
			selectDiv.setAttribute('class', 'input-field col s12')
			
			select = document.createElement('select');
			select.setAttribute('id', 'listOfSubjects')

			text = document.createTextNode('Выбери Предмет');
			option1 = document.createElement('option');
			option1.setAttribute('value', " ");
			option1.setAttribute('disabled',"");
			option1.setAttribute('selected', "");
			option1.appendChild(text);
			select.appendChild(option1);
			

			data.data.forEach(function(data, index, arr){

				option = document.createElement('option');
				option.setAttribute('id', data.id);
				option.setAttribute('value', data.id);
				option.appendChild(document.createTextNode(data.name));
				select.appendChild(option);


			});
			selectDiv.appendChild(select);

			div = document.createElement('div');
			p = document.createElement('h5');
			p.appendChild(document.createTextNode('Добавить Вопрос'));
			input = document.createElement('input');
			input.setAttribute('type', 'text');
			input.setAttribute('id', 'addNewSubjectText')
			btn = document.createElement('button');
			btn.setAttribute('onclick', 'checkToAddQuestion()');
			btn.appendChild(document.createTextNode('Сохранить'));

			div.appendChild(p);
			div.appendChild(selectDiv);
			div.appendChild(input);
			div.appendChild(btn);

			content.appendChild(div);
			$(document).ready(function() {
			    $('select').material_select();
			  });

		}
	});
}
			// selectDiv.appendChild(select);
			// label = document.createElement('label');
			// label.appendChild(document.createTextNode("Выбери Предмет"));

// <div class="input-field col s12">
//     <select>
//       <option value="" disabled selected>Выбери Предмет</option>
//       <option value="1">Option 1</option>
//       <option value="2">Option 2</option>
//       <option value="3">Option 3</option>
//     </select>
//     <label>Materialize Select</label>
// </div>
