let item_id = 0
let items = []

$(document).ready(() => {
  $.get(`/tender/json/project/${id}/`, (project) => {
    console.log(project)
    $('#title').text(`New Tender to ${project.title}`)
  })

  $.get('/tender/json/company/mine/', (companies) => {
    companies.map((company, idx) => {
      console.log(company.id)
      $('#choose-company').append(`
        <option value="${company.id}">${company.company_name}</option>
      `)
    })
  })

  $('#new-item-open-button').click(() => {
    $('#new-item-modal').removeClass('hidden')
  })
  
  $('#new-item-close-button').click(() => {
    $('#new-item-modal').addClass('hidden')
  })

  $('#save-item').click(() => {
    const parseIDR = (amount) => {
      return "IDR "+amount.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ".") +",00"
    }

    new_item = {
      id: item_id++,
      name: $('#item-name').val(),
      quantity: $('#item-quantity').val(),
      price: $('#item-price').val(),
      description: $('#item-description').val()
    }
    items.push(new_item)
    $('#num-of-items').text(`${items.length} items`)
    $('#items-section').append(`
      <div id="item-${new_item.id}" class="mt-4 p-4 w-full flex justify-between items-center shadow-lg rounded-lg hover:bg-gray-200 duration-300">
        <div>
          <p class="font-bold text-xl">${new_item.quantity} ${new_item.name}</p>
          <p class="text-gray-400">${new_item.description}</p>
          <p class="text-emerald-400">${parseIDR(new_item.price*new_item.quantity)}</p>
        </div>
        <button id="delete-item-${new_item.id}" type="button" class="text-red-400 hover:text-red-600 duration-300">
          Delete
        </button>
      </div>
    `)
    $("#delete-item-"+new_item.id).click(() => {
      items = items.filter((item) => item.id !== new_item.id)
      $(`#item-${new_item.id}`).addClass('hidden')
      $('#num-of-items').text(`${items.length} items`)
    })
    $('#new-item-modal').addClass('hidden')
  })

  $('#save-tender').click(() => {
    console.log('HERE')
    $.ajax({
      url: `/tender/json/registrant/${id}/`,
      type: 'POST',
      credentials: 'include',
      contentType: 'application/json; charset=utf-8',
      dataType: 'text',
      data: JSON.stringify({ 
        company_id: parseInt($('#choose-company').val())
      }),
      success: (registrant) => {
        items.forEach((item) => {
          $.ajax({
            url: '/tender/json/item/',
            type: 'POST',
            credentials: 'include',
            contentType: 'application/json; charset=utf-8',
            dataType: 'text',
            data: JSON.stringify({
              registrant_id: registrant.id,
              ...item
            }),
            error: (err) => alert('Failed to save item')
          })
        })
        location.href = `/tender/project/${id}/`
      }
    })
    console.log('DONE')
  })
})