const openMenu = () => {
  const drawer = document.getElementById("drawer")
  drawer.classList.remove("right-[-100vw]")
  drawer.classList.add("right-0")
}

const closeMenu = () => {
  const drawer = document.getElementById("drawer")
  drawer.classList.remove("right-0")
  drawer.classList.add("right-[-100vw]")
}

const message = document.getElementById("message");

setTimeout(function(){ 
   message.style.display = "none"; 
}, 3000);