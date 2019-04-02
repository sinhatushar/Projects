// Get the modal
var modal = document.getElementById("myModal");

var itArray;

// Get the button that opens the modal
var btn = document.getElementById('cart_btn');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// document.write("Checj");
// When the user clicks the button, open the modal 



function checkout(){



	var x = $('#res_id2').html();
	console.log(x);

	var y = {
		"res_id" : x,
		"itArray" : JSON.stringify(itArray),
		csrfmiddlewaretoken : document.getElementsByName('csrfmiddlewaretoken')[0].value
	}
	console.log("Y starts");
	console.log(itArray);
	console.log(y);

	$.ajax({
		type : "POST",
		url : "/cart/",
		data : y,
		success : function(data){
			window.location.replace('/place_order/');
		}
	});

	// $.post('/cart/', y, function(response){
	// 	// if(response == 'success'){console.log('success');}
	// 	// else {console.log('fail')}
	// });

}

$('#logout_btn').click(function(){

	window.alert('Logout Successful !');
  	window.location.replace('/login_user/');
});

btn.onclick = function() {

	// $('.clearfix [name="name"]').each(function(){
	// 	var no = parseInt($(this).val())
	// 	// var currItem = $(this).closest('span').find('.clearfix');
	// 	// var title = currItem.find('.menu-title').text();
	// 	console.log(no);
	// });

	itArray = [];
	var toSetHtml = '<h2 class = "header-h" style = "padding-left:40%;">Cart Details</h2><table style = "width:100%;margin-bottom:40px;">';

	$('.clearfix').each(function(){
		var itemName = $(this).find('.menu-title').html();
		var val = parseInt($(this).find('#itemVal').val());
		var price1 = $(this).find('.menu-price').html();
		var price = parseInt(price1.split(" ")[1]);
		// console.log(itemName);
		// console.log(val);
		console.log(price);

		var cartItem = {
			"name" : itemName,
			"num" : val,
			"price" : price
		}

		var cartIt = {
			"item" : cartItem
		}

		if(cartIt.item.num != 0)
			itArray.push(cartIt);
	});
	toSetHtml = toSetHtml + '<tr> <p class = "cart_style"> <td style = "font-weight:bold;">Item Name</td> <td style = "font-weight:bold;">Quantity</td> <td style = "font-weight:bold;">Price</td></tr>';
	for ( var i=0; i<itArray.length; i++)
	{ 
		var itemName = itArray[i].item.name;
		var num = itArray[i].item.num;
		var price = itArray[i].item.price;
		if(num != 0)
		{
			toSetHtml = toSetHtml + '<tr><p class = "cart_style"> <td>'+ itemName + '</td> <td>'+ num + '</td> <td>' + price + '</td></tr></p>';
		}

	}	

	toSetHtml = toSetHtml + '</table>';
	toSetHtml = toSetHtml + '<a id="place_order" type="button" onclick="checkout()" style = "margin-left:455px;padding:10px;"> Checkout</a>';

	if(itArray.length == 0)
	{
		toSetHtml = '<h2 class = "header-h" align="center">No Items in Cart</h2>';
	}
	//console.log(toSetHtml);
	$(modal).find('.itemsDisplay').html(toSetHtml);
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}