$(document).ready(function () {

    $.getJSON('/fetchcategory',function(data) {

        $.each(data,function (index,item) {

            $('#I').append($('<option>').text(item[1]).val(item[0]))

        })
    })

    $('#I').change(function () {

        $.getJSON('/fetchsubcategory',{ajax:true,I:$('#I').val()},function(data) {

            $('#SCI').empty()
            $('#SCI').append($('<option>').text('--Select Sub Category--'))

            $.each(data,function (index,item) {

                $('#SCI').append($('<option>').text(item[2]).val(item[1]))

            })

        })

    })



})