let num_of_projects = 0
let num_of_companies = 0

$(document).ready(() => {
  $.get('/tender/json/project/', (projects) => {
    num_of_projects = projects.length
    projects
      .filter((project, idx) => idx < 6)
      .forEach((project, idx) => {
        $('#projects-section').append(`
          <div class="shadow-md rounded-lg flex-col justify-center hover:bg-gray-200 duration-300">
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
    if (num_of_projects > 6) {
      $('#more-projects').removeClass('hidden')
    }
  })

  $.get('/tender/json/company/', (companies) => {
    num_of_companies = companies.length
    companies
      .filter((company, idx) => idx < 6)
      .forEach((company, idx) => {
        $('#companies-section').append(`
          <div class="shadow-md rounded-lg flex-col justify-center ">
            <img src="${company.photo}" class="rounded-t-lg">
            <div class="p-4 w-full rounded-b-lg">
              <h1 class="font-bold text-xl text-center">
                ${company.company_name}
              </h1>
              <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
                ${company.pt_name}
              </p>
            </div>
          </div>
        `)
      })
    if (num_of_companies > 6) {
      $('#more-companies').removeClass('hidden')
    }
  })

  $('#new-project-open-button').click(() => {
    $('#new-project-modal').removeClass('hidden')
  })
  
  $('#new-project-close-button').click(() => {
    $('#new-project-modal').addClass('hidden')
  })
  
  $('#new-company-open-button').click(() => {
    $('#new-company-modal').removeClass('hidden')
  })
  
  $('#new-company-close-button').click(() => {
    $('#new-company-modal').addClass('hidden')
  })

  $('#new-project-form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: '/tender/json/project/',
      type: 'POST',
      credentials: 'include',
      dataType: 'json',
      data: $('#new-project-form').serialize(),
      success: (project) => {
        if (++num_of_projects <= 6) {
          $('#projects-section').append(`
            <div class="shadow-md rounded-lg flex-col justify-center hover:bg-gray-200 duration-300">
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
        }
        if (num_of_projects > 6) {
          $('more-projects').removeClass('hidden')
        }
        $('#new-project-modal').addClass('hidden')
      }
    })
  })
  $('#new-company-form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: '/tender/json/company/',
      type: 'POST',
      credentials: 'include',
      dataType: 'json',
      data: $('#new-company-form').serialize(),
      success: (company) => {
        if (++num_of_companies <= 6) {
          $('#companies-section').append(`
            <div class="shadow-md rounded-lg flex-col justify-center ">
              <img src="${company.photo}" class="rounded-t-lg">
              <div class="p-4 w-full rounded-b-lg">
                <h1 class="font-bold text-xl text-center">
                  ${company.company_name}
                </h1>
                <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
                  ${company.pt_name}
                </p>
              </div>
            </div>
          `)
        }
        if (num_of_projects > 6) {
          $('more-projects').removeClass('hidden')
        }
        $('#new-project-modal').addClass('hidden')
      }
    })
  })
})