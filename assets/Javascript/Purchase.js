$(document).ready(function () {

    $.getJSON('/fetchpurchasecategory', function (data) {

        $.each(data, function (index, item) {

            $('#catid').append($('<option>').text(item[1]).val(item[0]))

        })
    })

    $('#catid').change(function () {

        $.getJSON('/fetchpurchasesubcategory', {ajax: true, catid: $('#catid').val()}, function (data) {

            $('#subcatid').empty()
            $('#subcatid').append($('<option>').text('--Sub Category--'))

            $.each(data, function (index, item) {

                $('#subcatid').append($('<option>').text(item[2]).val(item[1]))

            })

        })

    })

    $('#subcatid').change(function () {

        $.getJSON('/fetchpurchaseproduct', {ajax: true, subcatid: $('#subcatid').val()}, function (data) {

            $('#productid').empty()
            $('#productid').append($('<option>').text('--Product--'))

            $.each(data, function (index, item) {

                $('#productid').append($('<option>').text(item[3]).val(item[2]))

            })

        })

    })

    $('#productid').change(function () {

        $.getJSON('/fetchpurchasefinalproduct', {ajax: true, productid: $('#productid').val()}, function (data) {

            $('#finalproductid').empty()
            $('#finalproductid').append($('<option>').text('--Final Product--'))

            $.each(data, function (index, item) {

                $('#finalproductid').append($('<option>').text(item[4]).val(item[3]))

            })

        })

    })

    $.getJSON('/fetchsupplierjason', function (data) {

        $.each(data, function (index, item) {

            $('#supplierid').append($('<option>').text(item[1]).val(item[0]))

        })
    })

})
