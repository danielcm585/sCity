let num_of_projects = 0

$(document).ready(() => {
  $.get(`/tender/api/project/${id}/`, (project) => {
    $('#project-title').text(project.title)
    $('#project-description').text(project.description)
    $('#project-image').append(`
      <img src="${project.photo}" class="mt-4 w-full rounded-lg">
    `)
    if (project.registrants) {
      num_of_projects = project.registrants.length
      $('#num-of-registrants').text(`${num_of_projects} registrants`)
      project.registrants.forEach((registrant) => {
        $('#project-registrants').append(`
          <div onclick="location.href='/tender/company/${registrant.company.id}'" class="shadow-md rounded-lg flex-col justify-center ">
            <img src="${registrant.company.photo}" class="rounded-t-lg">
            <div class="p-4 w-full rounded-b-lg">
              <h1 class="font-bold text-xl text-center">
                ${registrant.company.company_name}
              </h1>
              <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
                ${registrant.company.pt_name}
              </p>
            </div>
          </div>
        `)
      })
    }
  })

  $.get('/tender/api/company/mine/', (companies) => {
    companies.map((company, idx) => {
      $('#choose-company').append(`
        <option value="${company.id}">${company.company_name}</option>
      `)
    })
  })

  $('#tender-modal-open-button').click(() => {
    $('#tender-modal').removeClass('hidden')
  })

  $('#tender-modal-close-button').click(() => {
    $('#tender-modal').addClass('hidden')
  })

  $('#registrant-form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: `/tender/api/registrant/${id}/`,
      type: 'POST',
      credentials: 'include',
      dataType: 'json',
      data: $('#registrant-form').serialize(),
      success: (registrant) => {
        $('#tender-modal').addClass('hidden')
        $('#num-of-registrants').text(`${++num_of_projects} registrants`)
        $('#project-registrants').append(`
          <div onclick="location.href='/tender/company/${registrant.company.id}'" class="shadow-md rounded-lg flex-col justify-center ">
            <img src="${registrant.company.photo}" class="rounded-t-lg">
            <div class="p-4 w-full rounded-b-lg">
              <h1 class="font-bold text-xl text-center">
                ${registrant.company.company_name}
              </h1>
              <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
                ${registrant.company.pt_name}
              </p>
            </div>
          </div>
        `)
      },
      error: () => {
        alert('gagal')
      }
    })
  })
})