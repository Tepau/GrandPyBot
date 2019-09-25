from app import app
from flask import render_template, request, jsonify
from app.parser import Parser
from app.geocode import GoogleMap
from app.wiki import WikipediaInformation
import os



@app.route('/')
@app.route('/accueil', methods=['GET', 'POST'])
def accueil():
    return render_template("accueil.html", title="GrandPyBot", googleApiKey=os.environ.get('GOOGLE_MAP_API_KEY'))


@app.route('/api/map', methods=['GET', 'POST'])
def question():
    """
    Get input, parse it, get position, get info, get story
    and return latitude, longitude, adress and story in json
    """
    question = request.form['question']
    parser = Parser()
    words = parser.clean_sentence(question)
    latlon = GoogleMap().find_location(words)
    adress = GoogleMap().find_adress(words)
    location = GoogleMap().wiki_search(words)
    infos = WikipediaInformation(location).summary_informations()
    return jsonify(search=words, latlon=latlon, adress=adress, infos=infos)
