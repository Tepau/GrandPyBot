var form = document.querySelector("form");

$("form").on("submit", function(e){
	e.preventDefault();
	$('#contenu_section').hide();
	$('#chargement').show();
	var phrase = e.target.elements.question.value
	var data = new FormData(form);
	ajaxPost("/api/map", data, function(reponse){
		elements = JSON.parse(reponse)	
		document.getElementById("phrase").style.display = "block";
		form.style.display = "none";
		var sectionElt = document.querySelector("section");
		var pElt = document.createElement("p");
		pElt.textContent = "Bien sûr fiston, voici l'adresse : " + elements["adresse"];
		sectionElt.appendChild(pElt);
		var divMapElt = document.createElement("div");
		divMapElt.id = "map";
		divMapElt.style.height = "60%";
		divMapElt.style.width = "60%";
		divMapElt.style.margin = "auto";
		sectionElt.appendChild(divMapElt);
		function initMap() {
    		var map = new google.maps.Map(document.getElementById('map'), {
    			center: {lat: elements["latlon"][0], lng: elements["latlon"][1]},
    			zoom: 8
  			});
    		// Nous ajoutons un marqueur
			var marker = new google.maps.Marker({
				// Nous définissons sa position (syntaxe json)
				position: {lat: elements["latlon"][0], lng: elements["latlon"][1]},
				// Nous définissons à quelle carte il est ajouté
				map: map
			});
		}

		initMap();
		$('#chargement').hide();
		$('#contenu_section').show();
	
		var wikiElt = document.createElement("p");
		wikiElt.textContent = "Reste ici j'ai autre chose à te raconter. " + elements["infos"];
		sectionElt.appendChild(wikiElt);
		wikiElt.style.textAlign = "justify";
	});

});

