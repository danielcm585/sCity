const toggleShowPassword1 = (e) => {
  const passwordInput = document.getElementById('password1-input')
  const eye = document.getElementById('eye1')
  const eyeSlash = document.getElementById('eye1-slash')
  
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

const toggleShowPassword2 = (e) => {
  const passwordInput = document.getElementById('password2-input')
  const eye = document.getElementById('eye2')
  const eyeSlash = document.getElementById('eye2-slash')
  
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

document.getElementById("password1-toggler").addEventListener("click", toggleShowPassword1)
document.getElementById("password2-toggler").addEventListener("click", toggleShowPassword2)