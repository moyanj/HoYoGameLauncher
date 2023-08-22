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
})