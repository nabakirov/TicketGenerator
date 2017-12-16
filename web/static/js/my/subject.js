// <li class="bold active">
//               <a class="collapsible-header waves-effect waves-cyan active">
//                 <span class="nav-text">Dashboard</span>
//               </a>
              
//             </li>



function appendSubject(data){
	var li = document.createElement('li');
	li.setAttribute('dbid', data.id);
	li.setAttribute('class', 'bold');
	li.setAttribute('onclick', "loadQuestions($)".replace('$', data.id))
	var a = document.createElement('a');
	a.setAttribute('class', "collapsible-header waves-effect waves-cyan active");
	var span = document.createElement('span');
	span.setAttribute('class', "nav-text");
	var text = document.createTextNode(data.name);
	span.appendChild(text);
	a.appendChild(span);
	li.appendChild(a);

	var des = document.getElementById('left-sidebar-nav').childNodes[1];
	var mob = document.getElementById('nav-mobile').childNodes[1];
	// console.log(li);
	mob.insertBefore(li, mob.childNodes[0]);
	des.insertBefore(li, des.childNodes[0]);
	// console.log(li);
}