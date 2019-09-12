from app import app
from flask import render_template, request, jsonify
from app.parser import Parser
from app.geocode import GoogleMap
from app.wiki import Wiki


@app.route('/')
@app.route('/accueil', methods=['GET', 'POST'])
def accueil():
    return render_template("accueil.html", title="GrandPyBot")


@app.route('/api/map', methods=['GET', 'POST'])
def question():
    """
    Get input, parse it, get position, get info, get story
    and return latitude, longitude, adress and story in json
    """
    question = request.form['question']
    parser = Parser()
    words = parser.cleanSentence(question)
    latlon = GoogleMap(words).findLocation()
    adresse = GoogleMap(words).findAdress()
    location = GoogleMap(words).wikiSearch()
    infos = Wiki(location).infos_sup()
    return jsonify(search=words, latlon=latlon, adresse=adresse, infos=infos)
