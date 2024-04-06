import requests
from bs4 import BeautifulSoup
from pokemonNames import all_pokemons

# Contains each pokemon's names and their skills
pokedex = {}

# Function to scrape the table after the "Base stats" header from a given URL
def scrape_base_stats_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the header with id "Base_stats"
    base_stats_header = soup.find('span', {'id': 'Base_stats'})
    if base_stats_header:
        # Find the next table after the header
        base_stats_table = base_stats_header.find_next('table')
        if base_stats_table:
            return base_stats_table
    return None

# Scraping the table after "Base stats" for each Pokemon
for pokemon_name in all_pokemons:
    url = f"https://bulbapedia.bulbagarden.net/wiki/{pokemon_name}_(Pok%C3%A9mon)"
    # Scraping the table after "Base stats"  for each Pokemon
    base_stats_table = scrape_base_stats_table(url)
    
    if base_stats_table:
        # Extracting tbody element which contains data
        body_table = base_stats_table.find("tbody")

        # Table rows which contains pokemons skills
        skills = body_table.find_all("tr")
        skills = skills[2:-1]

        # Pokemons agility stats dictionary
        stats_dict = {}

        # Extracting pokemon's HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Total into stats_dict
        for tr in skills:
            th = tr.find("th")
            # Extract the text from the th element
            key = th.text.strip().split(':')[0]
            value = th.text.strip().split(':')[1]
            # Add the key-value pair to the dictionary
            stats_dict[key] = value

        pokedex[pokemon_name] = stats_dict

# Print the extracted Pokemon data
for pokemon, stats in pokedex.items():
    print(f"{pokemon}: {stats}")
