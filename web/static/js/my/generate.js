function generate(){

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
			p.appendChild(document.createTextNode('Генерировать Билеты'));
			input = document.createElement('input');
			input.setAttribute('type', 'text');
			input.placeholder = 'Кол-во билетов'
			input.setAttribute('id', 'makeTicketCount')
			input2 = document.createElement('input');
			input2.setAttribute('type', 'text');
			input2.placeholder = 'Кол-во вопросов'
			input2.setAttribute('id', 'makeQuestionCount')
			btn = document.createElement('button');
			btn.setAttribute('onclick', 'checkToGenerate()');
			btn.appendChild(document.createTextNode('Сохранить'));

			div.appendChild(p);
			div.appendChild(selectDiv);
			div.appendChild(input);
			div.appendChild(input2);
			div.appendChild(btn);

			content.appendChild(div);
			$(document).ready(function() {
			    $('select').material_select();
			  });

		}
	});
}

function checkToGenerate(){
	subject = document.getElementById('listOfSubjects');
	subjectInd = subject.selectedIndex;
	makeQuestionCount = document.getElementById('makeQuestionCount').value;
	makeTicketCount = document.getElementById('makeTicketCount').value;
	if(subjectInd == 0 || !makeQuestionCount || !makeTicketCount){
		alert("Заполни");
	}
	else{
		sid = subject.options[subjectInd].value;
		uid = getFromStorage('user_id');
		token = getFromStorage('token');
		toGenerate(makeTicketCount, makeQuestionCount, uid, sid, token).then(function(data){
			if(data.status != 200){
				alert(data.message);
			}
			else{
				content = document.getElementById('content');
				a = document.createElement('a');
				a.href = data.download + '&token=' + token;
				a.appendChild(document.createTextNode('Скачать'));
				content.appendChild(a);
			}
		})
	}
}