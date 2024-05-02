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
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
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

    def switch_turn(self):
        self.current_turn = (self.current_turn + 1) % 2

    def start_fight(self):
        attacker = self.pokemon1 if self.current_turn == 0 else self.pokemon2
        defender = self.pokemon2 if self.current_turn == 0 else self.pokemon1

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
                print(f"{self.pokemon1.name} health = {self.pokemon1.current_health} HP, {self.pokemon2.name} health = {self.pokemon2.current_health} HP")
                print("="*50)

                if defender.current_health <= 0:
                    print(f"{defender.name} fainted!")
                    break
            elif choice == '2':
                attacker.revive()
                print(f"{self.pokemon1.name} health = {self.pokemon1.current_health} HP, {self.pokemon2.name} health = {self.pokemon2.current_health} HP")
                print("="*50)
            elif choice == '3':
                print("Thanks for playing! Farewell!")
                return
            else:
                print("Invalid choice.")
                print("="*50)

            self.switch_turn()
            attacker = self.pokemon1 if self.current_turn == 0 else self.pokemon2
            defender = self.pokemon2 if self.current_turn == 0 else self.pokemon1


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

# Get user input for Pokémon names
which_pokemon1 = input("Enter the name of the first Pokémon: ").strip()
which_pokemon2 = input("Enter the name of the second Pokémon: ").strip()

# Fetch Pokémon data from MongoDB and create Pokémon instances
player1 = collection.find_one({"_id": which_pokemon1}, {"agility": 1, "effects": 1, "type": 1})
player2 = collection.find_one({"_id": which_pokemon2}, {"agility": 1, "effects": 1, "type": 1})
pok1 = document_to_pokemon(player1)
pok2 = document_to_pokemon(player2)

# Start the fight
fight = Fight(pok1, pok2)
fight.start_fight()

