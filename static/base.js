const drawer = document.getElementById("drawer")

const openMenu = () => {
  drawer.classList.remove("right-[-100vw]")
  drawer.classList.add("right-0")
}

const closeMenu = () => {
  drawer.classList.remove("right-0")
  drawer.classList.add("right-[-100vw]")
}

const message = document.getElementById("message");

setTimeout(() => { 
   message.style.display = "none"; 
}, 3000);