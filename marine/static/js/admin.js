$(document).ready(function () {
    const card = (data) => `
      
    <a href="/marine/single/${data.pk}/" class="group">
      <div class="aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-lg bg-gray-200 xl:aspect-w-7 xl:aspect-h-8">
        <img src="${data.fields.photo_url}" alt="${data.fields.description}." class="h-full w-full object-cover object-center group-hover:opacity-75">
      </div>
      <h3 class="mt-4 text-sm text-gray-700">${data.fields.title}</h3>
      <p class="mt-1 text-lg font-medium text-gray-900">Rp${data.fields.price}</p>
    </a>
      `
    const addCard = (data) => {
      return $('#items').append(card(data))
    }

    const removeCard = (item) => {
      $(`#${item.pk}`).click(function () {
        $.ajax({
          url: `/marine/delete/${item.pk}`,
          type: 'DELETE',
          success: function (response) {
            $(`#${item.pk}-card`).remove()
          },
        })
      })
    }

    $.get('/marine/json', function (todo) {
      todo.map((task) => {
        addCard(task)
        removeCard(task)
      })
    })

    $('#add-item').click(function () {
      if ($('#title').val() && $('#description').val() && $('#photo').val() && $('#price').val() && $('#contact_name').val() && $('#contact_number').val()) {
        $.post(
          '/marine/add/',
          {
            photo: $('#photo').val(),
            title: $('#title').val(),
            description: $('#description').val(),
            price: $('#price').val(),
            contact_name: $('#contact_name').val(),
            contact_number: $('#contact_number').val(),
          },
          function (res, status) {
            if (status == 'success') {
              addCard(res)
              $('#title').val('')
              $('#description').val('')
              $('#contact_number').val('')
              $('#contact_name').val('')
              $('#price').val('')
              removeCard(res)
              console.log("kontol")
            }
          },
        )
      }
    })
  })