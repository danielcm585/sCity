let num_of_items = 0

$(document).ready(() => {
  $.get(`/tender/api/registrant/${registrant_id}/`, (registrant) => {
    num_of_items = registrant.items.length
  })

  $('#new-item-open-button').click(() => {
    $('#new-item-modal').removeClass('hidden')
  })
  
  $('.new-item-close-button').click(() => {
    $('#new-item-modal').addClass('hidden')
  })

  $('#new-item-form').submit((e) => {
    const parseIDR = (amount) => {
      return "IDR "+amount.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ".") +",00"
    }

    e.preventDefault()
    $.ajax({
      url: `/tender/api/item/${id}/`,
      type: 'POST',
      credentials: 'include',
      dataType: 'json',
      data: $('#new-item-form').serialize(),
      success: (item) => {
        $('#num-of-items').text(`${++num_of_items} items`)
        $('#items-section').append(`
          <div id="item-${item.id}" class="mt-4 p-4 w-full flex justify-between items-center shadow-lg rounded-lg hover:bg-gray-200 duration-300">
            <div>
              <p class="font-bold text-xl">${item.quantity} ${item.name}</p>
              <p class="text-gray-400">${item.description}</p>
              <p class="text-emerald-400">${parseIDR(item.price*item.quantity)}</p>
            </div>
            <button id="delete-item-${item.id}" type="button" class="text-red-400 hover:text-red-600 duration-300">
              Delete
            </button>
          </div>
        `)
        $(`#delete-item-${item.id}`).click(() => {
          items = items.filter((item) => item.id !== item.id)
          $(`#item-${item.id}`).addClass('hidden')
          $('#num-of-items').text(`${items.length} items`)
        })
        $('#new-item-modal').addClass('hidden')
        $('#message-container').html(`
          <div id="js-message" class="absolute top-16 right-4">
            <div class="mt-4 mr-2 flex items-center rounded-lg bg-green-500 border-l-4 border-green-700 py-2 px-3 shadow-md transition ease-in-out hover:scale-110">
              <div class="text-green-500 rounded-full bg-white mr-3">
                <svg width="1.8em" height="1.8em" viewBox="0 0 16 16" class="bi bi-check" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.236.236 0 0 1 .02-.022z"/>
                </svg>
              </div>
              <div class="text-white max-w-xs mr-2">
                Registered successfully
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