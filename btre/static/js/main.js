const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// makes alert messages disappear after 3 sec
setTimeout(function(){
	$('#message').fadeOut('slow');
}, 3000);
