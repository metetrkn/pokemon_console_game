from bs4 import BeautifulSoup
import requests
from unicodedata import numeric
from pokemonNames import all_pokemons

# Function to scrape the table after the "Type_effectiveness" header from a given URL
def scrape_base_stats_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the header with id "Base_stats"
    base_stats_header = soup.find('span', {'id': 'Type_effectiveness'})
    if base_stats_header:
        # Find the next table after the header
        base_stats_table = base_stats_header.find_next('table')
        if base_stats_table:
            return base_stats_table
    return None

# Python dict which contains pokemon type effectiveness
types_effects = {}

for pokemon in all_pokemons:
    url = f"https://bulbapedia.bulbagarden.net/wiki/{pokemon}_(Pok%C3%A9mon)"
    # Scraping the table after "Base stats"  for each Pokemon
    table_ = scrape_base_stats_table(url)
    # Initializing types_effects dict
    types_effects[pokemon] = {}

    if table_:
        # Extracting tbody element which contains data
        body_table = table_.find("tbody")

        # Extracting tr elements which contains type effectiveness
        effectiveness = body_table.find_all("tr", recursive=False)
        effectiveness = effectiveness[1:-1]

    # Looping trough children tr / Main rows of table
    for effects in effectiveness:        
        # Main row in the table
        main_row = effects.find('th').text.strip()
        # Initialize dictionary for the main row if not already initialized
        types_effects[pokemon][main_row] = {}
        
        # Extracting span's contains power of effect 
        power_effect = effects.find_all("span", {'style': 'display:inline-block;'})
        
        # Inner cells
        for type in power_effect:
            a_tag = type.find('a')
            if a_tag:
                type_name = a_tag.text.strip()
                multiplier = type.find_all('td')[1].text.strip()[:-1] 
                # Extracting effects and their values into dict
                ### numeric() func error veriyor, unicode olmali str deigil diye coz
                types_effects[pokemon][main_row][type_name] = numeric(multiplier)




for key, value in types_effects.items():
    print(key + ":")
    print(value)
