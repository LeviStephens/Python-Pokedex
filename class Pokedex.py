class Pokedex:
    def __init__(self):
        self.pokemon_data = {}

    def add_pokemon(self, number, name, entry):
        self.pokemon_data[number] = {'name': name, 'entry': entry}

    def get_pokemon_entry(self, number):
        return self.pokemon_data.get(number, "Pokemon not found in Pokedex.")

# Instantiate the Pokedex
pokedex = Pokedex()

# Add Generation 1 Pokemon and their entries
pokedex.add_pokemon(1, 'Bulbasaur', 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokemon.')
pokedex.add_pokemon(2, 'Ivysaur', 'When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.')
pokedex.add_pokemon(3, 'Venusaur', 'The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.')
pokedex.add_pokemon(4, 'Charmander', 'Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.')
pokedex.add_pokemon(5, 'Charmeleon', 'When it swings its burning tail, it elevates the temperature to unbearably high levels.')
pokedex.add_pokemon(6, 'Charizard', 'Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.')
pokedex.add_pokemon(7, 'Squirtle', 'After birth, its back swells and hardens into a shell. It powerfully sprays foam from its mouth.')
pokedex.add_pokemon(8, 'Wartortle', 'Often hides in water to stalk unwary prey. For swimming fast, it moves its ears to maintain balance.')
pokedex.add_pokemon(9, 'Blastoise', 'The jets of water it spouts from the rocket cannons on its shell can punch through thick steel.')
pokedex.add_pokemon(10, 'Caterpie', 'Its short feet are tipped with suction pads that enable it to tirelessly climb slopes and walls.')
pokedex.add_pokemon(11, 'Metapod', 'This is its pre-evolution form. At this stage, it can only harden, so it remains motionless to avoid attack.')
pokedex.add_pokemon(12, 'Butterfree', 'In battle, it flaps its wings at high speed to release highly toxic dust into the air.')
pokedex.add_pokemon(13, 'Weedle', 'Often found in forests and grasslands. It has a sharp, toxic barb of around two inches on top of its head.')
pokedex.add_pokemon(14, 'Kakuna', 'This is its pre-evolution form. Once it has reached this stage, it remains motionless until it evolves.')
pokedex.add_pokemon(15, 'Beedrill', 'It can take down any opponent with its powerful poison stingers. It sometimes attacks in swarms.')
pokedex.add_pokemon(16, 'Pidgey', 'A common sight in forests and woods. It flaps its wings at ground level to kick up blinding sand.')
pokedex.add_pokemon(17, 'Pidgeotto', 'This is its pre-evolution form. It evolves into Pidgeot starting at level 36.')
pokedex.add_pokemon(18, 'Pidgeot', 'When hunting, it skims the surface of water at high speed to pick off unwary prey such as Magikarp.')
pokedex.add_pokemon(19, 'Rattata', 'Its fangs are long and very sharp. They grow continuously, so it gnaws on hard things to whittle them down.')
pokedex.add_pokemon(20, 'Raticate', 'Its hind feet are webbed, so it’s a strong swimmer. It can cross rivers and sometimes even oceans.')
pokedex.add_pokemon(21, 'Spearow', 'This is its pre-evolution form. It evolves into Fearow starting at level 20.')
pokedex.add_pokemon(22, 'Fearow', 'It circles in the sky, keeping a keen eye out for Pokemon in the mountains’ grass. It swoops to strike and carry prey off to its nest.')
pokedex.add_pokemon(23, 'Ekans', 'It flutters the tip of its tongue to seek out the scent of prey, then swallows the prey whole.')
pokedex.add_pokemon(24, 'Arbok', 'It is rumored that the ferocious warning markings on its belly differ from area to area.')
pokedex.add_pokemon(25, 'Pikachu', 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.')
pokedex.add_pokemon(26, 'Raichu', 'Its electric charges can reach even 100,000 volts. Careless contact can cause even an Indian elephant to faint.')
pokedex.add_pokemon(27, 'Sandshrew', 'It burrows and lives underground. If threatened, it curls itself up into a ball for protection.')
pokedex.add_pokemon(28, 'Sandslash', 'It is skilled at slashing enemies with its claws. If broken, they start to grow back in a day.')
pokedex.add_pokemon(29, 'Nidoran♀', 'It constantly moves its large ears in many directions in order to detect danger right away.')
pokedex.add_pokemon(30, 'Nidorina', 'This is its pre-evolution form. It evolves into Nidoqueen starting at level 16.')
pokedex.add_pokemon(31, 'Nidoqueen', 'Its hard scales provide strong protection. It uses its hefty bulk to execute powerful moves.')
pokedex.add_pokemon(32, 'Nidoran♂', 'The larger the horn, the more powerful its secreted venom. For this reason, it is unsafe to approach it.')
pokedex.add_pokemon(33, 'Nidorino', 'Its horn contains venom. If it stabs an enemy with the horn, the impact makes the poison leak out.')
pokedex.add_pokemon(34, 'Nidoking', 'One swing of its mighty tail can snap a telephone pole as if it were a matchstick.')
pokedex.add_pokemon(35, 'Clefairy', 'It is said that happiness will come to those who see a gathering of Clefairy under a full moon.')
pokedex.add_pokemon(36, 'Clefable', 'Its very sensitive ears let it distinguish what kinds of prey are around, even in complete darkness.')
pokedex.add_pokemon(37, 'Vulpix', 'While young, it has six gorgeous tails. When it grows, several new tails are sprouted.')
pokedex.add_pokemon(38, 'Ninetales', 'Legend has it that Ninetales came into being when nine wizards possessing sacred powers merged into one.')
pokedex.add_pokemon(39, 'Jigglypuff', 'It captivates foes with its huge, round eyes and puts them to sleep by singing a lullaby.')
pokedex.add_pokemon(40, 'Wigglytuff', 'This is its pre-evolution form. It evolves from Jigglypuff when exposed to a Moon Stone.')
pokedex.add_pokemon(41, 'Zubat', 'Forms colonies in perpetually dark places. Uses ultrasonic waves to identify and approach targets.')
pokedex.add_pokemon(42, 'Golbat', 'It can drink more than 10 ounces of blood at once. If it has too much, it gets heavy and flies clumsily.')
pokedex.add_pokemon(43, 'Oddish', 'It is nocturnal and active in the evening and early morning. It is known to burst into bloom in the evening.')
pokedex.add_pokemon(44, 'Gloom', 'This is its pre-evolution form. It evolves into Vileplume starting at level 21.')
pokedex.add_pokemon(45, 'Vileplume', 'The bud bursts into bloom with a bang. It then starts scattering allergenic, poisonous pollen.')
pokedex.add_pokemon(46, 'Paras', 'Burrows under the ground to gnaw on tree roots. The mushrooms on its back grow by drawing nutrients from the bug host.')
pokedex.add_pokemon(47, 'Parasect', 'The mushroom on its back grows by drawing nutrients from the bug host. It often has its parasitic tendrils attached to the host.')
pokedex.add_pokemon(48, 'Venonat', 'Lives in the shadows of tall trees where it eats bugs. It is attracted by light at night.')
pokedex.add_pokemon(49, 'Venomoth', 'The wings are covered with dust-like scales. Every time it flaps its wings, it looses highly toxic dust.')
pokedex.add_pokemon(50, 'Diglett', 'It leaves its nest at dawn. By burrowing rapidly, it can surprise its enemies coming up from below.')
pokedex.add_pokemon(51, 'Dugtrio', 'This is its pre-evolution form. It evolves from Diglett starting at level 26.')
pokedex.add_pokemon(52, 'Meowth', 'Adores round objects. It wanders the streets on a nightly basis to look for dropped loose change.')
pokedex.add_pokemon(53, 'Persian', 'It has a distinctively sweet-and-sour scent. The scent acts to sharply raise the foe’s spirit.')
pokedex.add_pokemon(54, 'Psyduck', 'While lulling its enemies with its vacant look, this wily Pokemon will use psychokinetic powers.')
pokedex.add_pokemon(55, 'Golduck', 'It appears by waterways at dusk. It may use telekinetic powers if its forehead glows mysteriously.')
pokedex.add_pokemon(56, 'Mankey', 'It becomes wildly furious if it even senses someone looking at it. It chases anyone that meets its glare.')
pokedex.add_pokemon(57, 'Primeape', 'It has been known to become so angry that it dies as a result. Its face looks peaceful in death, however.')
pokedex.add_pokemon(58, 'Growlithe', 'While it is young, it uses the horn on its head to pierce the shell of its molted shell to get it started.')
pokedex.add_pokemon(59, 'Arcanine', 'Its magnificent bark conveys a sense of majesty. Anyone hearing it can’t help but grovel before it.')
pokedex.add_pokemon(60, 'Poliwag', 'The direction of its belly spiral differs by area. The equator is thought to have an effect on this.')
pokedex.add_pokemon(61, 'Poliwhirl', 'The direction of the spiral on its belly differs by area. It is more adept at swimming than walking.')
pokedex.add_pokemon(62, 'Poliwrath', 'Swims powerfully using all the muscles in its body. It can even overtake champion swimmers.')
pokedex.add_pokemon(63, 'Abra', 'Using its ability to read minds, it will identify impending danger and teleport to safety.')
pokedex.add_pokemon(64, 'Kadabra', 'This is its pre-evolution form. It evolves from Abra starting at level 16.')
pokedex.add_pokemon(65, 'Alakazam', 'Its brain can outperform a supercomputer. Its intelligence quotient is said to be 5,000.')
pokedex.add_pokemon(66, 'Machop', 'This is its pre-evolution form. It evolves into Machoke starting at level 28.')
pokedex.add_pokemon(67, 'Machoke', 'Its muscular body is so powerful that it must wear a power-save belt to be able to regulate its motions.')
pokedex.add_pokemon(68, 'Machamp', 'It uses its four powerful arms to pin the limbs of its foe, then throws the victim over the horizon.')
pokedex.add_pokemon(69, 'Bellsprout', 'A carnivorous Pokemon that traps and eats bugs. It uses its root feet to soak up needed moisture.')
pokedex.add_pokemon(70, 'Weepinbell', 'This is its pre-evolution form. It evolves into Victreebel starting at level 21.')
pokedex.add_pokemon(71, 'Victreebel', 'Lures prey with the sweet aroma of honey. Swallowed whole, the prey is dissolved in a day.')
pokedex.add_pokemon(72, 'Tentacool', 'While luring in its prey using its honey, it hurls a tentacle into them. Once they’re attacked, prey can’t escape.')
pokedex.add_pokemon(73, 'Tentacruel', 'The tentacles are normally kept short. On hunts, the Pokemon uses its longer tentacles to immobilize its prey.')
pokedex.add_pokemon(74, 'Geodude', 'Found in fields and mountains. Mistaking them for boulders, people often step or trip on them.')
pokedex.add_pokemon(75, 'Graveler', 'Rolls down slopes to move. It rolls over any obstacle without slowing or changing its direction.')
pokedex.add_pokemon(76, 'Golem', 'Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without taking damage.')
pokedex.add_pokemon(77, 'Ponyta', 'When full of life, the Pokemon’s fur will stand on end and sometimes it will neigh rather coquettishly.')
pokedex.add_pokemon(78, 'Rapidash', 'Very competitive, this Pokemon will chase anything that moves fast in the hopes of racing it.')
pokedex.add_pokemon(79, 'Slowpoke', 'A sweet sap leaks from its tail’s tip. Although not nutritious, the tail is pleasant to chew on.')
pokedex.add_pokemon(80, 'Slowbro', 'Being bitten by Shellder makes it spout spiral energy out of its Shellder’s shell.')
pokedex.add_pokemon(81, 'Magnemite', 'If any metal object is close, it will be drawn to it. It exudes electricity from all over its body.')
pokedex.add_pokemon(82, 'Magneton', 'Magnemite is its pre-evolution form. It evolves from Magnemite when leveled up in areas called Electric Fields.')
pokedex.add_pokemon(83, 'Farfetch\'d', 'If anyone tries to disturb where the essential plant stalks grow, it uses its own stalk to thwart them.')
pokedex.add_pokemon(84, 'Doduo', 'It races through grassy plains with powerful strides, using its two heads to thrash the grass into submission.')
pokedex.add_pokemon(85, 'Dodrio', 'It has two powerful legs and three equally powerful heads. It has three sets of hearts and lungs as well.')
pokedex.add_pokemon(86, 'Seel', 'The horn on its head is sharp. It pops inflated rubber rafts and operates as a buoy when its head is submerged in water.')
pokedex.add_pokemon(87, 'Dewgong', 'It sleeps under shallow ocean waters during the day, then looks for food in tidal pools during the night.')
pokedex.add_pokemon(88, 'Grimer', 'Born from polluted sludge in the sea, Grimer’s favorite food is anything filthy. They feed on wastewater pumped out from factories.')
pokedex.add_pokemon(89, 'Muk', 'Thickly covered with a filthy, vile sludge. It is so toxic, even its footprints contain poison.')
pokedex.add_pokemon(90, 'Shellder', 'Its hard shell repels any kind of attack. It is vulnerable only when its shell is open.')
pokedex.add_pokemon(91, 'Cloyster', 'For protection, it uses its harder-than-diamonds shell. It also shoots spikes from the shell.')
pokedex.add_pokemon(92, 'Gastly', 'It’s nocturnal, so it wanders around at night. It avoids sunlight and stays close to dark places.')
pokedex.add_pokemon(93, 'Haunter', 'This is its pre-evolution form. It evolves from Gastly starting at level 25.')
pokedex.add_pokemon(94, 'Gengar', 'It has been said that it swallows those who get too close and that it puts up against the weak with a sinister grin on its face.')
pokedex.add_pokemon(95, 'Onix', 'This is its pre-evolution form. It evolves from Onix when leveled up while holding a Metal Coat.')
pokedex.add_pokemon(96, 'Drowzee', 'The longer it drowses, the more it talks about its dreams, which leaves everyone in awe.')
pokedex.add_pokemon(97, 'Hypno', 'When it locks eyes with an enemy, it will use a mix of moves to beguile the foe with a wide range of illusions.')
pokedex.add_pokemon(98, 'Krabby', 'It can be found near the sea. The large pincers grow back if they are torn out of their sockets.')
pokedex.add_pokemon(99, 'Kingler', 'The pincers break off easily. If it loses a pincer, it somehow becomes incapable of walking sideways.')
pokedex.add_pokemon(100, 'Voltorb', 'It was discovered when Poke Balls were introduced. It is said that there is some connection.')
pokedex.add_pokemon(101, 'Electrode', 'This is its pre-evolution form. It evolves from Voltorb when leveled up to level 30.')
pokedex.add_pokemon(102, 'Exeggcute', 'The heads attract each other and spin around. There must be 6 heads for it to maintain balance.')
pokedex.add_pokemon(103, 'Exeggutor', 'Its cries are very noisy. This is because each of the three heads thinks about whatever it likes.')
pokedex.add_pokemon(104, 'Cubone', 'Always wearing the skull of its deceased mother, it cries for the mother it will never see again.')
pokedex.add_pokemon(105, 'Marowak', 'The bone it holds is its key weapon. It throws the bone skillfully like a boomerang to KO targets.')
pokedex.add_pokemon(106, 'Hitmonlee', 'Its legs freely contract and stretch. The stretch of its legs allow it to hit a distant foe with a rising kick.')
pokedex.add_pokemon(107, 'Hitmonchan', 'Its punches slice the air. However, it seems to need a short break after fighting for three minutes.')
pokedex.add_pokemon(108, 'Lickitung', 'Its long tongue, slathered with a gooey saliva, sticks to anything, so it is very useful.')
pokedex.add_pokemon(109, 'Koffing', 'Its thin, balloon-like membrane is very sensitive. If it is damaged, it leaks a sticky, fluid.')
pokedex.add_pokemon(110, 'Weezing', 'It is highly sensitive to air pollution. If it smells toxic fumes, it will spit out a powerful, destructive fluid from its mouth.')
pokedex.add_pokemon(111, 'Rhyhorn', 'The impact of this Pokemon running along rocky mountains makes a sound like thunder.')
pokedex.add_pokemon(112, 'Rhydon', 'Protected by an armor-like hide, it is capable of living in molten lava of 3,600 degrees Fahrenheit.')
pokedex.add_pokemon(113, 'Chansey', 'It lays several eggs a day. The eggs are apparently rich in nutrients and extremely delicious.')
pokedex.add_pokemon(114, 'Tangela', 'During battle, it constantly moves the vines that cover its body in order to annoy its opponent.')
pokedex.add_pokemon(115, 'Kangaskhan', 'It has a good temperament and prefers not to fight. If it is angered, however, it will pulverize opponents.')
pokedex.add_pokemon(116, 'Horsea', 'If it senses any danger, it will vigorously spray water or a special type of ink from its mouth.')
pokedex.add_pokemon(117, 'Seadra', 'This is its pre-evolution form. It evolves from Horsea starting at level 32.')
pokedex.add_pokemon(118, 'Goldeen', 'It swims at a steady 5 knots. If it senses danger, it will strike back with its sharp horn.')
pokedex.add_pokemon(119, 'Seaking', 'During spawning season, Seaking gather from all over, coloring the waters its hue with their bodies.')
pokedex.add_pokemon(120, 'Staryu', 'At night, the center of its body slowly flickers with the same rhythm as a human heartbeat.')
pokedex.add_pokemon(121, 'Starmie', 'It can reconstitute its entire cellular structure to change into what it sees, but it returns to normal when it relaxes.')
pokedex.add_pokemon(122, 'Mr. Mime', 'If interrupted while it is miming, it will slap around the offender with its broad hands.')
pokedex.add_pokemon(123, 'Scyther', 'If it moves too quickly, the confusion of its three heads makes it tough to aim properly.')
pokedex.add_pokemon(124, 'Jynx', 'It speaks a language similar to that of humans. However, it seems to use dancing to communicate.')
pokedex.add_pokemon(125, 'Electabuzz', 'This is its pre-evolution form. It evolves from Elekid when leveled up while holding an Electirizer.')
pokedex.add_pokemon(126, 'Magmar', 'When angered, it spouts brilliant fire from all over its body. It doesn’t calm down until it burns everything down.')
pokedex.add_pokemon(127, 'Pinsir', 'If it fails to crush the victim in its pincers, it will swing it around and toss it hard.')
pokedex.add_pokemon(128, 'Tauros', 'They fight each other by locking horns. The herd’s protector takes pride in its battle-scarred horns.')
pokedex.add_pokemon(129, 'Magikarp', 'It is said to be the world’s weakest Pokemon. No one knows why it has managed to survive.')
pokedex.add_pokemon(130, 'Gyarados', 'When it is angered, it immediately evolves into a much larger Gyarados.')
pokedex.add_pokemon(131, 'Lapras', 'A kindhearted Pokemon that leads lost and foundering ships in a storm to the safety of land.')
pokedex.add_pokemon(132, 'Ditto', 'It can transform into anything. When it sleeps, it changes into a stone to avoid being attacked.')
pokedex.add_pokemon(133, 'Eevee', 'It has the ability to alter the composition of its body to suit its surrounding environment.')
pokedex.add_pokemon(134, 'Vaporeon', 'It has evolved to be suitable for an aquatic life. It can invisibly melt away into water.')
pokedex.add_pokemon(135, 'Jolteon', 'If agitated, it uses electricity to straighten out its fur and launch it in small bunches.')
pokedex.add_pokemon(136, 'Flareon', 'It has a flame bag inside its body. After inhaling deeply, it blows out flames of nearly 3,100 degrees Fahrenheit.')
pokedex.add_pokemon(137, 'Porygon', 'A man-made Pokemon that consists entirely of programming code. It is capable of moving freely in cyberspace.')
pokedex.add_pokemon(138, 'Omanyte', 'A Pokemon that was resurrected from a fossil found in what was once the ocean floor eons ago.')
pokedex.add_pokemon(139, 'Omastar', 'Despite having strong enough limbs to crawl out of the ocean, it also had to have a means of maintaining buoyancy in the water.')
pokedex.add_pokemon(140, 'Kabuto', 'A Pokemon that was resurrected from a fossil found in what was once the ocean floor eons ago.')
pokedex.add_pokemon(141, 'Kabutops', 'It is thought that this Pokemon came onto land because its prey adapted to life on land.')
pokedex.add_pokemon(142, 'Aerodactyl', 'A Pokemon from the age of dinosaurs. It was regenerated from a fossil using advanced scientific means.')
pokedex.add_pokemon(143, 'Snorlax', 'It is not satisfied unless it eats over 880 pounds of food every day. When it is done eating, it goes promptly to sleep.')
pokedex.add_pokemon(144, 'Articuno', 'A legendary bird Pokemon that is said to appear to doomed people who are lost in icy mountains.')
pokedex.add_pokemon(145, 'Zapdos', 'This is its pre-evolution form. It evolves from Elekid when leveled up while holding a Magnet.')
pokedex.add_pokemon(146, 'Moltres', 'A Pokemon that is said to live in thunderclouds. It freely controls lightning bolts.')
pokedex.add_pokemon(147, 'Dratini', 'It grows by molting repeatedly. Boots it made from the tanned cast-off skins of its moltings are a super luxury item.')
pokedex.add_pokemon(148, 'Dragonair', 'This is its pre-evolution form. It evolves from Dratini starting at level 30.')
pokedex.add_pokemon(149, 'Dragonite', 'This Pokemon is a powerful flier that is also adept at walking on legs. It is capable of circling the globe in just 16 hours.')
pokedex.add_pokemon(150, 'Mewtwo', 'A Pokemon created by recombining Mew’s genes. Its DNA is almost the same as Mew’s.')
pokedex.add_pokemon(151, 'Mew', 'A Pokemon of South America that was thought to have been extinct. It is very intelligent and learns any move.')
# Continue adding entries for the remaining Generation 1 Pokemon...

# User interaction loop
while True:
    try:
        # Prompt the user for input
        user_input = input("What Pokemon would you like to view? Enter a number (1-151) or 'exit' to quit: ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting Pokedex. Goodbye!")
            break

        # Convert user input to an integer
        pokemon_number = int(user_input)

        # Get and display the Pokedex entry
        entry = pokedex.get_pokemon_entry(pokemon_number)
        print(f'#{pokemon_number} - {entry["name"]}: {entry["entry"]}')

    except ValueError:
        print("Please enter a valid number or 'exit'.")
    except KeyboardInterrupt:
        print("\nExiting Pokedex. Goodbye!")
        break
