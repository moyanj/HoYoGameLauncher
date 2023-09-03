$(document).ready(function () {
    $(".i18n").each(function (index,domEle) {
        $.ajax(
            {
                type:"GET",
                url:"/i18n/get",
                data:{
                    key: $(domEle).text()
                },
                success:function (data) {
                    console.log(data)
                    $(domEle).text(data);
                }
            }
        )
    }
    );
});
