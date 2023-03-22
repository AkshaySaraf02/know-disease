var img = document.getElementById("uploaded-img");
img.src = ""
var loadFile = function (event) {
    img.src = URL.createObjectURL(event.target.files[0])
}

var imgUploaded = 0;

var change = function (event) {
    imgUploaded += 1
    $("#btn-predict").show()
    $("#result").hide()
}

var enableSubmit = function (event) {
    if (imgUploaded > 0) {
        document.querySelector(".analyze").textContent = "Analyzing..."
        setTimeout(() => {
            document.querySelector(".analyze").textContent = "Analyze";
        }, 1000);
    }
    var formFields = document.getElementById('form1').elements;
    console.log(formFields['lung-img'].files.length > 0); // True if file selected

    var form_data = new FormData($('#form1')[0]);

    console.log(form_data)
    // Make prediction by calling api /predict
    $.ajax({
        type: 'POST',
        url: '/analyzeTB',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        async: true,
        success: function (data) {
            $('#result').text("Report:" + "   " + data);
            console.log('Success!');
            $("#btn-predict").hide()
            $("#result").show()
        },
    });
    console.log("END")
}