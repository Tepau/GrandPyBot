var form = document.querySelector("form");

// Add an event when the form is validated
$("form").on("submit", function(e){
	e.preventDefault();
	//Mask the form and show image during loading time
	$('#section_content').hide();
	$('#loading').show();
	var data = new FormData(form);
	ajaxPost("/api/map", data, function(response){
		elements = JSON.parse(response)
		console.log(elements);
		document.getElementById("sentence").style.display = "block";
		form.style.display = "none";
		var sectionElt = document.querySelector("section");
		var pElt = document.createElement("p");
		pElt.textContent = "Bien sûr fiston, voici l'adresse : " + elements["adress"];
		sectionElt.insertAdjacentHTML(afterBegin, pElt);
		var divMapElt = document.getElementById("map");
		divMapElt.style.display = "block";
		function initMap() {
    		var map = new google.maps.Map(divMapElt, {
    			center: {lat: elements["latlon"][0], lng: elements["latlon"][1]},
    			zoom: 8
  			});
    		//  Add a marker to the map
			var marker = new google.maps.Marker({
				// Marker's position)
				position: {lat: elements["latlon"][0], lng: elements["latlon"][1]},
				// Map's marker
				map: map
			});
		}

		initMap();
		// Mask the loading picture and print a response
		$('#loading').hide();


	    // Add a paragraph containing wikipedia info
		var wikiElt = document.createElement("p");
		wikiElt.textContent = "Reste ici j'ai autre chose à te raconter. " + elements["infos"];
		sectionElt.appendChild(wikiElt);
		wikiElt.style.textAlign = "justify";
		wikiElt.style.padding = "0px 17px 0px 17px";
	});

});

