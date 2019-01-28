const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// makes alert messages disappear after 4 sec
setTimeout(function(){
	$('#message').fadeOut('slow');
}, 4000);
