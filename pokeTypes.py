import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Connect the connection to the MongoDB instance, you may need to adjust host:port the same in pokemonNames.py
client = MongoClient("mongodb://127.0.0.1:27017")

# Conneceting db
db = client["pokemonData"] 

# Connecting the collection 
collection = db["pokedex"]  

# Getting base pokemon names for exceptional ones
exceptions_ = {"PikachuPikachu in a cap":"Pikachu", "Gengar*":"Gengar",
 "Mime Jr.":"Mime_Jr.", "Mr. Mime":"Mr._Mime", 
 "Mr. MimeGalarian Mr. Mime": "Mr._Mime", "Mr. Rime":"Mr._Rime",
"Kleavor*":"Kleavor", "Zapdos*":"Zapdos", 
"TaurosPaldean Tauros(Aqua Breed)":"Tauros",
"TaurosPaldean Tauros(Blaze Breed)": "Tauros",
"TaurosPaldean Tauros(Combat Breed)": "Tauros"}


for pokemon in collection.find():
    # Access the id_/name field of the document
    id_ = pokemon["_id"]

    # Check if pokemon name in exception list or consist of multiple names
    if id_ in exceptions_.keys():
        id_ = exceptions_[id_]
    elif len(id_.split()) > 1:
        id_ = id_.split()[1]

    # Scraping pokemons type from its web page
    url = f"https://bulbapedia.bulbagarden.net/wiki/{id_}_(Pokémon)"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', {'class':'mw-parser-output'})
    table_ = div.find('table', {'class': 'roundy'}).find('tbody')
    tr_element = table_.find_all('tr', recursive=False)[1]
    type_ = tr_element.find('table', {'class':'roundy'}).find_all('a')[0].span.b.text

    # Appying pokemon type into pokedex collection
    collection.update_one({"_id": id_}, {"$set": {"type": type_}})


    
   

