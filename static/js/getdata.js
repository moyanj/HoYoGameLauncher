$(document).ready(function () {
    $.ajax({
        type:"GET",
        url:"/ifinit",
        success:function(data){
            if(data=="not ok"){
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

})