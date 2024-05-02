# Pokémon Game Project

This project aims to create a comprehensive console-based Pokémon battle system using Python. It includes scripts for data collection, database management utilizing MongoDB, and the implementation of a console-based battle system.

## Installation

To run the Pokémon game project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/pokemon-game.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Data Collection

- **pokemonNames.py**: Collects Pokémon data from Bulbapedia's list of Pokémon by ability.
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
- Defines Pokémon and Fight classes for battle simulation.
- Fetches Pokémon data from MongoDB to create Pokémon instances.
- Initiates battles, switches turns, and executes player actions (attack or revive).
- Provides a user-friendly console interface for players to engage in battles.

## Contributors

- Mete Turkan
