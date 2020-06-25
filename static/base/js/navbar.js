const navslide = () =>{
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.navlinks')
  const navlinks=document.querySelectorAll('.navlinks li')

  burger.addEventListener('click',function () {
    nav.classList.toggle('nav-active');

      navlinks.forEach((link, index) => {
        if(link.style.animation){
          link.style.animation=``
        }
        else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${index/7+0.4}s`;
        }


      });

      burger.classList.toggle('toggle')

  });



}

// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

navslide();
