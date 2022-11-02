function show(data) {
    let content = "";
    for (let i = 0; i < data.length; i++) {
        let message = data[i].fields.is_confirm ? "Verified" : "Not Verified";
        let color = data[i].fields.is_confirm ? "green" : "red";
        content += `
              <br />
              <div id="${data[i].pk}" class="p-10 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
                  <h5 class="p-4 mb-2 text-2xl font-bold tracking-tight text-gray-900">${data[i].fields.username
            }</h5>
                  <p  class="px-4 mb-3 font-normal text-700"><b>date: </b>${data[i].fields.date
            }</p>
                  <p  class="text-right px-4 mb-3 font-normal text-700"><b>Type: </b>${data[i].fields.waste_type
            }</p>
                  <p  class="text-right px-4 mb-3 font-normal text-700"><b>Weight: </b>${data[i].fields.weight
            } Kg</p>
                  <p  class="text-right px-4 mb-3 font-normal text-700"><b>Income: </b>Rp.${income(
                data[i].fields.waste_type,
                Number(data[i].fields.weight)
            )}</p>
                  <div class="flex">
                  <div class="items-center justify-center">
                  <p id="${data[i].pk}-update" style="color: ${color}" class="text-xl flex-1 p-4 mb-3 font-normal text-700">${message}</p>
                  </div>
                  <div class="item-center justify-center">
                  <button id="waste-update" onClick="{update(${data[i].pk})}" class="p-2 mt-4 bg-white  border border-emerald-400 rounded-lg shadow-md text-emerald-400 hover:bg-emerald-600 hover:text-white duration-300" >Update
                   </button>
                   <button  id="waste-delete" onClick="{delete_waste(${data[i].pk})}" class="p-2 mt-4 bg-white  border border-red-500 rounded-lg shadow-md text-red-500 hover:bg-red-500 hover:text-white duration-300" >Delete
                   </button>
                  </div>
                  </div>
                  <br>
              </div>
        `;
        $(".content").html(content);
    }
}

function income(type, weight) {
    if (type === "Plastic") {
        return weight * 3000;
    } else if (type === "Metal") {
        return weight * 4000;
    } else if (type === "Paper") {
        return weight * 2000;
    } else if (type === "Glass") {
        return weight * 1000;
    }
}

function main() {
    $.get("/waste/json/admin", function (data, status) {
        show(data);
    });
}
main();


function update(id) {
    $.ajax({
        type: 'POST',
        url: `update/${id}`,
        success: function () {
            var msg = $(`#${id}-update`).text()
            var new_msg = msg == "Verified" ? "Not Verified" : "Verified";
            $(`#${id}-update`).text(new_msg)

            $(`#${id}-update`).css('color', 'red')
            if (new_msg == "Verified"){
                $(`#${id}-update`).css('color', 'green')
            }
        }
    })
}

function delete_waste(id){
    $.ajax({
        type: 'POST',
        url: `delete/${id}`,
        success: function () {
            $(`#${id}`).remove();
        }
    })
}