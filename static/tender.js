$(document).ready(() => {
  $.get('/tender/json/project/', (projects) => {
    projects
      .filter((project, idx) => idx < 4)
      .forEach((project, idx) => {
        console.log(project)
        $('#projects-section').append(`
          <div>
            Project ${idx}
          </div>
        `)
      })
  })

  $('#new-project-open-button').click(() => {
    $('#new-project-modal').removeClass('hidden')
  })
  
  $('#new-project-close-button').click(() => {
    $('#new-project-modal').addClass('hidden')
  })

  $('#new-project-form').submit((e) => {
    e.preventDefault()
    
  })
})