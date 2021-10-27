$(document).ready(function () {

    $.getJSON('/getcategoryjson', function (data) {

        $.each(data, function (index, item) {

            $('#CI').append($('<option>').text(item[1]).val(item[0]))

        })
    })


})
