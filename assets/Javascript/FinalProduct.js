$(document).ready(function () {

    $.getJSON('/fetchsizeunit', function (data) {

        $.each(data, function (index, item) {

            $('#sizeunit').append($('<option>').text(item[1]).val(item[0]))

        })
    })

    $.getJSON('/fetchweightunit', function (data) {

        $.each(data, function (index, item) {

            $('#weightunit').append($('<option>').text(item[1]).val(item[0]))

        })
    })


})