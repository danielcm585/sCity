let num_of_projects = 0

const parseIDR = (amount) => {
  return "IDR "+amount.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ".") +",00"
}

$(document).ready(() => {
  $.get(`/tender/api/project/${id}/`, (project) => {
    num_of_projects = project.registrants.length
<<<<<<< HEAD
    is_closed = (project.registrants.filter((registrant) => registrant.isChosen).length > 0)
=======
>>>>>>> 0cbcf13 (Fix some bugs)
    $('#project-title').text(project.title)
    $('#project-description').text(project.description)
    $('#project-image').append(`
      <img src="${project.photo}" class="mt-4 w-full rounded-lg">
    `)
    $('#num-of-registrants').text(`${num_of_projects} registrants`)
    project.registrants.forEach((registrant) => {
      $('#project-registrants').append(`
        <div id="registrant-${registrant.id}" class="shadow-md rounded-lg flex-col justify-center p-2 hover:bg-gray-200 duration-300">
          <img src="${registrant.company.photo}" class="rounded-t-lg">
          <div class="p-4 w-full flex-col items-center rounded-b-lg">
            <a href="/tender/company/${registrant.company.id}">
              <h1 class="font-bold text-xl text-center">
                ${registrant.company.company_name}
              </h1>
            </a>
            <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
              ${registrant.company.pt_name}
            </p>
            <p class="text-emerald-400 text-center font-bold">
              ${parseIDR(registrant.offer_price)}
            </p>
          </div>
          ${
            project.is_closed ? (
              registrant.is_chosen ? `
                <p class="p-2 rounded-lg bg-emerald-400 text-xs text-white text-center">
                  CHOSEN
                </p>
              ` : `
                <button id="choose-registrant-${registrant.id}" class="p-2 w-full rounded-lg bg-gray-400 text-xs text-white hover:bg-gray-600 duration-300" disabled>
                  CHOOSE
                </button>
              `
            ) : `
              <button id="choose-registrant-${registrant.id}" class="p-2 w-full rounded-lg bg-emerald-400 text-xs text-white hover:bg-emerald-600 duration-300">
                CHOOSE
              </button>
            `
          }
        </div>
      `)
      $(`#choose-registrant-${registrant.id}`).click(() => {
        alert('woy')
        $.ajax({
          url: `/tender/api/registrant/choose/${registrant.id}/`,
          type: 'GET',
          credentials: 'include',
          dataType: 'json',
          success: (registrant) => {
            $('#message-container').html(`
              <div id="js-message" class="absolute top-16 right-4">
                <div class="mt-4 mr-2 flex items-center rounded-lg bg-green-500 border-l-4 border-green-700 py-2 px-3 shadow-md transition ease-in-out hover:scale-110">
                  <div class="text-green-500 rounded-full bg-white mr-3">
                    <svg width="1.8em" height="1.8em" viewBox="0 0 16 16" class="bi bi-check" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.236.236 0 0 1 .02-.022z"/>
                    </svg>
                  </div>
                  <div class="text-white max-w-xs mr-2">
                    Registrant chosen
                  </div>
                </div>
              </div>
            `)
            setTimeout(() => {
              $('#js-message').fadeOut('slow');
            }, 4000)
            location.href = `/tender/project/${id}`
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

  })

  $.get('/tender/api/company/mine/', (companies) => {
    companies.map((company) => {
      $('#choose-company').append(`
        <option value="${company.id}">${company.company_name}</option>
      `)
    })
  })

  $('#tender-modal-open-button').click(() => {
    $('#tender-modal').removeClass('hidden')
  })

  $('.tender-modal-close-button').click(() => {
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
          <div id="registrant-${registrant.id}" class="shadow-md rounded-lg flex-col justify-center p-2 hover:bg-gray-200 duration-300">
            <img src="${registrant.company.photo}" class="rounded-t-lg">
            <div class="p-4 w-full flex-col items-center rounded-b-lg">
              <a href="/tender/company/${registrant.company.id}">
                <h1 class="font-bold text-xl text-center">
                  ${registrant.company.company_name}
                </h1>
              </a>
              <p class="text-gray-500 text-center text-ellipsis overflow-hidden">
                ${registrant.company.pt_name}
              </p>
              <p class="text-emerald-400 text-center font-bold">
                ${parseIDR(registrant.offer_price)}
              </p>
            </div>
            ${
              project.is_closed ? (
                registrant.is_chosen ? `
                  <p class="p-2 rounded-lg bg-emerald-400 text-xs text-white text-center">
                    CHOSEN
                  </p>
                ` : `
                  <button id="choose-registrant-${registrant.id}" class="p-2 w-full rounded-lg bg-gray-400 text-xs text-white hover:bg-gray-600 duration-300" disabled>
                    CHOOSE
                  </button>
                `
              ) : `
                <button id="choose-registrant-${registrant.id}" class="p-2 w-full rounded-lg bg-emerald-400 text-xs text-white hover:bg-emerald-600 duration-300">
                  CHOOSE
                </button>
              `
            }
          </div>
        `)

      },
      error: (err) => {
        $('#tender-modal').addClass('hidden')
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