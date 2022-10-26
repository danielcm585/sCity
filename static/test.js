$(document).ready(() => {
  $.get('/tender/test/project/', (projects) => {
    console.log(projects)
  })
})