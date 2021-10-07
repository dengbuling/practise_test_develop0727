//function submitForm(){
//    $.ajax({
//        url:"http://127.0.0.1:8000/user/Login/",
//        type:'POST',
//        data:$('#f1').serialize(),
//        success:function(arg){
//            console.log(arg)
//        }
//
//    })
//
//}

function submitForm(){
    var user_name = document.getElementById("user_name")
    var user_password = document.getElementById("user_password")
    var formData = new FormData()
    formData.user_name = user_name.value
    formData.user_password = user_password.value
//    document.getElementById("file").files[0]拿到文件列表去第一个
    formData.append("user_nnn",document.getElementById("file").files[0])
    var ajax = new XMLHttpRequest()
    ajax.onreadystatechange = function(){
        if(ajax.readyState==4){



            var json=JSON.parse(ajax.responseText)
            console.log(json)
            console.log(json.file_path)
            var tt1 = document.createElement('img')
            tt1.src = "/"+json.file_path

            var tt2 = document.createElement('span')
            var node = document.createTextNode(json.data.user_name);
            tt2.appendChild(node)

//            tt2.innerText = json.data.user_name
            tt2.id = "f2"

            var u9 = document.getElementById("user_name").getElementsByTagName("span")
            if(u9){
                console.log("99999")
//                console.log(u9.innerTextNode)
                document.getElementById("user_name").removeChild(u9)

//                document.getElementById("nnn").replaceChild(tt2,u9)
            }


            document.getElementById("nnn").appendChild(tt2)
            document.getElementById("ff3").appendChild(tt1)


        }
    }
    ajax.open('POST',"http://127.0.0.1:8000/user/Login/")
//    aaa.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    ajax.send(formData)
}