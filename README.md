# Pokémon Game Project

This project aims to create a comprehensive console-based Pokémon battle system using Python. It includes scripts for data collection, database management utilizing MongoDB, and the implementation of a console-based battle system.

## Installation

To run the Pokémon game project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/pokemon-game.git
```

2. Open the console wherever game files located:

3. Execute installation.sh file, give permissions if it is needed:

```bash
./installation.sh
```

4. After installations is done, execute play.py file to play the game:

```bash
python3 play.py
```

## Usage

### Installation
 - **installation.sh**: Installs all programs, tools and libraries needed to play the game. Execute it, It could take some time to complete all scraping.

### Data Collection

- **pokemonNames.py**: Collects Pokémon data from Bulbapedia's list of Pokémon bay ability.
- **pokemonImg.py**: Downloads Pokémon images from Bulbapedia and stores them in MongoDB database.
- **pokemonSkills.py**: Retrieves Pokémon base stats from Bulbapedia pages.
- **typeEffect.py**: Gathers Pokémon type effectiveness data from Bulbapedia.

### Database Management

**MongoDB Database Structure:**

- **Collections:**
  - **pokedex**: Stores Pokémon data including names, base stats, type effectiveness, and images.
  - **Additional Collections:** Images, base stats, and type effectiveness stored as embedded documents within each Pokémon document.

**MongoDB Database Usage:**

- **Connection:** Establishes connection to the MongoDB instance running locally.
- **Insertion:** Pokémon data is inserted into the database collections using MongoDB's `insert_one()` or `update_one()` methods.
- **Querying:** Data is retrieved from the database using MongoDB queries based on Pokémon names or other identifiers.
- **Closing Connection:** Once the data operations are completed, the database connection is closed.

### Console-Based Battle System

- **pokeTypes.py** and **play.py**: Implements the console-based battle system for Pokémon battles.
- **play.py**  implements the console-based battle system for Pokémon battles. It defines Pokemon and Fight classes for battle simulation. The Pokemon class has attributes such as name, base health, stats, effects, and type. The Fight class manages the battle between two Pokémon, including initiating battles, switching turns, and executing player actions such as attacking or reviving.
- The **play.py** script fetches Pokémon data from MongoDB to create Pokémon instances. It calculates damage based on the attacking and defending Pokémon's stats, type effectiveness, and a random factor. The script also allows players to revive their fainted Pokémon or substitute a new Pokémon during the battle.
- The Fight class provides a user-friendly console interface for players to engage in battles. It displays the current health of each Pokémon, the damage dealt, and the type of attack used. The script also handles the logic for determining the winner of the battle based on the remaining health of each Pokémon.

- To run the console-based battle system, simply execute the play.py script with the required dependencies installed. The script will prompt the user to select the game mode and choose their Pokémon for the battle. Once the battle begins, the user can input their desired actions for each turn until the battle is over.

### Upcoming Features
- There will be GUI to make  gaming experience even better. Pictures of pokemons are allready collected and implemented into mongodb file. These pictures will be used in GUI.

## Contributors

- Mete Turkan
