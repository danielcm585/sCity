$(document).ready(() => {
  $.get(`/tender/api/company/${company_id}`, (company) => {
    $('#company-details').append(`
      <h2 class="text-xl font-bold">PT Name</h2>
      <p id="company_pt_name">${company.company_name}</p>
      <h2 class="mt-4 text-xl font-bold">NPWP</h2>
      <p id="company_pt_name">${company.npwp}</p>
      <h2 class="mt-4 text-xl font-bold">Projects</h2>
    `)
    $('#company-name').text(company.company_name)
  })
})