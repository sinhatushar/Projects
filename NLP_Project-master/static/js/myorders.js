



var modeel = document.getElementById('newmodeel');

var btn = document.getElementById("showOrders");

var span = document.getElementsByClassName("closer")[0];

// When the user clicks the button, open the modeel 
btn.onclick = function() {
    modeel.style.display = "block";
}

// When the user clicks on <span> (x), close the modeel
span.onclick = function() {
    modeel.style.display = "none";
}

// When the user clicks anywhere outside of the modeel, close it
window.onclick = function(event) 
{
    if (event.target == modeel) {
        modeel.style.display = "none";
    }
}

