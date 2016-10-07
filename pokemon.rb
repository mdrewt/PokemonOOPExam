# encoding: utf-8

# Instructions
=begin
 - This exam will test your understanding of Object Oriented Developement and Test Driven Developement
 - Looking up things is highly encouraged
 -
 - In this exam you will create a Pokemon class and an Attack class
 - Both classes will accept a single argument when instantiating an object
 - This argument will be a hash, and will contain the data neccesary to construct the individual Pokemon or Attacks
 - Examples of these data-hashes are listed below
 - A Pokemon will have HP, attacks, a name, a preform_attack method, a receive_attack method, and a learn_attack method
 - An Attack will have a name and a power and belong to a pokemon
 -
 - Tests have been written for you to make sure your code is behaving as expected
 - When you're ready to start, run this file and look at the first test message that appears
 - The test message should tell you what is needed to pass that test
 - Write the minimum amount of code to make that test pass, do not rush ahead
 - When the conditions for the passing test are met you will see a "Test Passed!" message and a new test message will appear
 -
 - After all the tests are passing you's see a message telling you that you're done
 - Be sure to stick around after the credits for a prize (Don't forget to resize your terminal)
 -
 - Bonus:
 - For extra credit give a pokemon types of attacks that it is strong against (maybe takes half damage from?) and types of attacks it is weak to (maybe takes double damage from?)
 - Consider giving a bonus to damage if the pokemon's type matches the attack type?
 - Practice making data-hashes (also called "options-hashes" or just "options")
=end

# Sample creation-data hashes

sample_pokemon_hash = {
  name: "Charmander",
  type: "fire",
  strengths: ["fire"],
  weaknesses: ["water"],
  hp: 10
}

sample_attack = {
  name: "Ember",
  type: "fire",
  power: 5
}

# Write Your Code Below This Line

  # Code Here...

# Write Your Code Above This Line

# Tests

def run_tests(tests)
  tests_complete = false

  tests.each_with_index { |test, i|
    begin
      test.run
      if test.passed?
        test.success
      else
        test.failure
        break
      end
    rescue Exception => e
      test.failure
      puts "  - error: " + e.to_s
      break
    end

    if i == tests.length - 1
      tests_complete = true
    end
  }

  tests_complete
end

class Test
  def initialize(options)
    @setup_proc = options.fetch(:setup, Proc.new {})
    @check_proc = options.fetch(:check, nil)
    @success_message = options.fetch(:success_message, "Test Passed")
    @fail_message = options.fetch(:fail_message, "Test Failed")
    @passed = false
  end

  def run
    result = @setup_proc.call
    if @check_proc
      if @check_proc.call(result)
        @passed = true
      end
    else
      @passed = true
    end
  end

  def passed?
    @passed
  end

  def success
    puts @success_message
  end

  def failure
    puts @fail_message
  end
end

tests = [
  {
    setup: Proc.new { Pokemon },
    fail_message: "You need to create a Pokemon class"
  },
  {
    setup: Proc.new { Pokemon.new({ name: "Pikachu", hp: 10}) },
    fail_message: "A Pokemon should take a single argument during initialization"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10})
      pokemon.name
    },
    fail_message: "A Pokemon should have a 'name' method"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10})
      pokemon.name
    },
    check: Proc.new { |name| name == "Pikachu"},
    fail_message: "The 'name' method should return the name the Pokemon was created with"
  },
  {
    setup: Proc.new { Attack },
    fail_message: "You need to create an Attack class"
  },
  {
    setup: Proc.new { Attack.new({ name: "Thunderbolt", power: 15, type: "electric"}) },
    fail_message: "An Attack should take a single argument during creation"
  },
  {
    setup: Proc.new {
      attack = Attack.new({ name: "Thunderbolt", power: 15, type: "electric"})
      attack.name
    },
    fail_message: "An Attack should have a 'name' method"
  },
  {
    setup: Proc.new {
      attack = Attack.new({ name: "Thunderbolt", power: 15, type: "electric"})
      attack.name
    },
    check: Proc.new { |name| name == "Thunderbolt"},
    fail_message: "The 'name' method should return the name the Attack was created with"
  },
  {
    setup: Proc.new {
      attack = Attack.new({ name: "Thunderbolt", power: 15, type: "electric"})
      attack.methods
    },
    check: Proc.new { |methods| methods.include?(:power)},
    fail_message: "An Attack should have a 'power' method"
  },
  {
    setup: Proc.new {
      attack = Attack.new({ name: "Thunderbolt", power: 15, type: "electric"})
      attack.power
    },
    check: Proc.new { |power| power == 15},
    fail_message: "The 'power' method should return the power the Attack was created with"
  },
  {
    setup: Proc.new {
      attack = Attack.new({ name: "Thunderbolt", power: 15, type: "electric"})
      attack.methods
    },
    check: Proc.new { |methods| methods.include?(:type)},
    fail_message: "An Attack should have a 'type' method"
  },
  {
    setup: Proc.new {
      attack = Attack.new({ name: "Thunderbolt", type: "electric", power: 15})
      attack.type
    },
    check: Proc.new { |type| type == "electric"},
    fail_message: "The 'type' method should return the type the Attack was created with"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.attacks
    },
    fail_message: "A Pokemon should have an 'attacks' method"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.attacks
    },
    check: Proc.new { |attacks| attacks == [] },
    fail_message: "The 'attacks' method should return an array of the attacks the Pokemon knows"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.methods
    },
    check: Proc.new { |methods| methods.include?(:learn_attack) },
    fail_message: "A Pokemon should have a 'learn_attack' method"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.learn_attack(Attack.new({name: "Thunderbolt", power: 15, type: "electric" }))
    },
    fail_message: "The 'learn_attack' method should take a single argument"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.learn_attack(Attack.new({name: "Thunderbolt", power: 15, type: "electric" }))
      pokemon.attacks
    },
    check: Proc.new { |attacks| attacks.length == 1 },
    fail_message: "The 'learn_attack' method should add an attack to array of the attacks the Pokemon knows"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.methods
    },
    check: Proc.new { |methods| methods.include?(:perform_attack) },
    fail_message: "A Pokemon should have a 'perform_attack' method"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.learn_attack(Attack.new({name: "Thunderbolt", power: 15, type: "electric"}))
      pokemon.perform_attack(pokemon.attacks.sample, Pokemon.new({ name: "Squirtle", hp: 10 }))
    },
    fail_message: "The 'perform_attack' method should take two arguments (the attack and the target)"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.methods
    },
    check: Proc.new { |methods| methods.include?(:receive_attack) },
    fail_message: "A Pokemon should have a 'receive_attack' method"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.receive_attack(5, "normal")
    },
    fail_message: "The 'receive_attack' method should take two arguments (damage and type)"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.methods
    },
    check: Proc.new { |methods| methods.include?(:hp) },
    fail_message: "A Pokemon should have a 'hp' method"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.hp
    },
    check: Proc.new { |hp| hp == 10 },
    fail_message: "A Pokemon's 'hp' method should return the hp attribute that it was created with"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.receive_attack(5, "")
      pokemon.hp
    },
    check: Proc.new { |hp| hp < 10 },
    fail_message: "A Pokemon's 'receive_attack' method should lower the hp attribute of that pokemon"
  },
  {
    setup: Proc.new {
      pokemon = Pokemon.new({ name: "Pikachu", hp: 10 })
      pokemon.learn_attack(Attack.new({ name: "Thunderbolt", power: 15, type: "electric"}))

      pokemon.perform_attack(pokemon.attacks.sample, pokemon)
      pokemon.hp
    },
    check: Proc.new { |hp| hp < 10 },
    fail_message: "A Pokemon's 'perform_attack' method should use the attack and apply damage to that pokemon's target in a way related to the attack's power."
  }
  # take damage test
]

tests.map! {|test| Test.new(test)}

tests_complete = run_tests(tests)

# There is nothing important beyond this mark

# Reward for completing all tests
# require "Marshal"

POKEMON_DATA = [
  {
    name: "Pikachu",
    type: "electric",
    strengths: ["electric", "water", "flying", "parental"],
    weaknesses: ["rock", "ground"],
    hp: 25
  },
  {
    name: "Pidgy",
    type: "flying",
    strengths: ["bug"],
    weaknesses: ["electric"],
    hp: 25
  }
]

ATTACK_DATA = [
  {
    name: "Shock",
    type: "electric",
    power: 5
  },
  {
    name: "Tackle",
    type: "normal",
    power: 5
  },
  {
    name: "Thunder",
    type: "electric",
    power: 10
  },
  {
    name: "Gust",
    type: "flying",
    power: 5
  },
  {
    name: "Swagger",
    type: "normal",
    power: 0
  }
]

class GameController

  def initialize
    @START_SCREEN = "██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ███████╗    ██████╗  ██████╗ ███╗   ██╗███████╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗████╗  ██║██╔════╝██║
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝█████╗      ██║  ██║██║   ██║██╔██╗ ██║█████╗  ██║
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗██╔══╝      ██║  ██║██║   ██║██║╚██╗██║██╔══╝  ╚═╝
   ██║   ╚██████╔╝╚██████╔╝██║  ██║███████╗    ██████╔╝╚██████╔╝██║ ╚████║███████╗██╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝"

   @CREDITS = "
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
    Took The Test:        Chris Guard

    EMOJI VISIONARY:      Drew Teter
    7th Earl of Bradford: Drew Teter
    Electron Re-Ionizer:  Drew Teter
    Nerf Herder:          Drew Teter





".upcase

    @NONTRANVERSIBLE_TILES = ["-", "_", "|", "+", "H", "/", "\\"]
    @LOCATION_MAP = [
      ["+","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","+"],
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","_","_"," "," ","|"].reverse,
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," ","\\"," "," ","/"," ","|"].reverse,
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," ","|","H","_","|"," ","|"].reverse,
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," "," "," "," "," "," ","|"].reverse,
      ["|"," ","w","w","w","w","w","w","w","w","w","w","w","w"," "," "," "," "," "," "," "," "," "," "," ","|"].reverse,
      ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"].reverse,
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

    @TITLE = " ______     _
 | ___ \\   | |
 | |_/ /__ | | _____ _ __ ___   ___  _ __
 |  __/ _ \\| |/ / _ \\ '_ ` _ \\ / _ \\| '_ \\
 | | | (_) |   <  __/ | | | | | (_) | | | |
 \\_|  \\___/|_|\\_\\___|_| |_| |_|\\___/|_| |_|
+-------------------------------------------+"

    @EXPLORE_COMMANDS = [
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

    @BATTLE_COMMANDS = [
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

    @VIEW_HIEGHT = 10
    @VIEW_WIDTH = 22

    @player_location = {x: 4, y: 4}
    @game_status = "starting"

    @pokemon = [Pokemon.new(POKEMON_DATA[0]), Pokemon.new(POKEMON_DATA[1])]
    ATTACK_DATA[0..2].each {|attack|
      @pokemon[0].learn_attack(Attack.new(attack))
    }
    ATTACK_DATA[3..4].each {|attack|
      @pokemon[1].learn_attack(Attack.new(attack))
    }
  end

  def localize_map(location, map)
    top = [location[:y] - @VIEW_HIEGHT/2, 0].max
    left = [location[:x] - @VIEW_WIDTH/2, 0].max
    map[top..top + @VIEW_HIEGHT].map {|row| row[left..left + @VIEW_WIDTH]}
  end

  def clear_screen
    print "\e[2J"
  end

  def display_screen
    clear_screen
    display_title

    case @game_status
    when "starting"
      display_startup
    when "exploring"
      map = Marshal.load(Marshal.dump(@LOCATION_MAP))
      map = insert_avatar(map, @player_location)
      map = localize_map(@player_location, map)
      display_map(map)

      command = request_command
      handle_menu_command(command)
    when "encountering"
      clear_screen
      puts "You encountered a wild pokemon!"
      sleep(2)

      @game_status = "battling"
    when "battling"
      display_battle

      command = request_command
      handle_battle_command(command)
    when "finished"
      clear_screen
      puts "Fin."
      @game_status = "exit"
    end
  end

  def display_startup
    c = "\e[32m"
    d = "\e[39m"
    n = 4

    clear_screen
    @START_SCREEN.split("\n").each {|line|
      puts c+line+d
      sleep(0.25)
    }

    n.times {
      print "\n"
      sleep(0.25)
    }

    5.times {
      clear_screen
      puts @START_SCREEN
      print "\n"*(n + 1)
      sleep(0.2)

      clear_screen
      puts c+@START_SCREEN+d
      print "\n"*(n + 1)
      sleep(0.2)
    }

    sleep(0.2)

    @CREDITS.split("\n").each {|line|
      puts line
      sleep(0.4)
    }

    @game_status = "exploring"
  end

  def display_title
    puts @TITLE
  end

  def display_map(local_map)
    c = "\e[32m"
    d = "\e[39m"
    local_map.each_with_index {|row, i|
      print "|  "
      row.each {|cell|
        print cell == "w" ? c+cell+d : cell
      }
      print @EXPLORE_COMMANDS[i]
      print "\n"
    }
    print "\n"
  end

  def insert_avatar(map, player_location)
    c = "\e[31m"
    d = "\e[39m"
    map[player_location[:y]][player_location[:x]] = c+"Ω"+d
    map[player_location[:y] + 1][player_location[:x]] = c+"^"+d unless map[player_location[:y] + 1][player_location[:x]] == "w"
    map
  end

  def display_battle
    battle_view = generate_battle(@pokemon[0], @pokemon[1])
    battle_view.each_with_index {|line, i|
      puts line + @BATTLE_COMMANDS[i]
    }
  end

  def generate_battle(pokemon, opponent)
    opponent_name = opponent.name[0...21].ljust(21, " ")
    opponent_hp = opponent.hp.to_s[0...17].rjust(17, " ")
    name = pokemon.name[0...21].ljust(21, " ")
    hp = pokemon.hp.to_s[0...17].rjust(17, " ")
    [
      "+----------------------+",
      "| #{opponent_name}|",
      "|       --------       |",
      "| HP:#{opponent_hp} |",
      "+----------------------+",
      "                        ",
      "+----------------------+",
      "| #{name}|",
      "|       --------       |",
      "| HP:#{hp} |",
      "+----------------------+"
    ]
  end

  def request_command
    puts @game_status.upcase
    print "Enter your command: "
    gets.chomp.downcase
  end

  def move_avatar(direction)
    @player_location[:x] += direction[:x]
    @player_location[:y] += direction[:y]

    if @LOCATION_MAP[@player_location[:y] +1][@player_location[:x]] == "w" && rand(1..10) == 1
      @game_status = "encountering"
    end
  end

  def handle_menu_command(command)
    case command
    when "exit"
      @game_status = "exit"
    when "quit"
      @game_status = "exit"
    when "up"
      target_tile = @LOCATION_MAP[@player_location[:y] -1][@player_location[:x]]
      move_avatar({y: -1, x: 0}) unless @NONTRANVERSIBLE_TILES.include?(target_tile)
    when "down"
      target_tile = @LOCATION_MAP[@player_location[:y] +2][@player_location[:x]]
      move_avatar({y: 1, x: 0}) unless @NONTRANVERSIBLE_TILES.include?(target_tile)
    when "left"
      2.times {
        target_tile1 = @LOCATION_MAP[@player_location[:y]][@player_location[:x] -1]
        target_tile2 = @LOCATION_MAP[@player_location[:y] +1][@player_location[:x] -1]
        move_avatar({y: 0, x: -1}) unless @NONTRANVERSIBLE_TILES.include?(target_tile1) || @NONTRANVERSIBLE_TILES.include?(target_tile2)
      }
    when "right"
      2.times {
        target_tile1 = @LOCATION_MAP[@player_location[:y]][@player_location[:x] +1]
        target_tile2 = @LOCATION_MAP[@player_location[:y] +1][@player_location[:x] +1]
        move_avatar({y: 0, x: 1}) unless @NONTRANVERSIBLE_TILES.include?(target_tile1) || @NONTRANVERSIBLE_TILES.include?(target_tile2)
      }
    end
  end

  def handle_battle_command(command)
    pokemon = @pokemon[0]
    opponent = @pokemon[1]

    attack = pokemon.attacks.select {|atk| atk.name.downcase == command}.first

    case command
    when "exit"
      @game_status = "exit"
    when "quit"
      @game_status = "exit"
    when "shock"
      initial_hp = opponent.hp
      pokemon.perform_attack(attack, opponent)

      puts "You shocked #{opponent.name}!!!"
      sleep(1.5)
      puts "#{opponent.name} takes #{initial_hp - opponent.hp} damage."
      sleep(1.5)
    when "tackle"
      initial_hp = opponent.hp
      pokemon.perform_attack(attack, opponent)

      puts "You tackle #{opponent.name}!!!"
      sleep(1.5)
      puts "#{opponent.name} takes #{initial_hp - opponent.hp} damage."
      sleep(1.5)
    when "thunder"
      initial_hp = opponent.hp
      pokemon.perform_attack(attack, opponent)

      puts "You use Thunder!!!"
      sleep(1.5)
      puts "#{opponent.name} takes #{initial_hp - opponent.hp} damage."
      sleep(1.5)
    when "item"
      healing = pokemon.hp - 25
      pokemon.receive_attack(healing, "healing")

      puts "You healed your pokemon for #{healing.abs} points!"
      sleep(2)
    end

    if opponent.hp > 0 && @game_status != "exit"
      clear_screen
      display_title
      display_battle

      initial_hp = pokemon.hp
      attack = opponent.attacks.sample
      opponent.perform_attack(attack, pokemon)
      puts "#{opponent.name} uses #{attack.name}!!!"
      sleep(1.5)
      puts "You take #{initial_hp - pokemon.hp} damage."
      sleep(1.5)

      if pokemon.hp < 0
        puts "You whited out!"
        sleep(2)
        clear_screen
        puts "You lose!"
        sleep(2)

        @game_status = "finished"
      end
    else
      puts opponent.name + " fainted!"
      sleep(2)
      clear_screen
      puts "You win!"
      sleep(2)

      @game_status = "finished"
    end
  end

  def start
    until @game_status == "exit"
      display_screen
    end
  end

end

if (tests_complete)
  game = GameController.new
  game.start
end
