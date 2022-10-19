$(document).ready(() => {
  $.get('/tender/api/company/', (companies) => {
    companies.forEach((company, idx) => {
      $('#companies-section').append(`
        <div onclick="location.href='/tender/company/${company.id}'" class="shadow-md rounded-lg flex-col justify-center ">
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
  })

  $('#new-company-open-button').click(() => {
    $('#new-company-modal').removeClass('hidden')
  })
  
  $('#new-company-close-button').click(() => {
    $('#new-company-modal').addClass('hidden')
  })

  $('#new-company-form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: '/tender/api/company/',
      type: 'POST',
      credentials: 'include',
      dataType: 'json',
      data: $('#new-company-form').serialize(),
      success: (company) => {
        $('#companies-section').append(`
          <div onclick="location.href='/tender/company/${company.id}'" class="shadow-md rounded-lg flex-col justify-center ">
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
        $('#new-project-modal').addClass('hidden')
      }
    })
  })
})