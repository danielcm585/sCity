$(document).on("submit", function(e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/healthcare/add_keluhan/",
        data: {
            dokter: $("#id_dokter").find(":selected").val(),
            keluhan: $("#id_appointment_date").val(),
            noHP: $("#id_phone_number").val(),
            csrfmiddlewaretoken: "{{ csrf_token }}",
        },
        dataType: "json",
        success: function() {
            alert("Data added")
            window.location.href = "/healthcare/";
        },
    });
});

(document).ready(function() {
    let tab = '';
    $.ajax({
        url: "/healthcare/show_healthcare",
        type: "GET",
        dataType: "json",
        success: function(resp) {
            let counter = 0;
            for (let i of resp) {
                counter += 1;
                let statusAppointment = i.fields.Appointment_status;
                AppointmentMessage = statusAppointment ? `<p class="bg-emerald-400 w-fit rounded-2xl p-2">Appointment Confirmed</p>` : `<p class="bg-red-500 w-fit rounded-2xl p-2">Appointment Unchecked</p>`
                tab += `
              <div class="" id="${i.pk}div">
                            <div id="${i.pk}" class="bg-white rounded-2xl p-6 flex w-fit flex-col gap-2 hover:drop-shadow-lg transition duration-300 ease-in-out">
                                <div>
                                  <p>Status Appointment : ${AppointmentMessage} </p>
                                </div>
                            </div>
                        </div>
                        `;
            };
        }
    })
});