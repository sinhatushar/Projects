$(function(){

	$("#resReg").submit(function(event){
		console.log('Hi');
		event.preventDefault();

		var username = $('#usernamesignup').val();
		var password1 = $('#passwordsignup').val();
		var password2 = $('#passwordsignup_confirm').val();
		var name = $('#resName').val();
		var phoneNo = $('#mobileNo').val();
		var address = $('#resAddress').val();
		var cuisine = $('#cuisine').val();

		var emailRegEx = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$');
		var passRegEx = new RegExp('^[a-zA-Z0-9._%+-]{8,}');
		var mobileRegEx = new RegExp('[789][0-9]{9}');
		var textRegEx = new RegExp('^(?!\\s*$).+');

		if(emailRegEx.test(username) == 0)
		{
			$('#err1').html('Invalid Email Address');
            $('#err1').fadeToggle('slow');
		}
		else if(passRegEx.test(password1) == 0)
		{
			console.log("Hererere");
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
		else if(textRegEx.test(address) == 0)
		{
			$('#err1').html('Address should not be empty');
            $('#err1').fadeToggle('slow');
		}
		else if(textRegEx.test(cuisine) == 0)
		{
			$('#err1').html('Cuisine should not be empty');
            $('#err1').fadeToggle('slow');
		}
		else
		{
			var regform = $(this);

			// window.alert("Successfully Registered");
			// window.location.replace('./login_restaurant/');

			var posting = $.post(regform.attr("action"),
								regform.serialize());

			posting.done(function(data){
				console.log(data);
				window.alert("Successfully Registered");
				window.location.replace('/login_restaurant/');
			});

			posting.fail(function(data){
				console.log('fail');
				window.alert("Error in Registration, Please try again !")
				window.location.replace('/login_restaurant/');
			});
		}



		
	});

	$('#resLogin').submit(function(event){
		console.log('Hi in login_form');
		event.preventDefault();

		var username = $('#username').val();
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

				// var jso = {"resUsername" : username};
				// localStorage.setItem('resUsername',JSON.stringify(jso));
				// window.location.replace('/rest_home/');
				var posting = $.post(myform.attr("action"),
									myform.serialize());

				posting.done(function(data){
					console.log(data);
					console.log(data.success);
					console.log(data.username);
					if(data.success == '1')
					{
				
						var jso = {"restUsername" : username};
						localStorage.setItem('restUsername',JSON.stringify(jso));
						window.location.replace('/rest_home/');
					}
					else
					{
						alert('Invalid Credentials');
						window.location.replace('/login_restaurant/');
					}
				});

				posting.fail(function(data){
					console.log('fail');
					alert('Invalid Credentials');
					window.location.replace('/login_restaurant/');
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