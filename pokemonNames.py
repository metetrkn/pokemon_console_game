import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Ability"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all Pokémon names under the specified section
generations_pokemon = ["Generation_I_families", "Generation_II_families", "Generation_III_families", "Generation_IV_families",
                       "Generation_V_families", "Generation_VI_families", "Generation_VII_families", "Generation_VIII_families", "Generation_IX_families"]

all_pokemons = list()
for section in generations_pokemon:
    pokemon_list = soup.find("span", {"id": section}).find_next("table").find_all("td", {"style": "text-align:left"})

    # Extract the Pokémon names
    pokemon_names = [pokemon.text.strip() for pokemon in pokemon_list]

    # Print the Pokémon names
    for name in pokemon_names:
        all_pokemons.append(name)

print(all_pokemons)