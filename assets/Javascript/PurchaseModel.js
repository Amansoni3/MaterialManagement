$(document).ready(function () {

    function setdata(data) {

        data = data.replaceAll("(", "")
        data = data.replaceAll(")", "")
        data = data.replaceAll("'", "")
        data = data.split(",")

        return data
    }

    $(".modal-button").click(function () {

        var target = $(this).data("target");
        var data = $(this).attr('data')
        data = setdata(data)
        $("#transactionid").val(data[0].trim())
        $("#employeid").val(data[1].trim())
        $("#catid").append($("<option>").text(data[10]).val(data[2]))
        $("#subcatid").append($("<option>").text(data[11]).val(data[3]))
        $("#productid").append($("<option>").text(data[12]).val(data[4]))
        $("#finalproductid").append($("<option>").text(data[13]).val(data[5]))
        $("#datepurchase").val(data[6].trim())
        $("#supplierid").append($("<option>").text(data[14]).val(data[7]))
        $("#stock").val(data[8].trim())
        $("#amount").val(data[9].trim())

        $("html").addClass("is-clipped");
        $(target).addClass("is-active");

    });

    $(".modal-close").click(function () {
        $("html").removeClass("is-clipped");
        $(this).parent().removeClass("is-active");

    });
})
