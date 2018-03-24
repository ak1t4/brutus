var url = "https://" + document.domain + "/account/apikeys"; 
var xmlhttp = new XMLHttpRequest(); 
xmlhttp.open("GET", url,true);
xmlhttp.responseType = 'text';

 // subscribe to this event before you send your request.
 xmlhttp.onreadystatechange=function() {
  if (xmlhttp.readyState==4) {
   //alert the user that a response now exists in the responseTest property.
   //alert(xmlhttp.responseText);
     alert(document.domain);
     var parser = new DOMParser(); var doc = parser.parseFromString(xmlhttp.responseText, "text/html"); var elem = doc.getElementById('accountDetailsTable'); alert(elem.innerHTML); prompt(elem.innerHTML);
   // And to view in firebug
  // console.log('xhr',xmlhttp)
  }
 }
 xmlhttp.send(null);
