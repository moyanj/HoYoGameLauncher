if (location.href == "https://user.mihoyo.com/#/account/home"){
    document.body.innerHTML = '';
    let div = document.body;
    let cookie = document.cookie.split("; ")
    div.innerHTML = '<h1>Stoken：</h1><p id="stoken"></p><h1>Login_ticket：</h1><p id="login_ticket"></p>'
    cookie.forEach(item => {
        if (item.indexOf("stoken") != -1){
            let stoken = item.split("=")[1]
            console.log(stoken)
            document.getElementById("stoken").innerHTML="<p>"+stoken+"</p>"

        }
        if (item.indexOf("login_ticket") != -1){
            let login_ticket = item.split("=")[1]
            console.log(login_ticket)
            document.getElementById("login_ticket").innerHTML="<p>"+login_ticket+"</p>"
        }
    })
} else {
    alert("请跳转至https://user.mihoyo.com/#/account/home")
    location.href = "https://user.mihoyo.com/#/account/home"
}