$(document).ready( function() {
    $('#logout').click(function(){
    window.alert("Successfully logged out !");
    window.location.replace('/login_user/');
    });
	// Logo
	var $logo 	= $('#logo');
	 if (location.href.indexOf("#") != -1) {
        if(location.href.substr(location.href.indexOf("#"))){
        	$logo.show();
        }
    }
    
	// Show logo 
	$('#tab-container .tab a').click(function() {
	  $logo.slideDown('slow');
	});
	// Hide logo
	// $('#tab-about').click(function() {
	//   $logo.slideUp('slow');
	// });	
function animMeter(){
    $(".meter > span").each(function() {
                $(this)
                    .data("origWidth", $(this).width())
                    .width(0)
                    .animate({
                        width: $(this).data("origWidth")
                    }, 1200);
            });
}
animMeter();

      $('#tab-container').easytabs({
        animate			: true,
        updateHash		: true,
        transitionIn	: 'slideDown',
        transitionOut	: 'slideUp',
        animationSpeed	: 600,
        tabActiveClass	: 'active'}).bind('easytabs:midTransition', function(event, $clicked, $targetPanel){
            if($targetPanel.selector=='#resume'){
                    animMeter();
            }
        });
    });



$(document).ready( function() {

    // Logo
    var $logo   = $('#logo');
     if (location.href.indexOf("#") != -1) {
        if(location.href.substr(location.href.indexOf("#"))){
            $logo.show();
        }
    }
    
    // Show logo 
    $('#tab-container1 .tab a').click(function() {
      $logo.slideDown('slow');
    });
function animMeter(){
    $(".meter > span").each(function() {
                $(this)
                    .data("origWidth", $(this).width())
                    .width(0)
                    .animate({
                        width: $(this).data("origWidth")
                    }, 1200);
            });
}
animMeter();

      $('#tab-container1').easytabs({
        animate         : true,
        updateHash      : true,
        transitionIn    : 'slideDown',
        transitionOut   : 'slideUp',
        animationSpeed  : 600,
        tabActiveClass  : 'active'}).bind('easytabs:midTransition', function(event, $clicked, $targetPanel){
            if($targetPanel.selector=='#delete_item'){
                    animMeter();
            }
        });

    $('#addForm').submit(function(event){

        event.preventDefault();

        var itemName = $('#item').val();
        var cost = $('#number').val();
        var type = $('#itemType').val();

        var textRegEx = new RegExp('^(?!\\s*$).+');
        var numRegEx = new RegExp('^[0-9]+$');

        if (textRegEx.test(itemName) == 0) 
        {
            $('#err').html('Item Name should not be empty');
            $('#err').fadeToggle('slow');
        }
        else if(numRegEx.test(cost) == 0)
        {
            $('#err').html('Cost should be a number');
            $('#err').fadeToggle('slow');
        }
        else if(type != "NV" && type != "V" && type != "B" && type != "D" )
        {
            $('#err').html('Item type should either be NV, V, B or D');
            $('#err').fadeToggle('slow');
        }
        else
        {
            var myform = $(this);

            window.alert(itemName+' added successfully');
            var posting = $.post(myform.attr("action"),
                                myform.serialize(), function(data){
                                    window.location.replace('/rest_home/');
                                });

        }        
    });

    $('#deleteForm').submit(function(event){

        event.preventDefault();

        var itemName = $('#itemND').val();

        var textRegEx = new RegExp('^(?!\\s*$).+');

        if (textRegEx.test(itemName) == 0) 
        {
            $('#err1').html('Item Name should not be empty');
            $('#err1').fadeToggle('slow');
        }
        else
        {
            var myform = $(this);

            window.alert(itemName+' deleted successfully');
            var posting = $.post(myform.attr("action"),
                                myform.serialize(), function(data){
                                    window.location.replace('/rest_home/');
                                });

        }        
    });

    $('#setForm').submit(function(event){

        event.preventDefault();

        var orderNo = $('#orderNo').val();
        var status = $('#status').val();
        
        var textRegEx = new RegExp('^(?!\\s*$).+');
        var numRegEx = new RegExp('^[0-9]*$');

        if (numRegEx.test(orderNo) == 0) 
        {
            $('#err2').html('Order No. should be a number');
            $('#err2').fadeToggle('slow');
        }
        else if (textRegEx.test(status) == 0) 
        {
            $('#err2').html('Status should not be empty');
            $('#err2').fadeToggle('slow');
        }
        else
        {
            var myform = $(this);

            window.alert('Status of Order '+ orderNo +' set to ' + status);
            var posting = $.post(myform.attr("action"),
                                myform.serialize(), function(data){
                                    window.location.replace('/rest_home/');
                                });

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

    var container3 = $("#err2");

    if (!container3.is(e.target) // if the target of the click isn't the container...
        && container3.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container3.hide();
    }

});
