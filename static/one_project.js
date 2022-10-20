$(document).ready(() => {
  $.get(`/tender/api/project/${id}/`, (project) => {
    $('#project-title').text(project.title)
    $('#project-description').text(project.description)
    $('#project-image').append(`
      <img src="${project.photo}" class="mt-4 w-full rounded-lg">
    `)
  })

  $.get('/tender/api/company/mine/', (companies) => {
    companies.map((company, idx) => {
      console.log(company.id)
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

  $('registrant-form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: `/tender/api/registrant/${id}/`,
      type: 'POST',
      credentials: 'include',
      dataType: 'json',
      data: $('#registrant-form').serialize(),
      success: (registrant) => {
        alert(berhasil)
        console.log(registrant)
        $('#tender-modal').addClass('hidden')
      }
    })
  })
})