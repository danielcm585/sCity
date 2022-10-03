const openMenu = () => {
  console.log("HERE")
  let drawer = document.getElementById("drawer")
  drawer.classList.remove("right-[-100vw]")
  drawer.classList.add("right-0")
}

const closeMenu = () => {
  let drawer = document.getElementById("drawer")
  drawer.classList.remove("right-0")
  drawer.classList.add("right-[-100vw]")
}
