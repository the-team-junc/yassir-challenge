window.addEventListener("load", function () {
  var form = document.getElementById("coords-form");
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (form.checkValidity() === false) {
      event.stopPropagation();
    } else {
      let SERVER_URL = document.getElementById("server-url-input").value;
      let datastring = $("#coords-form").serialize();
      //   let datastring=JSON.stringify($("#coords-form").serialize());
      console.log(datastring);
      console.log(datastring);

      let requestOptions = {
        type: "POST",
        url: SERVER_URL + "estimate",
        // "Content-Type": "application/json",
        // headers: {
        //     'Access-Control-Allow-Origin': '*',
        // },

        data: datastring,
      };

      $.ajax({
        ...requestOptions,
        success: function (response) {
          console.log(response);
          $('#eta-container').append(`Estimated Travel Duration : ${response.eta}`)
        },
        error: function (error) {
          console.error(error);
        },
      });
    }
  });
});

function request_estimation(data) {
  let SERVER_URL = document.getElementById("server-url-input").value;

  let requestOptions = {
    type: "POST",
    url: SERVER_URL + "estimate",

    data: data,
  };

  $.ajax({
    ...requestOptions,
    success: function (response) {
      console.log(response);
      $('#eta-container').append(`Estimated Travel Duration : ${response.eta}`)
    },
    error: function (error) {
      console.error(error);
    },
  });
}
