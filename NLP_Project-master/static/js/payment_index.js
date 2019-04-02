$(function () {
  $('[data-toggle="popover"]').popover();
  
  $('#cvc').on('click', function(){
    if ( $('.cvc-preview-container').hasClass('hide') ) {
      $('.cvc-preview-container').removeClass('hide');
    } else {
      $('.cvc-preview-container').addClass('hide');
    }    
  });
  
  $('.cvc-preview-container').on('click', function(){
    $(this).addClass('hide');
  });

});

$('#PayButton').click(function(){

  // window.alert('Hi');

  var addRegEx = new RegExp('^(?!\\s*$).+');
  var mobileRegEx = new RegExp('[789][0-9]{9}');

  var name = $('#name').val();
  var add = $('#add').val();
  var mobile = $('#phone').val();

  console.log(mobile);

  if(addRegEx.test(name) == 0)
  {
    $('#err').html('Name field should not be empty');
    $('#err').fadeToggle('slow');
  }
  else if(addRegEx.test(add) == 0)
  {
    $('#err').html('Address field should not be empty');
    $('#err').fadeToggle('slow');
  }
  else if(mobileRegEx.test(mobile) == 0)
  {
    $('#err').html('Invalid Mobile Number');
    $('#err').fadeToggle('slow');
  }
  else
  {

    var y = {
      "address" : add,
      csrfmiddlewaretoken : document.getElementsByName('csrfmiddlewaretoken')[0].value
    }

    $.ajax({
   
      type : "POST",
      url : "/checkout/",
      async : false,
      dataType : "text",
      data : y,
      success : function(data){
        $('#PayButton').hide();
        var placed = $('#placed');
        placed.html('Order Placed. Order No. - '+data);
        placed.fadeToggle('slow');
        $('#homePage').fadeToggle('slow');
        // window.alert('Order placed successfully. Order No. : '+data);
        // window.location.replace('/home/');
      }
    });
  }
  
  });

$('#homePage').click(function(){
  window.location.replace('/home/');
});

$(document).mouseup(function (e)
{
    var container1 = $("#err");

    if (!container1.is(e.target) // if the target of the click isn't the container...
        && container1.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container1.hide();
    }

});