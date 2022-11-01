let num_of_items = 0

$(document).ready(() => {
  $.get(`/tender/api/registrant/${registrant_id}/`, (registrant) => {
    console.log(registrant)
    num_of_items = registrant.items.length
  })

  $('#new-item-open-button').click(() => {
    $('#new-item-modal').removeClass('hidden')
  })
  
  $('#new-item-close-button').click(() => {
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
      },
      error: () => alert('gagal')
    })
  })
})