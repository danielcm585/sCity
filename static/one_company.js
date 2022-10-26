$(document).ready(() => {
  $.get(`/tender/api/company/${company_id}`, (company) => {
    console.log(company)
    $('#company-name').text(company.company_name)
    $('#company-details').append(`
      <h2 class="text-xl font-bold">PT Name</h2>
      <p id="company_pt_name">${company.pt_name}</p>
      <h2 class="mt-4 text-xl font-bold">NPWP</h2>
      <p id="company_pt_name">${company.npwp}</p>
    `)
    $('#num-of-projects').text(`${company.projects.length} projects`)
    company.projects.forEach((project) => {
      console.log(project)
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
})