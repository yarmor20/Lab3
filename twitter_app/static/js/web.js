document.getElementById("search-txt")
    .addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("myButton").click();
    }
});

function buttonCode()
{
  alert("Button code executed.");
}