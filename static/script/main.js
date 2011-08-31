    var checkBinding = function(weibo_type,checked) {
            if (!checked)
                return;
            var url="/process?type="+weibo_type;
            var xml_req = createXMLRequest();

            xml_req.onreadystatechange = function (){
                                            if (xml_req.readyState==4 && xml_req.status==200){
                                                    response=xml_req.responseText;
                                                    if (response == "false"){
                                                        //do oauth
                                                        //alert("false,need do oauth");
                                                        location.href="http://t.163.com";
                                                    }
                                                }
                                            }
            xml_req.open("GET",url,true);
            xml_req.send();

        }
    var createXMLRequest = function() {
            if (window.ActiveXObject)
                return new ActiveXObject("Microsoft.XMLHTTP");
            else if (window.XMLHttpRequest)
                return new XMLHttpRequest();
            else return false;
        }