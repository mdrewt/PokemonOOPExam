# encoding: utf-8
import functools
import random
import time

# Instructions
#  - This exam will test your understanding of Object Oriented Developement and Test Driven Developement
#  - Looking up things is highly encouraged
#
#  - In this exam you will create a Pokemon class and an Attack class
#  - Both classes will accept an argument when instantiating an object
#  - This argument will be a hash, and will contain the data neccesary to construct the individual Pokemon or Attacks
#  - Examples of these data-hashes are listed below
#  - A Pokemon will have HP, attacks, a name, a preform_attack method, a receive_damage method, and a learn_attack method
#  - An Attack will have a name and a power and belong to a pokemon
#
#  - Tests have been written for you to make sure your code is behaving as expected
#  - When you're ready to start, run this file and look at the first test message that appears
#  - The test message should tell you what is needed to pass that test
#  - Write the minimum amount of code to make that test pass, do not rush ahead
#  - When the conditions for the passing test are met you will see a "Test Passed!" message and a new test message will appear
#
#  - After all the tests are passing you's see a message telling you that you're done
#  - Be sure to stick around after the credits for a prize (Don't forget to resize your terminal)
#
#  - Bonus:
#  - For extra credit give a pokemon types of attacks that it is strong against (maybe takes half damage from?) and types of attacks it is weak to (maybe takes double damage from?)
#  - Consider giving a bonus to damage if the pokemon's type matches the attack type?
#  - Practice making data-hashes (also called "options-hashes" or just "options")

# Sample creation-data hashes

sample_pokemon_hash = {
  "name": "Charmander",
  "type": "fire",
  "strengths": ["fire"],
  "weaknesses": ["water"],
  "hp": 10
}

sample_attack = {
  "name": "Ember",
  "type": "fire",
  "power": 5
}

# Write Your Code Below This Line

# Code Here...

# Write Your Code Above This Line

# Tests

def run_tests(tests):
  index = 0
  for test in tests:
    if not test.run():
      break
    index += 1

  return index == len(tests)

def get_attributes(object):
  return list(object.__dict__.keys())

def get_methods(object):
  return [method for method in dir(object) if method not in get_attributes(object)]

def mutate(object, mutation):
  mutation(object)
  return object

class Test:
  def __init__(self, options):
    self._setup = options.get("setup") or ( lambda : True )
    self._mutations = options.get("mutations") or []
    self._check = options.get("check") or ( lambda  r : True )
    self.success_message = options.get("success_message") or "Test Passed"
    self.fail_message = options.get("fail_message") or "Test Failed"
    self.passed = False

  def run(self):
    try:
      result = self._check(
        functools.reduce(
          lambda a, b: b(a), self._mutations,
          self._setup()
        )
      )
    except Exception as e:
      result = False
      print("\n" + str(e.__class__) + " - " + str(e))
    finally:
      if result:
        self.success()
      else:
        self.failure()
      return result

  def success(self):
    print(self.success_message)

  def failure(self):
    print(self.fail_message)

tests = [
  {
    "setup": lambda : Pokemon,
    "fail_message": "You need to create a Pokemon class"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "fail_message": "A Pokemon should take an options argument during initialization"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : "name" in get_attributes(pokemon),
    "fail_message": "A Pokemon should have a 'name' attribute"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : pokemon.name == "Pikachu",
    "fail_message": "The 'name' attribute should return the name the Pokemon was created with"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : "hp" in get_attributes(pokemon),
    "fail_message": "A Pokemon should have a 'hp' attribute"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : pokemon.hp == 10,
    "fail_message": "A Pokemon's 'hp' method should return the hp attribute that it was created with"
  },
  {
    "setup": lambda : Attack,
    "fail_message": "You need to create an Attack class"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }),
    "fail_message": "An Attack should take an options argument during initialization"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }),
    "check": lambda attack : "name" in get_attributes(attack),
    "fail_message": "An Attack should have a 'name' attribute"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }),
    "check": lambda attack : attack.name == "Thunderbolt",
    "fail_message": "The 'name' attribute should return the name the Attack was created with"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }),
    "check": lambda attack : "power" in get_attributes(attack),
    "fail_message": "An Attack should have a 'power' attribute"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }),
    "check": lambda attack : attack.power == 15,
    "fail_message": "The 'power' attribute should return the power the Attack was created with"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }),
    "check": lambda attack : "type" in get_attributes(attack),
    "fail_message": "An Attack should have a 'type' attribute"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "type": "electric", "power": 15 }),
    "check": lambda attack : attack.type == "electric",
    "fail_message": "The 'type' attribute should return the type the Attack was created with"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : "attacks" in get_attributes(pokemon),
    "fail_message": "A Pokemon should have an 'attacks' attribute"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : pokemon.attacks == [],
    "fail_message": "The 'attacks' attribute should return a list of the attacks the Pokemon knows"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : "learn_attack" in get_methods(pokemon),
    "fail_message": "A Pokemon should have a 'learn_attack' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }), 
    "mutations": [
      lambda p : mutate(p, lambda p : p.learn_attack(Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" })))
    ],
    "fail_message": "The 'learn_attack' method should take an attack as an argument"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "mutations": [
      lambda p : mutate(p, lambda p : p.learn_attack(Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" })))
    ],
    "check": lambda pokemon : len(pokemon.attacks) == 1,
    "fail_message": "The 'learn_attack' method should add an attack to array of the attacks the Pokemon knows"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : "receive_damage" in get_methods(pokemon),
    "fail_message": "A Pokemon should have a 'receive_damage' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "mutations": [
      lambda pokemon : pokemon.receive_damage(5, "normal")
    ],
    "fail_message": "The 'receive_damage' method should take the amount and type of damage as arguments"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "mutations": [
      lambda pokemon : mutate(pokemon, lambda p : p.receive_damage(5, ""))
    ],
    "check": lambda pokemon : pokemon.hp < 10,
    "fail_message": "A Pokemon's 'receive_damage' method should lower the hp attribute of that pokemon"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "check": lambda pokemon : "perform_attack" in get_methods(pokemon),
    "fail_message": "A Pokemon should have a 'perform_attack' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "mutations": [
      lambda pokemon : mutate(pokemon, lambda p : p.learn_attack(Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }))),
      lambda pokemon : mutate(pokemon, lambda p : p.perform_attack(random.choice(p.attacks), Pokemon({ "name": "Squirtle", "hp": 10 }))),
    ],
    "fail_message": "The 'perform_attack' method should take the attack and the target as arguments"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }),
    "mutations": [
      lambda pokemon : mutate(pokemon, lambda p : p.learn_attack(Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }))),
      lambda pokemon : mutate(pokemon, lambda p : p.perform_attack(random.choice(p.attacks), p))
    ],
    "check": lambda pokemon : pokemon.hp < 10,
    "fail_message": "A Pokemon's 'perform_attack' method should use the attack and apply damage to that pokemon's target in a way related to the attack's power."
  }
]

tests = list(map(lambda test : Test(test), tests))
tests_complete = run_tests(tests)

# There is nothing important beyond this mark...

# Reward for completing all tests

POKEMON_DATA = [
  {
    "name": "Pikachu",
    "type": "electric",
    "strengths": ["electric", "water", "flying", "parental"],
    "weaknesses": ["rock", "ground"],
    "hp": 25
  },
  {
    "name": "Pidgy",
    "type": "flying",
    "strengths": ["bug"],
    "weaknesses": ["electric"],
    "hp": 25
  }
]

ATTACK_DATA = [
  {
    "name": "Shock",
    "type": "electric",
    "power": 5
  },
  {
    "name": "Tackle",
    "type": "normal",
    "power": 5
  },
  {
    "name": "Thunder",
    "type": "electric",
    "power": 10
  },
  {
    "name": "Gust",
    "type": "flying",
    "power": 5
  },
  {
    "name": "Swagger",
    "type": "normal",
    "power": 0
  }
]

class GameController:

  def __init__(self):
    self.START_SCREEN = """
  ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ███████╗    ██████╗  ██████╗ ███╗   ██╗███████╗██╗
  ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗████╗  ██║██╔════╝██║
   ╚████╔╝ ██║   ██║██║   ██║██████╔╝█████╗      ██║  ██║██║   ██║██╔██╗ ██║█████╗  ██║
    ╚██╔╝  ██║   ██║██║   ██║██╔══██╗██╔══╝      ██║  ██║██║   ██║██║╚██╗██║██╔══╝  ╚═╝
     ██║   ╚██████╔╝╚██████╔╝██║  ██║███████╗    ██████╔╝╚██████╔╝██║ ╚████║███████╗██╗
     ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝
"""

    self.CREDITS = """
    Credits:

    Art Director:         Drew Teter
    Test Designer:        Drew Teter
    Lead Developer:       Drew Teter
    Project Manager:      Drew Teter
    PR Director:          Drew Teter
    Office Manager:       Drew Teter
    Chief Officer:        Drew Teter
    Chief Thinker:        Drew Teter
    Brand Warrior:        Drew Teter
    Digital Overlord:     Drew Teter
    Summer Intern:        Drew Teter
    INFORMAL PROCTOR:     Drew Teter
    PLATFORM NERD:        Drew Teter
    Beta Tester:          Drew Teter

    Guy Who Actually
    Took The Test:        Cody Seger

    EMOJI VISIONARY:      Drew Teter
    7th Earl of Bradford: Drew Teter
    Electron Re-Ionizer:  Drew Teter
    Nerf Herder:          Drew Teter





    """

    self.NONTRANVERSIBLE_TILES = ["-", "_", "|", "+", "H", "/", "\\"]
    self.LOCATION_MAP = [
      ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","_","_"," "," ","|"],
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," ","/"," "," ","\\"," ","|"],
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," ","|","H","_","|"," ","|"],
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," ","C","O","N","G","R","A","T","U","L","A","T","I","O","N","S","!"," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
      ["|"," "," ","_","_"," "," "," "," ","_","_"," "," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
      ["|"," ","/"," "," ","\\"," "," ","/"," "," ","\\"," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
      ["|"," ","|","H","_","|"," "," ","|","H","_","|"," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
      ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"]
    ]

    self.TITLE = """
  ______     _
  | ___ \\   | |
  | |_/ /__ | | _____ _ __ ___   ___  _ __
  |  __/ _ \\| |/ / _ \\ '_ ` _ \\ / _ \\| '_ \\
  | | | (_) |   <  __/ | | | | | (_) | | | |
  \\_|  \\___/|_|\\_\\___|_| |_| |_|\\___/|_| |_|
+-------------------------------------------+
"""

    self.EXPLORE_COMMANDS = [
      "  +---------------+",
      "  | Command List: |",
      "  |   > Up        |",
      "  |   > Down      |",
      "  |   > Left      |",
      "  |   > Right     |",
      "  |   > Quit      |",
      "  |               |",
      "  |               |",
      "  |               |",
      "  +---------------+"
    ]

    self.BATTLE_COMMANDS = [
      "    +---------------+",
      "    | Command List: |",
      "    |   > Shock     |",
      "    |   > Tackle    |",
      "    |   > Thunder   |",
      "    |   > -----     |",
      "    |   > Item      |",
      "    |   > Quit      |",
      "    |               |",
      "    |               |",
      "    +---------------+"
    ]

    self.VIEW_HIEGHT = 10
    self.VIEW_WIDTH = 22

    self.player_location = {"x": 12, "y": 6}
    self.game_status = "starting"

    self.pokemon = [Pokemon(POKEMON_DATA[0]), Pokemon(POKEMON_DATA[1])]
    
    for attack in ATTACK_DATA[0:3]:
      self.pokemon[0].learn_attack(Attack(attack))

    for attack in ATTACK_DATA[3:5]:
      self.pokemon[1].learn_attack(Attack(attack))

  def localize_map(self, location, area):
    top = max([int(location["y"] - self.VIEW_HIEGHT/2), 0])
    left = max([int(location["x"] - self.VIEW_WIDTH/2), 0])
    return list(map(
      lambda row : row[left:left + self.VIEW_WIDTH + 1],
      area[top:top + self.VIEW_HIEGHT + 1]
    ))

  def clear_screen(self):
    print(chr(27) + "[2J")

  def display_screen(self):
    self.clear_screen()
    self.display_title()
    
    if self.game_status == "starting":
      self.display_startup()
    elif self.game_status == "exploring":
      screen = self.insert_avatar(self.LOCATION_MAP, self.player_location)
      screen = self.localize_map(self.player_location, screen)
      self.display_map(screen)

      command = self.request_command()
      self.handle_menu_command(command)
    elif self.game_status == "encountering":
      self.clear_screen()
      print("You encountered a wild pokemon!")
      time.sleep(2)

      self.game_status = "battling"
    elif self.game_status == "battling":
      self.display_battle()

      command = self.request_command()
      self.handle_battle_command(command)
    elif self.game_status == "finished":
      self.clear_screen()
      print("Fin.")
      self.game_status = "exit"

  def display_startup(self):
    c = chr(27) + "[32m"
    d = chr(27) + "[39m"
    n = 4

    self.clear_screen()
    for line in self.START_SCREEN.split("\n"):
      print(c+line+d)
      time.sleep(0.4)

    for _ in range(n):
      print("")
      time.sleep(0.4)

    for _ in range(5):
      self.clear_screen()
      print(self.START_SCREEN + ("\n"*(n)))
      time.sleep(0.4)

      self.clear_screen()
      print(c+self.START_SCREEN+d + ("\n"*(n)))
      time.sleep(0.4)

    time.sleep(0.4)

    for line in self.CREDITS.split("\n"):
      print(line)
      time.sleep(0.4)

    self.game_status = "exploring"

  def display_title(self):
    print(self.TITLE)

  def display_map(self, local_map):
    c = chr(27) + "[32m"
    d = chr(27) + "[39m"

    for i in range(len(local_map)):
      row = local_map[i]
      print("|  " + "".join(map(lambda cell : c+cell+d if cell == "w" else cell, row)) + self.EXPLORE_COMMANDS[i])

  def insert_avatar(self, area, player_location):
    c = chr(27) + "[31m"
    d = chr(27) + "[39m"
    feet = c+"^"+d if (area[player_location["y"] + 1][player_location["x"]] != "w") else "w"

    top = area[0:player_location["y"]]
    middle1 = [area[player_location["y"]][0:player_location["x"]] + [c+"Ω"+d] + area[player_location["y"]][player_location["x"]+1:]]
    middle2 = [area[player_location["y"]+1][0:player_location["x"]] + [feet] + area[player_location["y"]+1][player_location["x"]+1:]]
    bottom = area[player_location["y"]+2:]

    return top + middle1 + middle2 + bottom

  def display_battle(self):
    battle_view = self.generate_battle(self.pokemon[0], self.pokemon[1])
    for i in range(len(battle_view)):
      line = battle_view[i]
      print(line + self.BATTLE_COMMANDS[i])

  def generate_battle(self, pokemon, opponent):
    opponent_name = opponent.name[0:21].ljust(21, " ")
    opponent_hp = str(opponent.hp)[0:17].rjust(17, " ")
    name = pokemon.name[0:21].ljust(21, " ")
    hp = str(pokemon.hp)[0:17].rjust(17, " ")
    return [
      "+----------------------+",
      f"| {opponent_name}|",
      "|       --------       |",
      f"| HP:{opponent_hp} |",
      "+----------------------+",
      "                        ",
      "+----------------------+",
      f"| {name}|",
      "|       --------       |",
      f"| HP:{hp} |",
      "+----------------------+"
    ]

  def request_command(self):
    print(self.game_status.upper())
    print("Enter your command: ")
    return input().lower()

  def move_avatar(self, direction):
    self.player_location["x"] += direction["x"]
    self.player_location["y"] += direction["y"]

    if self.LOCATION_MAP[self.player_location["y"] + 1][self.player_location["x"]] == "w" and random.choice(range(0,10)) == 0:
      self.game_status = "encountering"

  def handle_menu_command(self, command):
    if command == "exit":
      self.game_status = "exit"
    elif command == "quit":
      self.game_status = "exit"
    elif command == "up":
      target_tile = self.LOCATION_MAP[self.player_location["y"] - 1][self.player_location["x"]]
      if target_tile not in self.NONTRANVERSIBLE_TILES:
        self.move_avatar({"y": -1, "x": 0})
    elif command == "down":
      target_tile = self.LOCATION_MAP[self.player_location["y"] + 2][self.player_location["x"]]
      if target_tile not in self.NONTRANVERSIBLE_TILES:
        self.move_avatar({"y": 1, "x": 0})
    elif command == "left":
      for _ in range(2):
        target_tile1 = self.LOCATION_MAP[self.player_location["y"]][self.player_location["x"] - 1]
        target_tile2 = self.LOCATION_MAP[self.player_location["y"] + 1][self.player_location["x"] - 1]
        if (target_tile1 not in self.NONTRANVERSIBLE_TILES) and (target_tile2 not in self.NONTRANVERSIBLE_TILES):
          self.move_avatar({"y": 0, "x": -1})
    elif command == "right":
      for _ in range(2):
        target_tile1 = self.LOCATION_MAP[self.player_location["y"]][self.player_location["x"] + 1]
        target_tile2 = self.LOCATION_MAP[self.player_location["y"] + 1][self.player_location["x"] + 1]
        if (target_tile1 not in self.NONTRANVERSIBLE_TILES) and (target_tile2 not in self.NONTRANVERSIBLE_TILES):
          self.move_avatar({"y": 0, "x": 1})


  def handle_battle_command(self, command):
    pokemon = self.pokemon[0]
    opponent = self.pokemon[1]

    chosen_attack = None
    for attack in pokemon.attacks:
     if command == attack.name.lower():
       chosen_attack = attack
       break
     
    if chosen_attack != None:
      initial_hp = opponent.hp
      pokemon.perform_attack(chosen_attack, opponent)
      print(f"You used {chosen_attack.name} on {opponent.name}!")
      time.sleep(1.5)
      print(f"{opponent.name} takes {initial_hp - opponent.hp} damage.")
      time.sleep(1.5)

    elif command == "exit":
      self.game_status = "exit"

    elif command == "quit":
      self.game_status = "exit"

    elif command == "item":
      healing = pokemon.hp - 25
      pokemon.receive_damage(healing, "healing")
      print(f"You healed your pokemon for {healing.abs} points!")
      time.sleep(1.5)

    if opponent.hp > 0 and self.game_status != "exit":
      self.clear_screen()
      self.display_title()
      self.display_battle()

      initial_hp = pokemon.hp
      attack = random.choice(opponent.attacks)
      opponent.perform_attack(attack, pokemon)
      print(f"{opponent.name} uses {attack.name}!")
      time.sleep(1.5)
      print(f"You take {initial_hp - pokemon.hp} damage.")
      time.sleep(1.5)

      if pokemon.hp < 0:
        print("You whited out!")
        time.sleep(1.5)
        self.clear_screen()
        print("You lose!")
        time.sleep(1.5)

        self.game_status = "finished"
    else:
      print(opponent.name + " fainted!")
      time.sleep(1.5)
      self.clear_screen()
      print("You win!")
      time.sleep(1.5)

      self.game_status = "finished"

  def start(self):
    while self.game_status != "exit":
      self.display_screen()

if (tests_complete):
  print("Tests Complete.")
  game = GameController()
  game.start()
