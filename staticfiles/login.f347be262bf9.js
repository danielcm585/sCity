const toggleShowPassword = (e) => {
  const passwordInput = document.getElementById('password-input')
  const eye = document.getElementById('eye')
  const eyeSlash = document.getElementById('eye-slash')
  
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