function helloStranger() {
    var txt;
    var person = prompt("Please enter your name:", "Mils");
    if (person == null || person == "") {
        txt = "User cancelled the prompt.";
    } else {
        txt = "Hello " + person + "! How are you today?";
    }
    document.getElementById("demo").innerHTML = txt;
}
function newSubscribe() {
    var txt;
    var email = prompt("Please enter your email:", "5601xxxx@kmitl.ac.th");
    if (email== null || email == "") {
        txt = "Incorrect input";
    } else {
        txt = "We've sent you an email to " + email;
    }
    document.getElementById("demo").innerHTML = txt;
}
function newDoc() {
    window.location.assign("https://mesodiar.wordpress.com/")
}
/* slide_show */
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}
function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  console.log(slides[0]);
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}
function thumbUpanddown(x) {
    x.classList.toggle("fa-thumbs-down");
}