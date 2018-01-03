// <li class="bold active">
//               <a class="collapsible-header waves-effect waves-cyan active">
//                 <span class="nav-text">Dashboard</span>
//               </a>
              
//             </li>


function subjectDelete(id){
	token = getFromStorage("token");
	toDelSubject(id, token).then(function(data){
		if (data.status != 200){
			alert(data);
		}
		else{
			window.location.reload();
		}
	});
}

function appendSubject(data){
	var delBtn = document.createElement('button');
	delBtn.className = "subjectDelete waves-effect waves-cyan";
	delBtn.appendChild(document.createTextNode('удалить'))
	delBtn.setAttribute("onclick", "subjectDelete($)".replace('$', data.id));


	var li = document.createElement('li');
	li.setAttribute('dbid', data.id);
	li.setAttribute('class', 'bold subjectList');
	li.setAttribute('onclick', "loadQuestions($)".replace('$', data.id))
	var a = document.createElement('a');
	a.setAttribute('class', "waves-effect waves-cyan");
	var span = document.createElement('span');
	span.setAttribute('class', "nav-text");
	var text = document.createTextNode(data.name);
	span.appendChild(text);
	a.appendChild(span);
	li.appendChild(a);
	li.appendChild(delBtn);
	li.appendChild(document.createElement('hr'))

	var des = document.getElementById('left-sidebar-nav').childNodes[1];
	// console.log(li);
	des.insertBefore(li, document.getElementById('desctop-subject-insert-flag'));
	// console.log(li);
}

function addNewSubject(){
	// <div>
 //      <p>Добавить Предмет</p>
 //      <input type="text">
 //      <button>Сохранить</button>
 //    </div>
	content = document.getElementById('content')
	if(content.childNodes.length > 0){
		
		content.childNodes.forEach(function(data, index, arr){
			content.removeChild(data);
		});
	}

	div = document.createElement('div');
	p = document.createElement('p');
	p.appendChild(document.createTextNode('Добавить Предмет'));
	input = document.createElement('input');
	input.setAttribute('type', 'text');
	input.setAttribute('id', 'addNewSubjectText')
	btn = document.createElement('button');
	btn.setAttribute('onclick', 'checkToAddSubject()');
	btn.appendChild(document.createTextNode('Сохранить'));
	div.appendChild(p);
	div.appendChild(input);
	div.appendChild(btn);
	content.appendChild(div);
}

function checkToAddSubject(){
	text = document.getElementById('addNewSubjectText').value;
	if(!text){
		alert("empty");
	}
	else{
		newSubject(text, getFromStorage('user_id'), getFromStorage('token')).then(function(data){
			if(data.status != 200){
				alert(data.message);
			}
			else{
				window.location.reload();
			}
		})
	}
	
}

