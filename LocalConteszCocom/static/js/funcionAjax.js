const form = document.getElementById('login');
form.addEventListener('submit', function(e){
        e.preventDefault();
        let http = new XMLHttpRequest();
        let url = 'index.htm';
        //let url = '/';
        let data = new formData(form);
        http.open('POST',url, true);
        http.onreadystatechange = function(){
            if(http.readystatechange == 4 && http.status == 200){
                let resp = JSON.parse(http.responseText);
                if(resp.response == "true"){
                    setTimeout(function(){
                      window.location.href = "principal.html";
                    },2000);
                }else{
                    alert("incorrecto");
                }
            }
        }
        http.send(data);
});
