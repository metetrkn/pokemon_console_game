import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Create a connection to the MongoDB instance, you may adjust it based on your mongodb host:port
client = MongoClient("mongodb://127.0.0.1:27017")

# Select,Craete the database 
db = client["pokemonData"] 

# Select the collection 
collection = db["pokedex"]  

# URL of the webpage to scrape
url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Ability"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all Pokémon names under the specified section, for further generations list can be enhanced with the ones below
generations_pokemon = ["Generation_I_families"]
#, "Generation_II_families", "Generation_III_families", "Generation_IV_families",
#  "Generation_V_families", "Generation_VI_families", "Generation_VII_families", "Generation_VIII_families", "Generation_IX_families"

all_pokemons = list()
for section in generations_pokemon:
    pokemon_list = soup.find("span", {"id": section}).find_next("table").find_all("td", {"style": "text-align:left"})

    # Extract the Pokémon names
    pokemon_names = [pokemon.text.strip() for pokemon in pokemon_list]

    # Print the Pokémon names
    for name in pokemon_names:
        all_pokemons.append(name)
        # Check if a document with the same _id already exists
        if collection.count_documents({"_id": name}) == 0:
            # Insert a new document if it doesn't exist
            collection.insert_one({"_id": name})

# Closing database connection 
client.close() 

