import requests, os
from bs4 import BeautifulSoup
from pokemonNames import all_pokemons, soup

# Create a folder to save the images if it doesn't exist
if not os.path.exists("pokemon_images"):
    os.makedirs("pokemon_images")

# Find all the image links for Pokémon thumbnails
pokemon_thumbnails = []

for img in soup.find_all('img', src=True):
    if 'archives.bulbagarden.net/media/upload' in img['src'] and img['src'].endswith('.png'):
        pokemon_thumbnails.append("https:" + img['src'])


image_dict = {all_pokemons[i]: pokemon_thumbnails[i] for i in range(len(all_pokemons))}

for name_, url_ in image_dict.items():
    filename = f"pokemon_images/{name_}.png"
    # Send a GET request to the image URL
    response = requests.get(url_)
     # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the image to a file
        with open(filename, "wb") as f:
            f.write(response.content)