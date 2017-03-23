$(document).ready(function () {
    $("#submit").click(function () {
        event.preventDefault();
        // document.getElementById("myform").submit();
        var formData = $("#myform").serialize();
        $.ajax({
            url: '/',
            data: formData,
            error: function () {
                console.log('Failed!');
            },
            success: function (data) {
                var a = JSON.parse(data);
                console.log('Success!', a["success"]);
            },
            type: 'POST'
        });
    });
});

