$(document).ready(function () {
    // 获取所有图标链接
    var navLinks = $(".nav-link");

    // 添加点击事件监听器
    navLinks.on("click", function (event) {
        event.preventDefault();
        // 隐藏所有内容区域
        $("div[id$='Content']").hide();

        // 移除所有图标的激活状态
        navLinks.removeClass("active");

        // 显示当前图标对应的内容区域并设置为激活状态
        var contentId = $(this).attr("id") + "Content";
        $("#" + contentId).show();
        $(this).addClass("active");
    });

    // 切换暗色模式
    $('#darkModeToggle').change(function () {
        if (this.checked) {
            // 开启暗色模式
            console.log("切换深色模式")
            $("body").addClass("dark-mode");
            $("input").addClass("dark-mode");
            $(".sidebar").addClass("dark-mode");
            $(".nav-link").addClass("dark-mode");
            $(".active").addClass("dark-mode");
            $(".modal-body").addClass("dark-mode");
            $(".modal-footer").addClass("dark-mode");
        } else {
            // 关闭暗色模式
            console.log("切换浅色模式")
            $("body").removeClass("dark-mode");
            $("input").removeClass("dark-mode");
            $(".sidebar").removeClass("dark-mode");
            $(".nav-link").removeClass("dark-mode");
            $(".active").removeClass("dark-mode");
            $(".modal-body").removeClass("dark-mode");
            $(".modal-footer").removeClass("dark-mode");
        }
    });
    $("#startYSGameBtn").on("click", function () {
        $.ajax({
            type: "GET",
            url: "/run/ys",
            success: function (data) {
                // 显示运行成功模态框
                $("#RunOK").modal("show")
            },
            error: function (data) {
                // 显示运行失败模态框
                $("#RunError").modal("show")
            }

        });
    });
    // 崩铁启动逻辑
    $("#startSRGameBtn").on("click", function () {
        $.ajax({
            type: "GET",
            url: "/run/sr",
            success: function (data) {
                // 显示运行成功模态框
                $("#RunOK").modal("show")
            },
            error: function (data) {
                // 显示运行失败模态框
                $("#RunError").modal("show")
            },

        });
    });
    // 设置按钮逻辑
    $("#settingysBtn").on("click", function () {
        $("#APPset").modal("show")

    });
    $("#settingsrBtn").on("click", function () {
        $("#APPset").modal("show")

    });
    $("#aboutBtn").on("click", function () {
        $("#APPset").modal("hide")
        $("#APPabout").modal("show")

    });
    $("#testupdata").on("click", function updata() {
        alert("hello")

    });
    $("#okHide").on("click", function updata() {
        $("#ok").modal("hide")
        location.reload()
        $("#APPinit").modal("hide")

    });
    $("#InitSave").on("click", function () {
        var inputOb = $("#YSuid")
        var dt = inputOb.val();
        var url = "/init?uid=" + dt
        console.log(url)
        $.get(url, function (data) {
            // 显示运行成功模态框
            $("#APPinit").modal("hide")
            $("#ok").modal("show")


        })
        $("#APPinit").modal("hide")
        $("#ok").modal("show")
    });
    // 添加下拉列表变化事件监听
    $("#LangSelect").change(function () {
        // 在下拉列表发生变化时执行的代码
        var selectedValue = $(this).val();
        console.log("选中的值为：" + selectedValue);
        $.ajax({
            url: "/settings/language/"+selectedValue,
            type: "GET",
            success: function () {
                location.reload()
            }
        })
    });

})