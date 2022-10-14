$(document).ready(() => {
  $.get(`/tender/json/project/${id}/`, (project) => {
    $('#project-section').append(`
      <div class="w-full flex justify-between items-center">
        <div class="flex items-center">
          <button onclick="history.back()">
            <?xml version="1.0" ?><!DOCTYPE svg  PUBLIC '-//W3C//DTD SVG 1.1//EN'  'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'><svg height="28px" id="Layer_1" style="enable-background:new 0 0 512 512;" version="1.1" viewBox="0 0 512 512" width="28px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><polygon points="352,128.4 319.7,96 160,256 160,256 160,256 319.7,416 352,383.6 224.7,256 "/></svg>
          </button>
          <h1 class="ml-2 text-2xl font-bold">
            ${project.title}
          </h1>
        </div>
        <button onclick="location.href='/tender/join-tender/${id}/'" class="bg-emerald-400 text-white py-2 px-3 rounded-lg shadow-md hover:bg-emerald-600 duration-300">
          Tender
        </button>
      </div>
      <img src="${project.photo}" class="mt-4 w-full rounded-lg">
      <div class="mt-4">
        <p class="text-gray-500">
          ${project.description}
        </p>
      </div>
    `)
  })
})