const toggleShowPassword = (e) => {
  console.log('HERE')

  let passwordInput = document.getElementById('password-input')
  let eye = document.getElementById('eye')
  let eyeSlash = document.getElementById('eye-slash')
  
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text'
    eye.classList.add('hidden')
    eyeSlash.classList.remove('hidden')
  }
  else {
    passwordInput.type = 'password'
    eye.classList.remove('hidden')
    eyeSlash.classList.add('hidden')
  }

  e.preventDefault()
}

document.getElementById("password-toggler").addEventListener("click", toggleShowPassword)