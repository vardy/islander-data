url = "https://islands.ibpp.me"

payload = {
    "id": "THIS IS AN ID",
    "data": "Hi Kat"
}

var xhr = new XMLHttpRequest();
xhr.open("POST", url);
xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
   if (xhr.readyState === 4) {
      console.log(xhr.status);
      console.log(xhr.responseText);
   }
};

xhr.send(JSON.stringify(payload));