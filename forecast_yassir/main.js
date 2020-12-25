window.addEventListener(
    "load",
    function () {
        var form = document.getElementById("coords-form");
    form.addEventListener(
        "submit",
        function (event) {
            event.preventDefault();
            if (form.checkValidity() === false) {
                event.stopPropagation();
            } else {
              let SERVER_URL=document.getElementById('server-url-input').value;
              let datastring=JSON.stringify($("#coords-form").serialize());
              console.log(datastring)
              console.log(datastring);

            let requestOptions={
                type: "POST",
                url: SERVER_URL+"estimate",
                "Content-Type": "application/json",
               
                data: datastring
              };


              $.ajax({
                ...requestOptions,
                success: function (response) {
                  console.log(response);
                  displayLoading(false);
                
                },
                error: function (error) {
                  console.error(error);
                  
                }
                

                
              });
              


          }
        }
    );


    }

);

function request_estimation(){
    var form = document.getElementById("coords-form");
    form.addEventListener(
        "submit",
        function (event) {
            event.preventDefault();
            if (form.checkValidity() === false) {
                event.stopPropagation();
            } else {
              let SERVER_URL=document.getElementById('server-url-input').value;
              let datastring=$("#coords-form").serialize();

            let requestOptions={
                type: "POST",
                url: SERVER_URL+"estimate",
               
                data: datastring
              };


              $.ajax({
                ...requestOptions,
                success: function (response) {
                  console.log(response);
                  displayLoading(false);
                
                },
                error: function (error) {
                  console.error(error);
                  
                }
                

                
              });
              


          }
        }
    );

}


  