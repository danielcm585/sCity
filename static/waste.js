var total_income = 0;

function show(data) {
    let content = "";
    for (let i = 0; i < data.length; i++) {
        let message = data[i].fields.is_confirm ? "Verified" : "Not verified";
        let color = data[i].fields.is_confirm ? "green" : "red";
        if (data[i].fields.is_confirm == true) {
            total_income =
                total_income +
                income(data[i].fields.waste_type, Number(data[i].fields.weight));
        }
        content += `
              <br />
              <div class="box p-10 bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
                  <h5 class="p-4 mb-2 text-2xl font-bold tracking-tight text-gray-900">${data[i].fields.waste_type
            }</h5>
                  <p class="px-4 mb-3 font-normal text-700">date: ${data[i].fields.date
            }</p>
                  <p  class="text-right px-4 mb-3 font-normal text-700"><b>Weight: </b>${data[i].fields.weight
            } Kg</p>
                  <p  class="text-right px-4 mb-3 font-normal text-700"><b>Income: </b>Rp.${income(
                data[i].fields.waste_type,
                Number(data[i].fields.weight)
            )
                .toFixed(2)
                .replace(/\d(?=(\d{3})+\.)/g, "$&,")}</p>
                  <p style="color: ${color}" class=" text-xl p-4 mb-3 font-normal text-700">${message}</p>
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

function show_total() {
    total_display = `<h1>Total Income: Rp.${total_income
        .toFixed(2)
        .replace(/\d(?=(\d{3})+\.)/g, "$&,")}</h1>`;
    $(".total").html(total_display);
}

// GET
function main() {
    $.get("/waste/json/", function (data, status) {
        show(data);
        show_total();
    });
}
main();

$(document).on('submit', '#new-waste-form', function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'add/',
        data: $("#new-waste-form").serialize(),
        success: function(){
            removeModal()
            main()
        }
    })
})

function addModal() {
    $("#new-waste-modal").removeClass("hidden");
}

function removeModal() {
    $("#new-waste-modal").addClass("hidden");
}
