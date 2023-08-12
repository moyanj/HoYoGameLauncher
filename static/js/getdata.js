$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "/ifinit",
        success: function (data) {
            if (data == "not ok") {
                $("#APPinit").show();
            }
        }

    })
    // 获取游戏路径
    $.ajax({
        type: "GET",
        url: "/get/gamepath",
        dataType: 'json',
        success: function (data) {

            // 获取原神和崩铁的路径
            let yspath = data.ys;
            let srpath = data.sr;
            console.log("原神路径：" + yspath);
            console.log("崩铁路径：" + srpath);
            //写入输入框
            $("#YSPath").val(yspath);
            $("#SRPath").val(srpath);
        }
    });
    // 获取游戏名
    $.ajax({
        type: "GET",
        url: "/username",
        success: function (data) {
            console.log("玩家名称：" + data);
            //写入输入框
            $("#user-name").text(data);

        }
    });
    // 发送 AJAX 请求
    $.ajax({
        url: "/get/lang",
        method: "GET",
        dataType: "json",
        success: function (data) {
            // 在成功回调函数中处理返回的数据
            var selectElement = $("#LangSelect");

            // 遍历数据并添加选项
            for (var i = 0; i < data.length; i++) {
                selectElement.append("<option value='" + data[i] + "'>" + data[i] + "</option>");
            }
            $.ajax({
                type: "GET",
                url: "/get/language",
                success: function (data) {
                    let defaultOption = data;
                    $("#LangSelect").val(defaultOption);
                    console.log("默认语言：" + $("#LangSelect").val());
                }
            });
        },
        error: function (xhr, status, error) {
            // 处理请求错误
            console.log("请求错误：" + error);
        }
    });

})