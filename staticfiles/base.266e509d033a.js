$(document).ready(() => {
  $('#drawer-open-button').click(() => {
    $('#drawer').removeClass('right-[-100vw]')
    $('#drawer').addClass('right-0')
  })
  
  $('#drawer-close-button').click(() => {
    $('#drawer').removeClass('right-0')
    $('#drawer').addClass('right-[-100vw]')
  })
})

// FIXME: Fix the message timeout
// const message = document.getElementById("message")

// setTimeout(() => { 
//   if (message == null) return
//   message.style.display = "none"
// }, 3000);