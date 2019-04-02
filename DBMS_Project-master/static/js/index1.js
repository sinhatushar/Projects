$('#logout').click(function(){

  window.alert('Logout Successful !');
  window.location.replace('/login_user/');

});

$('#showOrders').click(function(){
  $.get("/showorders/",function(data){
    console.log(data);
    console.log('Hi');
  });
});
    

$('input[type="submit"]').mousedown(function(){
    $(this).css('background', '#2ecc71');
});


$('input[type="submit"]').mouseup(function(){
  $(this).css('background', '#1abc9c');
});

$(document).mouseup(function (e)
{
    var container1 = $(".userDD");

    if (!container1.is(e.target) // if the target of the click isn't the container...
        && container1.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container1.hide();
        $('#userDet').removeClass('green');
    }
});

window.onload = function(){

  var unameJS = localStorage.getItem('username');
  var unameJ = JSON.parse(unameJS);

  var username = unameJ.username;
  console.log(username);

  $('#userDet').html(username);

}

function myFun()
{
  $('.userDD').fadeToggle('slow');
  $(this).toggleClass('green');
}


 



