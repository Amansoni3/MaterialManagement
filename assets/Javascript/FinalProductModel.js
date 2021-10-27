$(document).ready(function () {

    function setdata(data){

        data=data.replaceAll("(","")
        data=data.replaceAll(")","")
        data=data.replaceAll("'","")
        data=data.split(",")

        return data
    }

    $(".modal-button").click(function() {

        var target = $(this).data("target");
        var data= $(this).attr('data')
        data=setdata(data)
        $("#fpid").val(data[3].trim())
        $("#oldpic").val(data[12].trim())
        $("#catid").append($("<option>").text(data[15]).val(data[0]))
        $("#subcatid").append($("<option>").text(data[16]).val(data[1]))
        $("#productid").append($("<option>").text(data[17]).val(data[2]))
        $("#fpname").val(data[4].trim())
        $("#size").val(data[5].trim())
        $("#sizeunit").val(data[6].trim())
        $("#weight").val(data[7].trim())
        $("#weightunit").val(data[8].trim())
        $("#colour").val(data[9].trim())
        $("#price").val(data[10].trim())
        $("#stock").val(data[11].trim())
        $("#pico").attr('src',"/static/FinalProductImages/"+data[12].trim())






        $("html").addClass("is-clipped");
        $(target).addClass("is-active");

    });

    $(".modal-close").click(function() {
        $("html").removeClass("is-clipped");
        $(this).parent().removeClass("is-active");

    });



    $(".modal-image").click(function() {

        var target = $(this).data("target");
        var data= $(this).attr('data')
        data=setdata(data)
        $("#finalid").val(data[3].trim())
        $("#oldimg").val(data[12].trim())
        $('#finalname').html(data[4])
        $("#image").attr('src',"/static/FinalProductImages/"+data[12].trim())
        $('#picture').change(function () {
        var file=picture.files[0]
        pic.src=URL.createObjectURL(file)
})

        $("html").addClass("is-clipped");
        $(target).addClass("is-active");

    });

    $(".modal-close").click(function() {
        $("html").removeClass("is-clipped");
        $(this).parent().removeClass("is-active");

    });





})
