$(document).ready(function () {
    $(".i18n").each(function (index,domEle) {
        $.ajax(
            {
                type:"GET",
                url:"/i18n/get",
                // 解析json
                dataType:"json",
                data:{
                    key: $(domEle).text()
                },
                success:function (data) {
                    // 获取键为data的数据
                    var text = data["Data"]
                    console.log(data)
                    $(domEle).text(text);
                }
            }
        )
    }
    );
});
