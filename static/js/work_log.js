$(function() {
    let value;
    let tab;
    $('#radios input').click(function () {
        value = $(this).val();
        tab = $(this).attr("data-choose");
        $('#'+ tab).siblings().css('display','none');
        $('#'+ tab).css('display','block');
        if(tab=="tab5" || tab=="tab4"){
            $('.right-block .btn-add').css('display','inline-block');
        }
        else{
            $('.right-block .btn-add').css('display','none');
        }
    });
    $('#addOne').click(function () {
        console.log(tab);
    })
    $('#save').click(function () {
        let params=null;
        let options = $("#select-pro option:selected").val();
        let address1 = $('#input2').val();
        let time = $('#input3').val();
        switch (tab) {
            case 'tab1'://途中
                params={
                    state:1,
                    proName:options,
                    address:address1,
                    time:time
                };
        }
        $.ajax({
            type: $('#addForm').attr('method'),
            url: "{% url 'system-rbac:menu_detail' %}",
            data: params,
            cache: false,
            success: function (msg) {
                console.log(msg);
                alert(msg);
            }
        });
    })
});
