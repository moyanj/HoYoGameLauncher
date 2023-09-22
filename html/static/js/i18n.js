function _t(text) {
    return new Promise(function(resolve, reject) {
      $.ajax({
        type: "GET",
        url: "/i18n/get",
        dataType: "json",
        data: {
          key: text
        },
        success: function(data) {
          var retText = data["Data"];
          resolve(retText);
        },
        error: function() {
          reject(text);
          bs4pop.notice("无法获取到语言文件", { type: 'danger' });
        }
      });
    });
  }
function t(text){
    return _t(text).then(function(translatedText){
        console.log(translatedText);
        return translatedText;
    }).catch(function(text){
        return text;
    });
}
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
                    $(domEle).text(text);
                }
            }
        )
    }
    );
});



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
                    $(domEle).text(text);
                }
            }
        )
    }
    );
});

