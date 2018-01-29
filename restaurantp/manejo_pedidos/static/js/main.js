$(document).ready(function(){
	$('#reader').html5_qrcode(function(data){
			$('#read').html(data);
			console.log(data);
			if(data == '0.0.0.0:8000/cliente'){
				location.href='0.0.0.0:8000/cliente';
			}

		},
		function(error){
			$('#read_error').html(error);
		}, function(videoError){
			$('#vid_error').html(videoError);
		}
	);
});
