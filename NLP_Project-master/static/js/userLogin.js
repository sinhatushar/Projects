

$(function(){

	$("#cus_form").submit(function(event){
		console.log('Hi');
		event.preventDefault();

		var username = $('#regUsername').val();
		var password1 = $('#password1').val();
		var password2 = $('#password2').val();
		var name = $('#name').val();
		var phoneNo = $('#phone_number').val();

		var emailRegEx = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$');
		var passRegEx = new RegExp('^[a-zA-Z0-9._%+-]{8,}');
		var mobileRegEx = new RegExp('[789][0-9]{9}');

		if(emailRegEx.test(username) == 0)
		{
			$('#err1').html('Invalid Email Address');
            $('#err1').fadeToggle('slow');
		}
		else if(passRegEx.test(password1) == 0)
		{
			$('#err1').html('Invalid Password');
            $('#err1').fadeToggle('slow');
		}
		else if(password1 != password2)
		{
			$('#err1').html('Passwords don\'t match');
            $('#err1').fadeToggle('slow');
		}
		else if(mobileRegEx.test(phoneNo) == 0)
		{
			$('#err1').html('Invalid Mobile Number');
            $('#err1').fadeToggle('slow');
		}
		else
		{
			console.log(username);
			console.log(password1);
			console.log(password2);
			console.log(name);
			console.log(phone_number);
			var regform = $(this);

			// window.alert("Successfully Registered");
			// window.location.replace('/login_user/');

			var posting = $.post(regform.attr("action"),
								regform.serialize());

			posting.done(function(data){
				console.log(data);
				window.alert("Successfully Registered");
				window.location.replace('/login_user/');
			});

			posting.fail(function(data){
				console.log('fail');
				window.alert("Error in Registration, Please try again !");
				window.location.replace('/login_user/');
			});
		}



		
	});

	$('#login_form').submit(function(event){
		console.log('Hi in login_form');
		event.preventDefault();

		var username = $('#logUsername').val();
		var password = $('#password').val();

		var emailRegEx = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$');
		var passRegEx = new RegExp('^[a-zA-Z0-9._%+-]{8,}');

        if (emailRegEx.test(username) == 0) 
        {
            $('#err').html('Invalid Email Address');
            $('#err').fadeToggle('slow');
        }
        else
        {
        	if(passRegEx.test(password) == 0)
        	{
        		$('#err').html('Invalid Password');
            	$('#err').fadeToggle('slow');
        	}
        	else
        	{
        		var myform = $(this);

				// var jso = {"username" : username};
				// localStorage.setItem('username',JSON.stringify(jso));
				// window.location.replace('/home/');
				var posting = $.post(myform.attr("action"),
									myform.serialize());

				posting.done(function(data){
					console.log(data);
					console.log(data.success);
					console.log(data.username);
					if(data.success == '1')
					{
				
						var jso = {"username" : username};
						localStorage.setItem('username',JSON.stringify(jso));
						window.location.replace('/home/');
					}
					else
					{
						alert('Invalid Credentials');
						window.location.replace('/login_user/');
					}
				});

				posting.fail(function(data){
					console.log('fail');
					alert('Invalid Credentials');
					window.location.replace('/login_user/');
				});
        	}
        }


		
	});
});

$(document).mouseup(function (e)
{
    var container1 = $("#err");

    if (!container1.is(e.target) // if the target of the click isn't the container...
        && container1.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container1.hide();
    }

    var container2 = $("#err1");

    if (!container2.is(e.target) // if the target of the click isn't the container...
        && container2.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container2.hide();
    }
});