$(document).ready(() => {
  $.get('/tender/api/project/', (projects) => {
    num_of_projects = projects.length
    projects.forEach((project, idx) => {
      $('#projects-section').append(`
        <div onclick="location.href='/tender/project/${project.id}'" class="shadow-md rounded-lg flex-col justify-center hover:bg-gray-200 duration-300">
          <img src="${project.photo}" class="rounded-t-lg">
          <div class="p-4 w-full rounded-b-lg">
            <h1 class="font-bold text-xl text-center">
              ${project.title}
            </h1>
            <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
              ${project.description}
            </p>
          </div>
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
    $.ajax({
      url: '/tender/api/project/',
      type: 'POST',
      credentials: 'include',
      dataType: 'json',
      data: $('#new-project-form').serialize(),
      success: (project) => {
        $('#projects-section').append(`
          <div onclick="location.href='/tender/project/${project.id}'" class="shadow-md rounded-lg flex-col justify-center hover:bg-gray-200 duration-300">
            <img src="${project.photo}" class="rounded-t-lg">
            <div class="p-4 w-full rounded-b-lg">
              <h1 class="font-bold text-xl text-center">
                ${project.title}
              </h1>
              <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
                ${project.description}
              </p>
            </div>
          </div>
        `)
        $('#new-project-modal').addClass('hidden')
      }
    })
  })
})