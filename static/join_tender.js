let my_companies = []

$(document).ready(() => {
  $.get(`/tender/json/project/${id}/`, (project) => {
    // $.get('/tender/json/company/mine/', (companies) => {
    //   my_companies = companies
    // })

    $('#new-tender-section').append(`
      <div class="flex">
        <button onclick="history.back()">
          <?xml version="1.0" ?><!DOCTYPE svg  PUBLIC '-//W3C//DTD SVG 1.1//EN'  'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'><svg height="28px" id="Layer_1" style="enable-background:new 0 0 512 512;" version="1.1" viewBox="0 0 512 512" width="28px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><polygon points="352,128.4 319.7,96 160,256 160,256 160,256 319.7,416 352,383.6 224.7,256 "/></svg>
        </button>
        <h1 class="ml-2 text-2xl font-bold">
          New Tender to ${project.title}
        </h1>
      </div>
      <div class="mt-4">
        <form id="new-tender-form">
          <div>
            <p>Company</p>
            <select name="company" id="choose-company" class="form-control w-full rounded-lg">
              ${my_companies.map((company, idx) => `
                <option value="${company.id}">${company.company_name}</option>
              `)}
            </select>
          </div>
        </form>
      </div>
    `)
  })
})