//Make a AJAX POST call
// Takes into parameters the target URL, the data to be sent and the callback function called on success
// The isJson parameter is used to indicate whether the send is for JSON data
function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // Calls the callback function by passing the response of the request
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
            $('#loading').hide();
            var sectionElt = document.querySelector("section");
		    var pElt = document.createElement("p");
		    pElt.textContent = "Erreur de Recherche, actualisez la page";
		    sectionElt.appendChild(pElt);
        }
    });
    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });
    if (isJson) {
        // Set the contents of the request as JSON
        req.setRequestHeader("Content-Type", "application/json");
        // Transform data from JSON to text before sending
        data = JSON.stringify(data);
    }
    req.send(data);
}