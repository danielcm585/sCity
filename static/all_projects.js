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
        $('#message-container').html(`
          <div id="js-message" class="absolute top-16 right-4">
            <div class="mt-4 mr-2 flex items-center rounded-lg bg-green-500 border-l-4 border-green-700 py-2 px-3 shadow-md transition ease-in-out hover:scale-110">
              <div class="text-green-500 rounded-full bg-white mr-3">
                <svg width="1.8em" height="1.8em" viewBox="0 0 16 16" class="bi bi-check" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.236.236 0 0 1 .02-.022z"/>
                </svg>
              </div>
              <div class="text-white max-w-xs mr-2">
                Project created
              </div>
            </div>
          </div>
        `)
        setTimeout(() => {
          $('#js-message').fadeOut('slow');
        }, 4000)
      },
      error: (err) => {
        $('#new-project-modal').addClass('hidden')
        $('#message-container').html(`
          <div id="js-message" class="absolute top-16 right-4">
            <div class="mt-4 ml-2 flex w-70 bg-red-500 items-center rounded-lg border-l-4 border-red-700 py-2 px-3 shadow-md transition ease-in-out hover:scale-110">
              <div class="text-red-500 rounded-full bg-white mr-3">
                <svg width="1.8em" height="1.8em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                  <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                </svg>
              </div>
              <div class="text-white max-w-xs mr-2">
                ${err.responseJSON}
              </div>
            </div>
          </div>
        `)
        setTimeout(() => {
          $('#js-message').fadeOut('slow');
        }, 4000)
      }
    })
  })
})