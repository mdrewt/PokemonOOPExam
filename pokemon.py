# encoding: utf-8

# Instructions
#  - This exam will test your understanding of Object Oriented Developement and Test Driven Developement
#  - Looking up things is highly encouraged
#
#  - In this exam you will create a Pokemon class and an Attack class
#  - Both classes will accept a single argument when instantiating an object
#  - This argument will be a hash, and will contain the data neccesary to construct the individual Pokemon or Attacks
#  - Examples of these data-hashes are listed below
#  - A Pokemon will have HP, attacks, a name, a preform_attack method, a receive_attack method, and a learn_attack method
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
  tests_complete = False

  index = 0
  for test in tests:
    index += 1
    try:
      test.run()
      if test.passed:
        test.success()
      else:
        test.failure()
        break
    except Exception as e:
      test.failure()
      print("  - error: ")
      print(e)
      break

    if index == len(tests):
      tests_complete = True

  tests_complete


class Test:
  def __init__(self, options):
    self._setup = options["setup"] or ( lambda : None )
    self._check = options["check"] or None
    self.success_message = options["success_message"] or "Test Passed"
    self.fail_message = options["fail_message"] or "Test Failed"
    self.passed = False

  def run(self):
    result = self._setup()
    if self._check:
      self.passed = self._check(result)
    else:
      self.passed = true

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
    "fail_message": "A Pokemon should take a single argument during initialization"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }).name,
    "fail_message": "A Pokemon should have a 'name' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }).name,
    "check": lambda name : name == "Pikachu",
    "fail_message": "The 'name' method should return the name the Pokemon was created with"
  },
  {
    "setup": lambda : Attack,
    "fail_message": "You need to create an Attack class"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }),
    "fail_message": "An Attack should take a single argument during creation"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }).name,
    "fail_message": "An Attack should have a 'name' method"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }).name,
    "check": lambda name : name == "Thunderbolt",
    "fail_message": "The 'name' method should return the name the Attack was created with"
  },
  {
    "setup": lambda : list(Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }).__dict__.keys()),
    "check": lambda methods : "power" in methods,
    "fail_message": "An Attack should have a 'power' method"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }).power,
    "check": lambda power : power == 15,
    "fail_message": "The 'power' method should return the power the Attack was created with"
  },
  {
    "setup": lambda : list(Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }).__dict__.keys()),
    "check": lambda methods : "type" in methods,
    "fail_message": "An Attack should have a 'type' method"
  },
  {
    "setup": lambda : Attack({ "name": "Thunderbolt", "type": "electric", "power": 15 }).type,
    "check": lambda type : type == "electric",
    "fail_message": "The 'type' method should return the type the Attack was created with"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }).attacks,
    "fail_message": "A Pokemon should have an 'attacks' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }).attacks,
    "check": lambda attacks : attacks == [],
    "fail_message": "The 'attacks' method should return an array of the attacks the Pokemon knows"
  },
  {
    "setup": lambda : list(Pokemon({ "name": "Pikachu", "hp": 10 }).__dict__.keys()),
    "check": lambda methods : "learn_attack" in methods,
    "fail_message": "A Pokemon should have a 'learn_attack' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }).learn_attack(Attack({"name": "Thunderbolt", "power": 15, "type": "electric" })),
    "fail_message": "The 'learn_attack' method should take a single argument"
  },
  # {
  #   "setup": lambda :
  #     pokemon = Pokemon({ "name": "Pikachu", "hp": 10 })
  #     pokemon.learn_attack(Attack({"name": "Thunderbolt", "power": 15, "type": "electric" }))
  #     pokemon.attacks
  #   ,
  #   "check": lambda attacks : attacks.length == 1,
  #   "fail_message": "The 'learn_attack' method should add an attack to array of the attacks the Pokemon knows"
  # },
  {
    "setup": lambda : list(Pokemon({ "name": "Pikachu", "hp": 10 }).__dict__.keys()),
    "check": lambda methods : "perform_attack" in methods,
    "fail_message": "A Pokemon should have a 'perform_attack' method"
  },
  # {
  #   "setup": lambda :
  #     pokemon = Pokemon({ "name": "Pikachu", "hp": 10 })
  #     pokemon.learn_attack(Attack({"name": "Thunderbolt", "power": 15, "type": "electric" }))
  #     pokemon.perform_attack(pokemon.attacks.sample, Pokemon({ "name": "Squirtle", "hp": 10 }))
  #   ,
  #   "fail_message": "The 'perform_attack' method should take two arguments (the attack and the target)"
  # },
  {
    "setup": lambda : list(Pokemon({ "name": "Pikachu", "hp": 10 }).__dict__.keys()),
    "check": lambda methods : "receive_attack" in methods,
    "fail_message": "A Pokemon should have a 'receive_attack' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }).receive_attack(5, "normal")
    ,
    "fail_message": "The 'receive_attack' method should take two arguments (damage and type)"
  },
  {
    "setup": lambda : list(Pokemon({ "name": "Pikachu", "hp": 10 }).__dict__.keys()),
    "check": lambda methods : "hp" in methods,
    "fail_message": "A Pokemon should have a 'hp' method"
  },
  {
    "setup": lambda : Pokemon({ "name": "Pikachu", "hp": 10 }).hp,
    "check": lambda hp : hp == 10,
    "fail_message": "A Pokemon's 'hp' method should return the hp attribute that it was created with"
  },
  # {
  #   "setup": lambda :
  #     pokemon = Pokemon({ "name": "Pikachu", "hp": 10 })
  #     pokemon.receive_attack(5, "")
  #     pokemon.hp
  #   ,
  #   "check": lambda hp : hp < 10,
  #   "fail_message": "A Pokemon's 'receive_attack' method should lower the hp attribute of that pokemon"
  # },
  # {
  #   "setup": lambda :
  #     pokemon = Pokemon({ "name": "Pikachu", "hp": 10 })
  #     pokemon.learn_attack(Attack({ "name": "Thunderbolt", "power": 15, "type": "electric" }))

  #     pokemon.perform_attack(pokemon.attacks.sample, pokemon)
  #     pokemon.hp
  #   ,
  #   "check": lambda hp : hp < 10,
  #   "fail_message": "A Pokemon's 'perform_attack' method should use the attack and apply damage to that pokemon's target in a way related to the attack's power."
  # }
]

tests = map(lambda test : Test(test), tests)
tests_complete = run_tests(tests)

# There is nothing important beyond this mark

# Reward for completing all tests

# POKEMON_DATA = [
#   {
#     "name": "Pikachu",
#     "type": "electric",
#     "strengths": ["electric", "water", "flying", "parental"],
#     "weaknesses": ["rock", "ground"],
#     "hp": 25
#   },
#   {
#     "name": "Pidgy",
#     "type": "flying",
#     "strengths": ["bug"],
#     "weaknesses": ["electric"],
#     "hp": 25
#   }
# ]

# ATTACK_DATA = [
#   {
#     "name": "Shock",
#     "type": "electric",
#     "power": 5
#   },
#   {
#     "name": "Tackle",
#     "type": "normal",
#     "power": 5
#   },
#   {
#     "name": "Thunder",
#     "type": "electric",
#     "power": 10
#   },
#   {
#     "name": "Gust",
#     "type": "flying",
#     "power": 5
#   },
#   {
#     "name": "Swagger",
#     "type": "normal",
#     "power": 0
#   }
# ]

# class GameController:

#   def __init__(self):
#     self.START_SCREEN = "██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ███████╗    ██████╗  ██████╗ ███╗   ██╗███████╗██╗
# ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗████╗  ██║██╔════╝██║
#  ╚████╔╝ ██║   ██║██║   ██║██████╔╝█████╗      ██║  ██║██║   ██║██╔██╗ ██║█████╗  ██║
#   ╚██╔╝  ██║   ██║██║   ██║██╔══██╗██╔══╝      ██║  ██║██║   ██║██║╚██╗██║██╔══╝  ╚═╝
#    ██║   ╚██████╔╝╚██████╔╝██║  ██║███████╗    ██████╔╝╚██████╔╝██║ ╚████║███████╗██╗
#    ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝"

#     self.CREDITS = '''
#     Credits:

#     Art Director:         Drew Teter
#     Test Designer:        Drew Teter
#     Lead Developer:       Drew Teter
#     Project Manager:      Drew Teter
#     PR Director:          Drew Teter
#     Office Manager:       Drew Teter
#     Chief Officer:        Drew Teter
#     Chief Thinker:        Drew Teter
#     Brand Warrior:        Drew Teter
#     Digital Overlord:     Drew Teter
#     Summer Intern:        Drew Teter
#     INFORMAL PROCTOR:     Drew Teter
#     PLATFORM NERD:        Drew Teter
#     Beta Tester:          Drew Teter

#     Guy Who Actually
#     Took The Test:        Chris Guard

#     EMOJI VISIONARY:      Drew Teter
#     7th Earl of Bradford: Drew Teter
#     Electron Re-Ionizer:  Drew Teter
#     Nerf Herder:          Drew Teter





#     '''.upcase

#     self.NONTRANVERSIBLE_TILES = ["-", "_", "|", "+", "H", "/", "\\"]
#     self.LOCATION_MAP = [
#       ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","_","_"," "," ","|"].reverse,
#       ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," ","\\"," "," ","/"," ","|"].reverse,
#       ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," ","|","H","_","|"," ","|"].reverse,
#       ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," "," "," "," "," "," ","|"].reverse,
#       ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," "," "," "," "," "," ","|"].reverse,
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"].reverse,
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," ","C","O","N","G","R","A","T","U","L","A","T","I","O","N","S","!"," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
#       ["|"," "," ","_","_"," "," "," "," ","_","_"," "," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
#       ["|"," ","/"," "," ","\\"," "," ","/"," "," ","\\"," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
#       ["|"," ","|","H","_","|"," "," ","|","H","_","|"," "," "," "," "," ","w","w","w","w","w","w","w"," ","|"],
#       ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
#       ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"]
#     ]

#     self.TITLE = ''' ______     _
#  | ___ \\   | |
#  | |_/ /__ | | _____ _ __ ___   ___  _ __
#  |  __/ _ \\| |/ / _ \\ '_ ` _ \\ / _ \\| '_ \\
#  | | | (_) |   <  __/ | | | | | (_) | | | |
#  \\_|  \\___/|_|\\_\\___|_| |_| |_|\\___/|_| |_|
# +-------------------------------------------+ '''

#     self.EXPLORE_COMMANDS = [
#       "  +---------------+",
#       "  | Command List: |",
#       "  |   > Up        |",
#       "  |   > Down      |",
#       "  |   > Left      |",
#       "  |   > Right     |",
#       "  |   > Quit      |",
#       "  |               |",
#       "  |               |",
#       "  |               |",
#       "  +---------------+"
#     ]

#     self.BATTLE_COMMANDS = [
#       "    +---------------+",
#       "    | Command List: |",
#       "    |   > Shock     |",
#       "    |   > Tackle    |",
#       "    |   > Thunder   |",
#       "    |   > -----     |",
#       "    |   > Item      |",
#       "    |   > Quit      |",
#       "    |               |",
#       "    |               |",
#       "    +---------------+"
#     ]

#     self.VIEW_HIEGHT = 10
#     self.VIEW_WIDTH = 22

#     self.player_location = {x: 4, y: 4}
#     self.game_status = "starting"

#     self.pokemon = [Pokemon(POKEMON_DATA[0]), Pokemon(POKEMON_DATA[1])]
#     ATTACK_DATA[0..2].each {|attack|
#       self.pokemon[0].learn_attack(Attack(attack))
#     }
#     ATTACK_DATA[3..4].each {|attack|
#       self.pokemon[1].learn_attack(Attack(attack))
#     }

#   def localize_map(location, map):
#     top = [location[:y] - self.VIEW_HIEGHT/2, 0].max
#     left = [location[:x] - self.VIEW_WIDTH/2, 0].max
#     map[top..top + self.VIEW_HIEGHT].map {|row| row[left..left + self.VIEW_WIDTH]}

#   def clear_screen:
#     print("\e[2J")

#   def display_screen:
#     clear_screen
#     display_title

#     case self.game_status
#     when "starting"
#       display_startup
#     when "exploring"
#       map = Marshal.load(Marshal.dump(self.LOCATION_MAP))
#       map = insert_avatar(map, self.player_location)
#       map = localize_map(self.player_location, map)
#       display_map(map)

#       command = request_command
#       handle_menu_command(command)
#     when "encountering"
#       clear_screen
#       puts "You encountered a wild pokemon!"
#       sleep(2)

#       self.game_status = "battling"
#     when "battling"
#       display_battle

#       command = request_command
#       handle_battle_command(command)
#     when "finished"
#       clear_screen
#       puts "Fin."
#       self.game_status = "exit"

#   def display_startup:
#     c = "\e[32m"
#     d = "\e[39m"
#     n = 4

#     clear_screen
#     self.START_SCREEN.split("\n").each {|line|
#       puts c+line+d
#       sleep(0.25)
#     }

#     n.times {
#       print("\n")
#       sleep(0.25)
#     }

#     5.times {
#       clear_screen
#       puts self.START_SCREEN
#       print("\n"*(n + 1))
#       sleep(0.2)

#       clear_screen
#       puts c+self.START_SCREEN+d
#       print("\n"*(n + 1))
#       sleep(0.2)
#     }

#     sleep(0.2)

#     self.CREDITS.split("\n").each {|line|
#       puts line
#       sleep(0.4)
#     }

#     self.game_status = "exploring"

#   def display_title:
#     puts self.TITLE

#   def display_map(local_map):
#     c = "\e[32m"
#     d = "\e[39m"
#     local_map.each_with_index {|row, i|
#       print("|  ")
#       row.each {|cell|
#         print cell == "w" ? c+cell+d : cell
#       }
#       print self.EXPLORE_COMMANDS[i]
#       print("\n")
#     }
#     print("\n")

#   def insert_avatar(map, player_location):
#     c = "\e[31m"
#     d = "\e[39m"
#     map[player_location[:y]][player_location[:x]] = c+"Ω"+d
#     map[player_location[:y] + 1][player_location[:x]] = c+"^"+d unless map[player_location[:y] + 1][player_location[:x]] == "w"
#     map

#   def display_battle:
#     battle_view = generate_battle(self.pokemon[0], self.pokemon[1])
#     battle_view.each_with_index { |line, i|
#       puts line + self.BATTLE_COMMANDS[i]
#     }

#   def generate_battle(pokemon, opponent)
#     opponent_name = opponent.name[0...21].ljust(21, " ")
#     opponent_hp = opponent.hp.to_s[0...17].rjust(17, " ")
#     name = pokemon.name[0...21].ljust(21, " ")
#     hp = pokemon.hp.to_s[0...17].rjust(17, " ")
#     [
#       "+----------------------+",
#       "| #{opponent_name}|",
#       "|       --------       |",
#       "| HP:#{opponent_hp} |",
#       "+----------------------+",
#       "                        ",
#       "+----------------------+",
#       "| #{name}|",
#       "|       --------       |",
#       "| HP:#{hp} |",
#       "+----------------------+"
#     ]
#   end

#   def request_command
#     puts self.game_status.upcase
#     print("Enter your command: ")
#     gets.chomp.downcase
#   end

#   def move_avatar(direction):
#     self.player_location[:x] += direction[:x]
#     self.player_location[:y] += direction[:y]

#     if self.LOCATION_MAP[self.player_location[:y] +1][self.player_location[:x]] == "w" and rand(1..10) == 1:
#       self.game_status = "encountering"

#   def handle_menu_command(command):
#     case command
#     when "exit"
#       self.game_status = "exit"
#     when "quit"
#       self.game_status = "exit"
#     when "up"
#       target_tile = self.LOCATION_MAP[self.player_location[:y] -1][self.player_location[:x]]
#       move_avatar({y: -1, x: 0}) unless self.NONTRANVERSIBLE_TILES.include(target_tile)
#     when "down"
#       target_tile = self.LOCATION_MAP[self.player_location[:y] +2][self.player_location[:x]]
#       move_avatar({y: 1, x: 0}) unless self.NONTRANVERSIBLE_TILES.include(target_tile)
#     when "left"
#       2.times {
#         target_tile1 = self.LOCATION_MAP[self.player_location[:y]][self.player_location[:x] -1]
#         target_tile2 = self.LOCATION_MAP[self.player_location[:y] +1][self.player_location[:x] -1]
#         move_avatar({y: 0, x: -1}) unless self.NONTRANVERSIBLE_TILES.include(target_tile1) || self.NONTRANVERSIBLE_TILES.include(target_tile2)
#       }
#     when "right"
#       2.times {
#         target_tile1 = self.LOCATION_MAP[self.player_location[:y]][self.player_location[:x] +1]
#         target_tile2 = self.LOCATION_MAP[self.player_location[:y] +1][self.player_location[:x] +1]
#         move_avatar({y: 0, x: 1}) unless self.NONTRANVERSIBLE_TILES.include(target_tile1) || self.NONTRANVERSIBLE_TILES.include(target_tile2)
#       }
#     end
#   end

#   def handle_battle_command(command)
#     pokemon = self.pokemon[0]
#     opponent = self.pokemon[1]

#     attack = pokemon.attacks.select {|atk| atk.name.downcase == command}.first

#     case command
#     when "exit"
#       self.game_status = "exit"
#     when "quit"
#       self.game_status = "exit"
#     when "shock"
#       initial_hp = opponent.hp
#       pokemon.perform_attack(attack, opponent)

#       puts "You shocked #{opponent.name}!!!"
#       sleep(1.5)
#       puts "#{opponent.name} takes #{initial_hp - opponent.hp} damage."
#       sleep(1.5)
#     when "tackle"
#       initial_hp = opponent.hp
#       pokemon.perform_attack(attack, opponent)

#       puts "You tackle #{opponent.name}!!!"
#       sleep(1.5)
#       puts "#{opponent.name} takes #{initial_hp - opponent.hp} damage."
#       sleep(1.5)
#     when "thunder"
#       initial_hp = opponent.hp
#       pokemon.perform_attack(attack, opponent)

#       puts "You use Thunder!!!"
#       sleep(1.5)
#       puts "#{opponent.name} takes #{initial_hp - opponent.hp} damage."
#       sleep(1.5)
#     when "item"
#       healing = pokemon.hp - 25
#       pokemon.receive_attack(healing, "healing")

#       puts "You healed your pokemon for #{healing.abs} points!"
#       sleep(2)
#     end

#     if opponent.hp > 0 and self.game_status != "exit"
#       clear_screen
#       display_title
#       display_battle

#       initial_hp = pokemon.hp
#       attack = opponent.attacks.sample
#       opponent.perform_attack(attack, pokemon)
#       puts "#{opponent.name} uses #{attack.name}!!!"
#       sleep(1.5)
#       puts "You take #{initial_hp - pokemon.hp} damage."
#       sleep(1.5)

#       if pokemon.hp < 0
#         puts "You whited out!"
#         sleep(2)
#         clear_screen
#         puts "You lose!"
#         sleep(2)

#         self.game_status = "finished"
#       end
#     else
#       puts opponent.name + " fainted!"
#       sleep(2)
#       clear_screen
#       puts "You win!"
#       sleep(2)

#       self.game_status = "finished"
#     end
#   end

#   def start
#     until self.game_status == "exit"
#       display_screen
#     end
#   end

# end

# if (tests_complete)
#   game = GameController.new
#   game.start
# end
