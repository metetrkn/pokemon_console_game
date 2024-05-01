import requests, os
from bs4 import BeautifulSoup
from pokemonNames import all_pokemons, soup
from pymongo import MongoClient

# Connect the connection to the MongoDB instance, you may need to adjust host:port the same in pokemonNames.py
client = MongoClient("mongodb://127.0.0.1:27017")

# Conneceting db
db = client["pokemonData"] 

# Connecting the collection 
collection = db["pokedex"]  

# Find all the image links for Pokémon thumbnails
pokemon_thumbnails = []

for img in soup.find_all('img', src=True):
    if 'archives.bulbagarden.net/media/upload' in img['src'] and img['src'].endswith('.png'):
        pokemon_thumbnails.append(img['src'])


image_dict = {all_pokemons[i]: pokemon_thumbnails[i] for i in range(len(all_pokemons))}

for name_, url_ in image_dict.items():
    # Send a GET request to the image URL
    response = requests.get(url_)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the image content to binary data
        image_data = response.content
        # Update existing document or insert a new one
        # Check if a document with the same _id already exists
        if collection.count_documents({"_id": name_}) == 0:
            # Insert a new document if it doesn't exist
            collection.insert_one({"_id": name_, "image_data": image_data})
        else:
            # Update the existing document with the image data
            collection.update_one({"_id": name_}, {"$set": {"image_data": image_data}})

# Closing database connection 
client.close() 