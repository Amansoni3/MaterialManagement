$(document).ready(function () {

    $.getJSON('/fetchfinalcagteory',function(data) {

        $.each(data,function (index,item) {

            $('#catid').append($('<option>').text(item[1]).val(item[0]))

        })
    })

    $('#catid').change(function () {

        $.getJSON('/fetchfinalsubcategory',{ajax:true,catid:$('#catid').val()},function(data) {

            $('#subcatid').empty()
            $('#subcatid').append($('<option>').text('--Sub Category--'))

            $.each(data,function (index,item) {

                $('#subcatid').append($('<option>').text(item[2]).val(item[1]))

            })

        })

    })

    $('#subcatid').change(function () {

        $.getJSON('/fetchfinalproduct',{ajax:true,subcatid:$('#subcatid').val()},function(data) {

            $('#productid').empty()
            $('#productid').append($('<option>').text('--Product--'))

            $.each(data,function (index,item) {

                $('#productid').append($('<option>').text(item[3]).val(item[2]))

            })

        })

    })


$('#picture').change(function () {
    var file=picture.files[0]
    pic.src=URL.createObjectURL(file)
})


})