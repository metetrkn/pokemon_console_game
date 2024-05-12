import random
from pymongo import MongoClient

class Pokemon:
    def __init__(self, name, base_health, stats, effects, type_):
        self.name = name
        self.base_health = round(base_health, 1)
        self.current_health = round(base_health, 1)
        self.stats = {key: round(value, 1) for key, value in stats.items()}
        self.effects = effects
        self.type_ = type_


    def calculate_damage(self, defender):
        random_factor = random.uniform(0, 1.2)
        random_factor = 0 if random_factor <= 0.15 else random_factor
        move_type = self.type_
        damage = round((2 * self.stats['Attack'] / defender.stats['Defense']) * self.move_type_multiplier(move_type, defender.effects) * random_factor, 1)
        return damage, random_factor, move_type

    def move_type_multiplier(self, move_type, defender_effects):
        multiplier = 2
        for key, value in defender_effects.items():
            if move_type in value:
                if key == 'Weak to:':
                    multiplier *= 4
                elif key == 'Resistant to:':
                    multiplier *= 1
        return multiplier

    def revive(self):
        # Revive the Pokémon by restoring its health by 1/20 of its current health
        heal_amount = round(self.current_health / 20, 1)
        self.current_health += heal_amount
        if self.current_health > self.base_health:
            self.current_health = self.base_health
        print(f"{self.name} revived {heal_amount} HP!")
        print(f"{self.name} health = {self.current_health}")

class Fight:
    def start_fight(self, warrior1, worrior2):         
        attacker = warrior1 if self.current_turn == 0 else worrior2
        defender = worrior2 if self.current_turn == 0 else warrior1

        while True:
            print(f"It's {attacker.name}'s turn.")
            choice = input("Enter 1 to attack, 2 to revive, 3 to quit: ")
            if choice == '1':
                damage, random_factor, move_type = attacker.calculate_damage(defender)
                if random_factor == 0:
                    print("Attack Missed!")
                elif random_factor > 1:
                    print("Critical Hit!")
                defender.current_health = round(max(0, defender.current_health - damage), 1)
                print(f"{attacker.name} attacks with {damage} PP, {defender.name} got injured.")
                print(f"{warrior1.name} health = {warrior1.current_health} HP, {worrior2.name} health = {worrior2.current_health} HP")
                print("="*50)

                if defender.current_health <= 0:
                    print(f"{defender.name} fainted!")
                    
                    # Updating teams with reamining pokemonss
                    self.teams_remainings()

            elif choice == '2':
                attacker.revive()
                print(f"{warrior1.name} health = {round(warrior1.current_health, 1)} HP, {worrior2.name} health = {round(worrior2.current_health, 1)} HP")
                print("="*50)
            elif choice == '3':
                print("Thanks for playing! Farewell!")
                return
            else:
                print("Invalid choice.")
                print("="*50)

            self.switch_turn()
            attacker = warrior1 if self.current_turn == 0 else worrior2
            defender = worrior2 if self.current_turn == 0 else warrior1


    def __init__(self, pokTeam1, pokTeam2):
        self.pokTeam1 = pokTeam1
        self.pokTeam2 = pokTeam2
        self.current_turn = 0
        print("="*50)
        print("+"*50)
        print("="*50)
        print("Welcome to the Pokémon Game!")
        print("Programmer: Mete Turkan")
        print("Today's Date: 2024-05-02")
        print("="*50)
        print("+"*50)
        print("="*50)

        # Creating a system to make teams to choose their 1st pokemon for 1st round
        if game_mode == '1':
            self.t1_fist_pok = 0
            self.t2_fist_pok = 0
        elif game_mode == '3':
            self.t1_fist_pok = int(input(f"Team1 chooses 1st round pokemon * Enter the number to choose\t\t:0={self.pokTeam1[0].name}\t\t1={self.pokTeam1[1].name}\t\t2={self.pokTeam1[2].name} ==>"))
            self.t2_fist_pok = int(input(f"Team2 chooses 1st round pokemon * Enter the number to choose\t\t:0={self.pokTeam2[0].name}\t\t1={self.pokTeam2[1].name}\t\t2={self.pokTeam2[2].name} ==>"))
        else:
            self.t1_fist_pok = int(input(f"Team1 chooses 1st round pokemon * Enter the number to choose\t\t:0= \
    {self.pokTeam1[0].name}\t\t1={self.pokTeam1[1].name}\t\t2={self.pokTeam1[2].name}\t\t3={self.pokTeam1[3].name}\t\t4={self.pokTeam1[4].name}\t\t5={self.pokTeam1[5].name} ==>"))
            self.t2_fist_pok = int(input(f"Team2 chooses 1st round pokemon * Enter the number to choose\t:0= \
    {self.pokTeam2[0].name}\t\t1={self.pokTeam2[1].name}\t\t2={self.pokTeam2[2].name}\t\t3={self.pokTeam2[3].name}\t\t4={self.pokTeam2[4].name}\t\t5={self.pokTeam2[5].name} ==>"))
        
        self.start_fight(pokTeam1[self.t1_fist_pok], pokTeam2[self.t2_fist_pok])
     

    def switch_turn(self):
        self.current_turn = (self.current_turn + 1) % 2

    def teams_remainings(self):
        # New teams list which contains that pokemons have more than 0 HP
        remainings_t1 = []
        remainings_t2 = []

        # Adding new teams list with not fainted pokemons
        # Number of remaining pokemon per team
        num1 = len(self.pokTeam1)
        num2 = len(self.pokTeam2)

        # Updating Team1
        for i in range(num1):
            if self.pokTeam1[i].current_health > 0:
                remainings_t1.append(self.pokTeam1[i])
        
        # Updating Team2
        for i in range(num2):
            if self.pokTeam2[i].current_health > 0:
                remainings_t2.append(self.pokTeam2[i])     

        # If one of teams all pokemon is fainted, other player wins!
        if len(remainings_t1) == 0:
            print("Team2 has winned the game! Congrats!!!")
            exit()
        elif len(remainings_t2) == 0:
            print("Team1 has winned the game! Congrats!!!")
            exit()

        # Updating teams with not fainted pokemons
        self.pokTeam1 = remainings_t1 
        self.pokTeam2 = remainings_t2 

        # Fainted pokemon's team chooses new pokemon for next round
        self.choosing_to_fight()

    def choosing_to_fight(self):  
        # Team1 chooses its new pokemon for new round
        which_pokemon = 0
        for pokemon_remaining in self.pokTeam1:
            print(which_pokemon, ": ", pokemon_remaining.name, "\t\t", end="")
            which_pokemon += 1
        warrior1 = int(input("Choose\t:"))
        print(f"{self.pokTeam1[warrior1].name} I choose you!")
        warrior1 = self.pokTeam1[warrior1]

        # Team2 chooses its new pokemon for new round
        which_pokemon = 0
        for pokemon_remaining in self.pokTeam2:
            print(which_pokemon, ": ", pokemon_remaining.name, "\t\t", end="")
            which_pokemon += 1
        warrior2 = int(input("Choose\t:"))
        print(f"{self.pokTeam2[warrior2].name} I choose you!")
        warrior2 = self.pokTeam2[warrior2]

        # New round begins with newly choosen pokemons
        self.start_fight(warrior1, warrior2)



# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017")
db = client["pokemonData"]
collection = db["pokedex"]

# Fetch Pokémon data from MongoDB and convert it into Pokémon instances
def document_to_pokemon(document):
    name = document['_id']
    base_health = int(float(document['agility']['HP']))
    stats = {
        'Attack': int(float(document['agility']['Attack'])),
        'Defense': int(float(document['agility']['Defense']))
    }
    effects = {
        'Weak to:': set(document['effects'].get('Weak to:', {}).keys()),
        'Resistant to:': set(document['effects'].get('Resistant to:', {}).keys())
    }
    type_ = document['type']
    return Pokemon(name, base_health, stats, effects, type_)


def choose_pokemons(num_pokemon, team):
    pokemons = []
    i = 0
    while len(pokemons) < num_pokemon:
        pokemon_name = input(f"Enter the name of {i+1}. Pokémon for {team}: ").strip()
        pokemon_data = collection.find_one({"_id": pokemon_name}, {"agility": 1, "effects": 1, "type": 1})
        if pokemon_data:
            pokemon_instance = document_to_pokemon(pokemon_data)
            pokemons.append(pokemon_instance)
            i += 1
        else:
            print(f"Error: Pokémon {pokemon_name} not found in the database.")
    return pokemons


# Get user input for the game mode
game_mode = input("Enter the desired game mode (1\t for 1 vs 1, 3\t for 3 vs 3, 6\t for 6 vs 6): ").strip()

# Choose Pokémon based on game mode
if game_mode == '1':
    team1 = choose_pokemons(1,"team-1")
    team2 = choose_pokemons(1,"team-2")
elif game_mode == '3':
    team1 = choose_pokemons(3,"team-1")
    team2 = choose_pokemons(3,"team-2")
elif game_mode == '6':
    team1 = choose_pokemons(6,"team-1")
    team2 = choose_pokemons(6,"team-2")
else:
    print("Invalid game mode. Please choose 1, 3, or 6.")

# Start the fight
fight = Fight(team1, team2)
fight.start_fight()


