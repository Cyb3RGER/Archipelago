from BaseClasses import Item
import typing


class ItemData(typing.NamedTuple):
    id: typing.Optional[int]
    is_progression: bool
    is_trap: bool


class TheBindingOfIsaacRebirthItem(Item):
    game: str = "The Binding of Isaac Rebirth"


junk_items = {
    "Random Pickup": ItemData(78031, False, False),
    "Random Heart": ItemData(78032, False, False),
    "Random Coin": ItemData(78033, False, False),
    "Random Bomb": ItemData(78034, False, False),
    "Random Key": ItemData(78035, False, False),
    "Random Card": ItemData(78036, False, False),
    "Random Pill": ItemData(78037, False, False),
    "Random Chest": ItemData(78038, False, False),
    "Random Trinket": ItemData(78039, False, False),
}

trap_items = {
    "Troll Bomb Trap": ItemData(78772, False, True),
    "Teleport Trap": ItemData(78773, False, True),
    "Retro Vision Trap": ItemData(78774, False, True),
    "Curse Trap": ItemData(78775, False, True),
}

# 78000 - 78???
item_table = {
    # items (main)
    "Treasure Room Item": ItemData(78000, True, False),
    "Shop Item": ItemData(78001, True, False),
    "Boss Item": ItemData(78002, True, False),
    "Devil Deal Item": ItemData(78003, True, False),
    "Angle Deal Item": ItemData(78004, True, False),
    "Secret Room Item": ItemData(78005, True, False),
    "Library Item": ItemData(78006, True, False),
    "Curse Room Item": ItemData(78007, True, False),
    "Planetarium Item": ItemData(78008, True, False),
    # item (experimental)
    "Shell Game Item": ItemData(78009, True, False),
    "Golden Chest Item": ItemData(78010, True, False),
    "Red Chest Item": ItemData(78011, True, False),
    "Beggar Item": ItemData(78012, True, False),
    "Demon Baggar Item": ItemData(78013, True, False),
    "Key Master Item": ItemData(78014, True, False),
    "Battery Bum Item": ItemData(78015, True, False),
    "Mom's Chest Item": ItemData(78016, True, False),
    "Greed Treasure Room Item": ItemData(78017, True, False),
    "Greed Boss Item": ItemData(78018, True, False),
    "Greed Shop Item": ItemData(78019, True, False),
    "Greed Devil Deal Item": ItemData(78020, True, False),
    "Greed Angel Deal Item": ItemData(78021, True, False),
    "Greed Curse Room Item": ItemData(78022, True, False),
    "Greed Secret Room Item": ItemData(78023, True, False),
    "Crane Game Item": ItemData(78024, True, False),
    "Ultra Secret Room Item": ItemData(78025, True, False),
    "Bomb Bum Item": ItemData(78026, True, False),
    "Old Chest Item": ItemData(78027, True, False),
    "Baby Shop Item": ItemData(78028, True, False),
    "Wooden Chest Item": ItemData(78029, True, False),
    "Rotten Beggar Item": ItemData(78030, True, False),
    **junk_items,
    # all collectables -> for start inv
    "Sad Onion": ItemData(78040, True, False),
    "Inner Eye": ItemData(78041, True, False),
    "Spoon Bender": ItemData(78042, True, False),
    "Crickets Head": ItemData(78043, True, False),
    "My Reflection": ItemData(78044, True, False),
    "Number One": ItemData(78045, True, False),
    "Blood Of The Martyr": ItemData(78046, True, False),
    "Brother Bobby": ItemData(78047, True, False),
    "Skatole": ItemData(78048, True, False),
    "Halo Of Flies": ItemData(78049, True, False),
    "1up": ItemData(78050, True, False),
    # 78050 need alias One Up
    "Magic Mushroom": ItemData(78051, True, False),
    "Virus": ItemData(78052, True, False),
    "Roid Rage": ItemData(78053, True, False),
    "Heart": ItemData(78054, True, False),
    "Raw Liver": ItemData(78055, True, False),
    "Skeleton Key": ItemData(78056, True, False),
    "Dollar": ItemData(78057, True, False),
    "Boom": ItemData(78058, True, False),
    "Transcendence": ItemData(78059, True, False),
    "Compass": ItemData(78060, True, False),
    "Lunch": ItemData(78061, True, False),
    "Dinner": ItemData(78062, True, False),
    "Dessert": ItemData(78063, True, False),
    "Breakfast": ItemData(78064, True, False),
    "Rotten Meat": ItemData(78065, True, False),
    "Wooden Spoon": ItemData(78066, True, False),
    "Belt": ItemData(78067, True, False),
    "Moms Underwear": ItemData(78068, True, False),
    "Moms Heels": ItemData(78069, True, False),
    "Moms Lipstick": ItemData(78070, True, False),
    "Wire Coat Hanger": ItemData(78071, True, False),
    "Bible": ItemData(78072, True, False),
    "Book Of Belial": ItemData(78073, True, False),
    "Necronomicon": ItemData(78074, True, False),
    "Poop": ItemData(78075, True, False),
    "Mr Boom": ItemData(78076, True, False),
    "Tammys Head": ItemData(78077, True, False),
    "Moms Bra": ItemData(78078, True, False),
    "Kamikaze": ItemData(78079, True, False),
    "Moms Pad": ItemData(78080, True, False),
    "Bobs Rotten Head": ItemData(78081, True, False),
    # "Pills Here": ItemData(78082, True, False), #doesn't exist
    "Teleport": ItemData(78083, True, False),
    "Yum Heart": ItemData(78084, True, False),
    "Lucky Foot": ItemData(78085, True, False),
    "Doctors Remote": ItemData(78086, True, False),
    "Cupids Arrow": ItemData(78087, True, False),
    "Shoop Da Whoop": ItemData(78088, True, False),
    "Steven": ItemData(78089, True, False),
    "Pentagram": ItemData(78090, True, False),
    "Dr Fetus": ItemData(78091, True, False),
    "Magneto": ItemData(78092, True, False),
    "Treasure Map": ItemData(78093, True, False),
    "Moms Eye": ItemData(78094, True, False),
    "Lemon Mishap": ItemData(78095, True, False),
    "Distant Admiration": ItemData(78096, True, False),
    "Book Of Shadows": ItemData(78097, True, False),
    "Book Of Belial Passive": ItemData(78098, True, False),
    "Ladder": ItemData(78099, True, False),
    # "Tarot Card": ItemData(78100, True, False), # doesn't exist
    "Charm Vampire": ItemData(78101, True, False),
    "Battery": ItemData(78102, True, False),
    "Steam Sale": ItemData(78103, True, False),
    "Anarchist Cookbook": ItemData(78104, True, False),
    "Hourglass": ItemData(78105, True, False),
    "Sister Maggy": ItemData(78106, True, False),
    "Technology": ItemData(78107, True, False),
    "Chocolate Milk": ItemData(78108, True, False),
    "Growth Hormones": ItemData(78109, True, False),
    "Mini Mush": ItemData(78110, True, False),
    "Rosary": ItemData(78111, True, False),
    "Cube Of Meat": ItemData(78112, True, False),
    "Quarter": ItemData(78113, True, False),
    "Phd": ItemData(78114, True, False),
    "Xray Vision": ItemData(78115, True, False),
    "My Little Unicorn": ItemData(78116, True, False),
    "Book Of Revelations": ItemData(78117, True, False),
    "Mark": ItemData(78118, True, False),
    "Pact": ItemData(78119, True, False),
    "Dead Cat": ItemData(78120, True, False),
    "Lord Of The Pit": ItemData(78121, True, False),
    "The Nail": ItemData(78122, True, False),
    "We Need To Go Deeper": ItemData(78123, True, False),
    "Deck Of Cards": ItemData(78124, True, False),
    "Monstros Tooth": ItemData(78125, True, False),
    "Lokis Horns": ItemData(78126, True, False),
    "Little Chubby": ItemData(78127, True, False),
    "Spider Bite": ItemData(78128, True, False),
    "Small Rock": ItemData(78129, True, False),
    "Spelunker Hat": ItemData(78130, True, False),
    "Super Bandage": ItemData(78131, True, False),
    "Gamekid": ItemData(78132, True, False),
    "Sack Of Pennies": ItemData(78133, True, False),
    "Robo Baby": ItemData(78134, True, False),
    "Little Chad": ItemData(78135, True, False),
    "Book Of Sin": ItemData(78136, True, False),
    "Relic": ItemData(78137, True, False),
    "Little Gish": ItemData(78138, True, False),
    "Little Steven": ItemData(78139, True, False),
    "Halo": ItemData(78140, True, False),
    "Moms Bottle Of Pills": ItemData(78141, True, False),
    "Common Cold": ItemData(78142, True, False),
    "Parasite": ItemData(78143, True, False),
    "D6": ItemData(78144, True, False),
    "Mr Mega": ItemData(78145, True, False),
    "Pinking Shears": ItemData(78146, True, False),
    "Wafer": ItemData(78147, True, False),
    "Money Equals Power": ItemData(78148, True, False),
    "Moms Contacts": ItemData(78149, True, False),
    "Bean": ItemData(78150, True, False),
    "Guardian Angel": ItemData(78151, True, False),
    "Demon Baby": ItemData(78152, True, False),
    "Moms Knife": ItemData(78153, True, False),
    "Ouija Board": ItemData(78154, True, False),
    "9 Volt": ItemData(78155, True, False),
    # 78155 need alias Nine Volt
    "Dead Bird": ItemData(78156, True, False),
    "Brimstone": ItemData(78157, True, False),
    "Blood Bag": ItemData(78158, True, False),
    "Odd Mushroom Thin": ItemData(78159, True, False),
    "Odd Mushroom Large": ItemData(78160, True, False),
    "Whore Of Babylon": ItemData(78161, True, False),
    "Monster Manual": ItemData(78162, True, False),
    "Dead Sea Scrolls": ItemData(78163, True, False),
    "Bobby Bomb": ItemData(78164, True, False),
    "Razor Blade": ItemData(78165, True, False),
    "Forget Me Now": ItemData(78166, True, False),
    "Forever Alone": ItemData(78167, True, False),
    "Bucket Of Lard": ItemData(78168, True, False),
    "Pony": ItemData(78169, True, False),
    "Bomb Bag": ItemData(78170, True, False),
    "Lump Of Coal": ItemData(78171, True, False),
    "Guppys Paw": ItemData(78172, True, False),
    "Guppys Tail": ItemData(78173, True, False),
    "Iv Bag": ItemData(78174, True, False),
    "Best Friend": ItemData(78175, True, False),
    "Remote Detonator": ItemData(78176, True, False),
    "Stigmata": ItemData(78177, True, False),
    "Moms Purse": ItemData(78178, True, False),
    "Bobs Curse": ItemData(78179, True, False),
    "Pageant Boy": ItemData(78180, True, False),
    "Scapular": ItemData(78181, True, False),
    "Speed Ball": ItemData(78182, True, False),
    "Bum Friend": ItemData(78183, True, False),
    "Guppys Head": ItemData(78184, True, False),
    "Prayer Card": ItemData(78185, True, False),
    "Notched Axe": ItemData(78186, True, False),
    "Infestation": ItemData(78187, True, False),
    "Ipecac": ItemData(78188, True, False),
    "Tough Love": ItemData(78189, True, False),
    "Mulligan": ItemData(78190, True, False),
    "Technology 2": ItemData(78191, True, False),
    "Mutant Spider": ItemData(78192, True, False),
    "Chemical Peel": ItemData(78193, True, False),
    "Peeper": ItemData(78194, True, False),
    "Habit": ItemData(78195, True, False),
    "Bloody Lust": ItemData(78196, True, False),
    "Crystal Ball": ItemData(78197, True, False),
    "Spirit Of The Night": ItemData(78198, True, False),
    "Crack The Sky": ItemData(78199, True, False),
    "Ankh": ItemData(78200, True, False),
    "Celtic Cross": ItemData(78201, True, False),
    "Ghost Baby": ItemData(78202, True, False),
    "Candle": ItemData(78203, True, False),
    "Cat O Nine Tails": ItemData(78204, True, False),
    "D20": ItemData(78205, True, False),
    "Harlequin Baby": ItemData(78206, True, False),
    "Epic Fetus": ItemData(78207, True, False),
    "Polyphemus": ItemData(78208, True, False),
    "Daddy Longlegs": ItemData(78209, True, False),
    "Spider Butt": ItemData(78210, True, False),
    "Sacrificial Dagger": ItemData(78211, True, False),
    "Mitre": ItemData(78212, True, False),
    "Rainbow Baby": ItemData(78213, True, False),
    "Dads Key": ItemData(78214, True, False),
    "Stem Cells": ItemData(78215, True, False),
    "Portable Slot": ItemData(78216, True, False),
    "Holy Water": ItemData(78217, True, False),
    "Fate": ItemData(78218, True, False),
    "Black Bean": ItemData(78219, True, False),
    "White Pony": ItemData(78220, True, False),
    "Sacred Heart": ItemData(78221, True, False),
    "Tooth Picks": ItemData(78222, True, False),
    "Holy Grail": ItemData(78223, True, False),
    "Dead Dove": ItemData(78224, True, False),
    "Blood Rights": ItemData(78225, True, False),
    "Guppys Hairball": ItemData(78226, True, False),
    "Abel": ItemData(78227, True, False),
    "Smb Super Fan": ItemData(78228, True, False),
    "Pyro": ItemData(78229, True, False),
    "3 Dollar Bill": ItemData(78230, True, False),
    "Telepathy Book": ItemData(78231, True, False),
    "Meat": ItemData(78232, True, False),
    "Magic 8 Ball": ItemData(78233, True, False),
    "Moms Coin Purse": ItemData(78234, True, False),
    "Squeezy": ItemData(78235, True, False),
    "Jesus Juice": ItemData(78236, True, False),
    "Box": ItemData(78237, True, False),
    "Moms Key": ItemData(78238, True, False),
    "Moms Eyeshadow": ItemData(78239, True, False),
    "Iron Bar": ItemData(78240, True, False),
    "Midas Touch": ItemData(78241, True, False),
    "Humbleing Bundle": ItemData(78242, True, False),
    "Fanny Pack": ItemData(78243, True, False),
    "Sharp Plug": ItemData(78244, True, False),
    "Guillotine": ItemData(78245, True, False),
    "Ball Of Bandages": ItemData(78246, True, False),
    "Champion Belt": ItemData(78247, True, False),
    "Butt Bombs": ItemData(78248, True, False),
    "Gnawed Leaf": ItemData(78249, True, False),
    "Spiderbaby": ItemData(78250, True, False),
    "Guppys Collar": ItemData(78251, True, False),
    "Lost Contact": ItemData(78252, True, False),
    "Anemic": ItemData(78253, True, False),
    "Goat Head": ItemData(78254, True, False),
    "Ceremonial Robes": ItemData(78255, True, False),
    "Moms Wig": ItemData(78256, True, False),
    "Placenta": ItemData(78257, True, False),
    "Old Bandage": ItemData(78258, True, False),
    "Sad Bombs": ItemData(78259, True, False),
    "Rubber Cement": ItemData(78260, True, False),
    "Anti Gravity": ItemData(78261, True, False),
    "Pyromaniac": ItemData(78262, True, False),
    "Crickets Body": ItemData(78263, True, False),
    "Gimpy": ItemData(78264, True, False),
    "Black Lotus": ItemData(78265, True, False),
    "Piggy Bank": ItemData(78266, True, False),
    "Moms Perfume": ItemData(78267, True, False),
    "Monstros Lung": ItemData(78268, True, False),
    "Abaddon": ItemData(78269, True, False),
    "Ball Of Tar": ItemData(78270, True, False),
    "Stop Watch": ItemData(78271, True, False),
    "Tiny Planet": ItemData(78272, True, False),
    "Infestation 2": ItemData(78273, True, False),
    # "235": ItemData(78274, True, False), #doesn't exist
    "E Coli": ItemData(78275, True, False),
    "Deaths Touch": ItemData(78276, True, False),
    "Key Piece 1": ItemData(78277, True, False),
    "Key Piece 2": ItemData(78278, True, False),
    "Experimental Treatment": ItemData(78279, True, False),
    "Contract From Below": ItemData(78280, True, False),
    "Infamy": ItemData(78281, True, False),
    "Trinity Shield": ItemData(78282, True, False),
    "Tech 5": ItemData(78283, True, False),
    "20 20": ItemData(78284, True, False),
    "Blue Map": ItemData(78285, True, False),
    "Bffs": ItemData(78286, True, False),
    "Hive Mind": ItemData(78287, True, False),
    "Theres Options": ItemData(78288, True, False),
    "Bogo Bombs": ItemData(78289, True, False),
    "Starter Deck": ItemData(78290, True, False),
    "Little Baggy": ItemData(78291, True, False),
    "Magic Scab": ItemData(78292, True, False),
    "Blood Clot": ItemData(78293, True, False),
    "Screw": ItemData(78294, True, False),
    "Hot Bombs": ItemData(78295, True, False),
    "Fire Mind": ItemData(78296, True, False),
    "Missing No": ItemData(78297, True, False),
    "Dark Matter": ItemData(78298, True, False),
    "Black Candle": ItemData(78299, True, False),
    "Proptosis": ItemData(78300, True, False),
    "Missing Page 2": ItemData(78301, True, False),
    "Clear Rune": ItemData(78302, True, False),
    "Smart Fly": ItemData(78303, True, False),
    "Dry Baby": ItemData(78304, True, False),
    "Juicy Sack": ItemData(78305, True, False),
    "Robo Baby 2": ItemData(78306, True, False),
    "Rotten Baby": ItemData(78307, True, False),
    "Headless Baby": ItemData(78308, True, False),
    "Leech": ItemData(78309, True, False),
    "Mystery Sack": ItemData(78310, True, False),
    "Bbf": ItemData(78311, True, False),
    "Bobs Brain": ItemData(78312, True, False),
    "Best Bud": ItemData(78313, True, False),
    "Lil Brimstone": ItemData(78314, True, False),
    "Isaacs Heart": ItemData(78315, True, False),
    "Lil Haunt": ItemData(78316, True, False),
    "Dark Bum": ItemData(78317, True, False),
    "Big Fan": ItemData(78318, True, False),
    "Sissy Longlegs": ItemData(78319, True, False),
    "Punching Bag": ItemData(78320, True, False),
    "How To Jump": ItemData(78321, True, False),
    "D100": ItemData(78322, True, False),
    "D4": ItemData(78323, True, False),
    "D10": ItemData(78324, True, False),
    "Blank Card": ItemData(78325, True, False),
    "Book Of Secrets": ItemData(78326, True, False),
    "Box Of Spiders": ItemData(78327, True, False),
    "Red Candle": ItemData(78328, True, False),
    "The Jar": ItemData(78329, True, False),
    "Flush": ItemData(78330, True, False),
    "Satanic Bible": ItemData(78331, True, False),
    "Head Of Krampus": ItemData(78332, True, False),
    "Butter Bean": ItemData(78333, True, False),
    "Magic Fingers": ItemData(78334, True, False),
    "Converter": ItemData(78335, True, False),
    "Blue Box": ItemData(78336, True, False),
    "Unicorn Stump": ItemData(78337, True, False),
    "Taurus": ItemData(78338, True, False),
    "Aries": ItemData(78339, True, False),
    "Cancer": ItemData(78340, True, False),
    "Leo": ItemData(78341, True, False),
    "Virgo": ItemData(78342, True, False),
    "Libra": ItemData(78343, True, False),
    "Scorpio": ItemData(78344, True, False),
    "Sagittarius": ItemData(78345, True, False),
    "Capricorn": ItemData(78346, True, False),
    "Aquarius": ItemData(78347, True, False),
    "Pisces": ItemData(78348, True, False),
    "Eves Mascara": ItemData(78349, True, False),
    "Judas Shadow": ItemData(78350, True, False),
    "Maggys Bow": ItemData(78351, True, False),
    "Holy Mantle": ItemData(78352, True, False),
    "Thunder Thighs": ItemData(78353, True, False),
    "Strange Attractor": ItemData(78354, True, False),
    "Cursed Eye": ItemData(78355, True, False),
    "Mysterious Liquid": ItemData(78356, True, False),
    "Gemini": ItemData(78357, True, False),
    "Cains Other Eye": ItemData(78358, True, False),
    "Blue Babys Only Friend": ItemData(78359, True, False),
    "Samsons Chains": ItemData(78360, True, False),
    "Mongo Baby": ItemData(78361, True, False),
    "Isaacs Tears": ItemData(78362, True, False),
    "Undefined": ItemData(78363, True, False),
    "Scissors": ItemData(78364, True, False),
    "Breath Of Life": ItemData(78365, True, False),
    "Polaroid": ItemData(78366, True, False),
    "Negative": ItemData(78367, True, False),
    "Ludovico Technique": ItemData(78368, True, False),
    "Soy Milk": ItemData(78369, True, False),
    "Godhead": ItemData(78370, True, False),
    "Lazarus Rags": ItemData(78371, True, False),
    "Mind": ItemData(78372, True, False),
    "Body": ItemData(78373, True, False),
    "Soul": ItemData(78374, True, False),
    "Dead Onion": ItemData(78375, True, False),
    "Broken Watch": ItemData(78376, True, False),
    "Boomerang": ItemData(78377, True, False),
    "Safety Pin": ItemData(78378, True, False),
    "Caffeine Pill": ItemData(78379, True, False),
    "Torn Photo": ItemData(78380, True, False),
    "Blue Cap": ItemData(78381, True, False),
    "Latch Key": ItemData(78382, True, False),
    "Match Book": ItemData(78383, True, False),
    "Synthoil": ItemData(78384, True, False),
    "Snack": ItemData(78385, True, False),
    "Diplopia": ItemData(78386, True, False),
    "Placebo": ItemData(78387, True, False),
    "Wooden Nickel": ItemData(78388, True, False),
    "Toxic Shock": ItemData(78389, True, False),
    "Mega Bean": ItemData(78390, True, False),
    "Glass Cannon": ItemData(78391, True, False),
    "Bomber Boy": ItemData(78392, True, False),
    "Crack Jacks": ItemData(78393, True, False),
    "Moms Pearls": ItemData(78394, True, False),
    "Car Battery": ItemData(78395, True, False),
    "Box Of Friends": ItemData(78396, True, False),
    "The Wiz": ItemData(78397, True, False),
    "8 Inch Nails": ItemData(78398, True, False),
    "Incubus": ItemData(78399, True, False),
    "Fates Reward": ItemData(78400, True, False),
    "Lil Chest": ItemData(78401, True, False),
    "Sworn Protector": ItemData(78402, True, False),
    "Friend Zone": ItemData(78403, True, False),
    "Lost Fly": ItemData(78404, True, False),
    "Scatter Bombs": ItemData(78405, True, False),
    "Sticky Bombs": ItemData(78406, True, False),
    "Epiphora": ItemData(78407, True, False),
    "Continuum": ItemData(78408, True, False),
    "Mr Dolly": ItemData(78409, True, False),
    "Curse Of The Tower": ItemData(78410, True, False),
    "Charged Baby": ItemData(78411, True, False),
    "Dead Eye": ItemData(78412, True, False),
    "Holy Light": ItemData(78413, True, False),
    "Host Hat": ItemData(78414, True, False),
    "Restock": ItemData(78415, True, False),
    "Bursting Sack": ItemData(78416, True, False),
    "Number Two": ItemData(78417, True, False),
    "Pupula Duplex": ItemData(78418, True, False),
    "Pay To Play": ItemData(78419, True, False),
    "Edens Blessing": ItemData(78420, True, False),
    "Friend Ball": ItemData(78421, True, False),
    "Tear Detonator": ItemData(78422, True, False),
    "Lil Gurdy": ItemData(78423, True, False),
    "Bumbo": ItemData(78424, True, False),
    "D12": ItemData(78425, True, False),
    "Censer": ItemData(78426, True, False),
    "Key Bum": ItemData(78427, True, False),
    "Rune Bag": ItemData(78428, True, False),
    "Seraphim": ItemData(78429, True, False),
    "Betrayal": ItemData(78430, True, False),
    "Zodiac": ItemData(78431, True, False),
    "Serpents Kiss": ItemData(78432, True, False),
    "Marked": ItemData(78433, True, False),
    "Tech X": ItemData(78434, True, False),
    "Ventricle Razor": ItemData(78435, True, False),
    "Tractor Beam": ItemData(78436, True, False),
    "Gods Flesh": ItemData(78437, True, False),
    "Maw Of The Void": ItemData(78438, True, False),
    "Spear Of Destiny": ItemData(78439, True, False),
    "Explosivo": ItemData(78440, True, False),
    "Chaos": ItemData(78441, True, False),
    "Spider Mod": ItemData(78442, True, False),
    "Farting Baby": ItemData(78443, True, False),
    "Gb Bug": ItemData(78444, True, False),
    "D8": ItemData(78445, True, False),
    "Purity": ItemData(78446, True, False),
    "Athame": ItemData(78447, True, False),
    "Empty Vessel": ItemData(78448, True, False),
    "Evil Eye": ItemData(78449, True, False),
    "Lusty Blood": ItemData(78450, True, False),
    "Cambion Conception": ItemData(78451, True, False),
    "Immaculate Conception": ItemData(78452, True, False),
    "More Options": ItemData(78453, True, False),
    "Crown Of Light": ItemData(78454, True, False),
    "Deep Pockets": ItemData(78455, True, False),
    "Succubus": ItemData(78456, True, False),
    "Fruit Cake": ItemData(78457, True, False),
    "Teleport 2": ItemData(78458, True, False),
    "Black Powder": ItemData(78459, True, False),
    "Kidney Bean": ItemData(78460, True, False),
    "Glowing Hour Glass": ItemData(78461, True, False),
    "Circle Of Protection": ItemData(78462, True, False),
    "Sack Head": ItemData(78463, True, False),
    "Night Light": ItemData(78464, True, False),
    "Obsessed Fan": ItemData(78465, True, False),
    "Mine Crafter": ItemData(78466, True, False),
    "Pjs": ItemData(78467, True, False),
    "Head Of The Keeper": ItemData(78468, True, False),
    "Papa Fly": ItemData(78469, True, False),
    "Multidimensional Baby": ItemData(78470, True, False),
    "Glitter Bombs": ItemData(78471, True, False),
    "My Shadow": ItemData(78472, True, False),
    "Jar Of Flies": ItemData(78473, True, False),
    "Lil Loki": ItemData(78474, True, False),
    "Milk": ItemData(78475, True, False),
    "D7": ItemData(78476, True, False),
    "Binky": ItemData(78477, True, False),
    "Moms Box": ItemData(78478, True, False),
    "Kidney Stone": ItemData(78479, True, False),
    "Mega Blast": ItemData(78480, True, False),
    "Dark Princes Crown": ItemData(78481, True, False),
    "Apple": ItemData(78482, True, False),
    "Lead Pencil": ItemData(78483, True, False),
    "Dog Tooth": ItemData(78484, True, False),
    "Dead Tooth": ItemData(78485, True, False),
    "Linger Bean": ItemData(78486, True, False),
    "Shard Of Glass": ItemData(78487, True, False),
    "Metal Plate": ItemData(78488, True, False),
    "Eye Of Greed": ItemData(78489, True, False),
    "Tarot Cloth": ItemData(78490, True, False),
    "Varicose Veins": ItemData(78491, True, False),
    "Compound Fracture": ItemData(78492, True, False),
    "Polydactyly": ItemData(78493, True, False),
    "Dads Lost Coin": ItemData(78494, True, False),
    "Midnight Snack": ItemData(78495, True, False),
    "Cone Head": ItemData(78496, True, False),
    "Belly Button": ItemData(78497, True, False),
    "Sinus Infection": ItemData(78498, True, False),
    "Glaucoma": ItemData(78499, True, False),
    "Parasitoid": ItemData(78500, True, False),
    "Eye Of Belial": ItemData(78501, True, False),
    "Sulfuric Acid": ItemData(78502, True, False),
    "Glyph Of Balance": ItemData(78503, True, False),
    "Analog Stick": ItemData(78504, True, False),
    "Contagion": ItemData(78505, True, False),
    "Finger": ItemData(78506, True, False),
    "Shade": ItemData(78507, True, False),
    "Depression": ItemData(78508, True, False),
    "Hushy": ItemData(78509, True, False),
    "Lil Monstro": ItemData(78510, True, False),
    "King Baby": ItemData(78511, True, False),
    "Big Chubby": ItemData(78512, True, False),
    "Broken Glass Cannon": ItemData(78513, True, False),
    "Plan C": ItemData(78514, True, False),
    "D1": ItemData(78515, True, False),
    "Void": ItemData(78516, True, False),
    "Pause": ItemData(78517, True, False),
    "Smelter": ItemData(78518, True, False),
    "Compost": ItemData(78519, True, False),
    "Dataminer": ItemData(78520, True, False),
    "Clicker": ItemData(78521, True, False),
    "Mama Mega": ItemData(78522, True, False),
    "Wait What": ItemData(78523, True, False),
    "Crooked Penny": ItemData(78524, True, False),
    "Dull Razor": ItemData(78525, True, False),
    "Potato Peeler": ItemData(78526, True, False),
    "Metronome": ItemData(78527, True, False),
    "D Infinity": ItemData(78528, True, False),
    "Edens Soul": ItemData(78529, True, False),
    "Acid Baby": ItemData(78530, True, False),
    "Yo Listen": ItemData(78531, True, False),
    "Adrenaline": ItemData(78532, True, False),
    "Jacobs Ladder": ItemData(78533, True, False),
    "Ghost Pepper": ItemData(78534, True, False),
    "Euthanasia": ItemData(78535, True, False),
    "Camo Undies": ItemData(78536, True, False),
    "Duality": ItemData(78537, True, False),
    "Eucharist": ItemData(78538, True, False),
    "Sack Of Sacks": ItemData(78539, True, False),
    "Greeds Gullet": ItemData(78540, True, False),
    "Large Zit": ItemData(78541, True, False),
    "Little Horn": ItemData(78542, True, False),
    "Brown Nugget": ItemData(78543, True, False),
    "Poke Go": ItemData(78544, True, False),
    "Backstabber": ItemData(78545, True, False),
    "Sharp Straw": ItemData(78546, True, False),
    "Moms Razor": ItemData(78547, True, False),
    "Bloodshot Eye": ItemData(78548, True, False),
    "Delirious": ItemData(78549, True, False),
    "Angry Fly": ItemData(78550, True, False),
    "Black Hole": ItemData(78551, True, False),
    "Bozo": ItemData(78552, True, False),
    "Broken Modem": ItemData(78553, True, False),
    "Mystery Gift": ItemData(78554, True, False),
    "Sprinkler": ItemData(78555, True, False),
    "Fast Bombs": ItemData(78556, True, False),
    "Buddy In A Box": ItemData(78557, True, False),
    "Lil Delirium": ItemData(78558, True, False),
    "Jumper Cables": ItemData(78559, True, False),
    "Coupon": ItemData(78560, True, False),
    "Telekinesis": ItemData(78561, True, False),
    "Moving Box": ItemData(78562, True, False),
    "Technology Zero": ItemData(78563, True, False),
    "Leprosy": ItemData(78564, True, False),
    "7 Seals": ItemData(78565, True, False),
    "Mr Me": ItemData(78566, True, False),
    "Angelic Prism": ItemData(78567, True, False),
    "Pop": ItemData(78568, True, False),
    "Deaths List": ItemData(78569, True, False),
    "Haemolacria": ItemData(78570, True, False),
    "Lachryphagy": ItemData(78571, True, False),
    "Trisagion": ItemData(78572, True, False),
    "Schoolbag": ItemData(78573, True, False),
    "Blanket": ItemData(78574, True, False),
    "Sacrificial Altar": ItemData(78575, True, False),
    "Lil Spewer": ItemData(78576, True, False),
    "Marbles": ItemData(78577, True, False),
    "Mystery Egg": ItemData(78578, True, False),
    "Flat Stone": ItemData(78579, True, False),
    "Marrow": ItemData(78580, True, False),
    "Slipped Rib": ItemData(78581, True, False),
    "Hallowed Ground": ItemData(78582, True, False),
    "Pointy Rib": ItemData(78583, True, False),
    "Book Of The Dead": ItemData(78584, True, False),
    "Dads Ring": ItemData(78585, True, False),
    "Divorce Papers": ItemData(78586, True, False),
    "Jaw Bone": ItemData(78587, True, False),
    "Brittle Bones": ItemData(78588, True, False),
    "Broken Shovel 1": ItemData(78589, True, False),
    "Broken Shovel 2": ItemData(78590, True, False),
    "Moms Shovel": ItemData(78591, True, False),
    "Mucormycosis": ItemData(78592, True, False),
    "2spooky": ItemData(78593, True, False),
    "Golden Razor": ItemData(78594, True, False),
    "Sulfur": ItemData(78595, True, False),
    "Fortune Cookie": ItemData(78596, True, False),
    "Eye Sore": ItemData(78597, True, False),
    "120 Volt": ItemData(78598, True, False),
    "It Hurts": ItemData(78599, True, False),
    "Almond Milk": ItemData(78600, True, False),
    "Rock Bottom": ItemData(78601, True, False),
    "Nancy Bombs": ItemData(78602, True, False),
    "Bar Of Soap": ItemData(78603, True, False),
    "Blood Puppy": ItemData(78604, True, False),
    "Dream Catcher": ItemData(78605, True, False),
    "Paschal Candle": ItemData(78606, True, False),
    "Divine Intervention": ItemData(78607, True, False),
    "Blood Oath": ItemData(78608, True, False),
    "Playdough Cookie": ItemData(78609, True, False),
    "Socks": ItemData(78610, True, False),
    "Eye Of The Occult": ItemData(78611, True, False),
    "Immaculate Heart": ItemData(78612, True, False),
    "Monstrance": ItemData(78613, True, False),
    "Intruder": ItemData(78614, True, False),
    "Dirty Mind": ItemData(78615, True, False),
    "Damocles": ItemData(78616, True, False),
    "Free Lemonade": ItemData(78617, True, False),
    "Spirit Sword": ItemData(78618, True, False),
    "Red Key": ItemData(78619, True, False),
    "Psy Fly": ItemData(78620, True, False),
    "Wavy Cap": ItemData(78621, True, False),
    "Rocket In A Jar": ItemData(78622, True, False),
    "Book Of Virtues": ItemData(78623, True, False),
    "Alabaster Box": ItemData(78624, True, False),
    "Stairway": ItemData(78625, True, False),
    "Sol": ItemData(78627, True, False),
    "Luna": ItemData(78628, True, False),
    "Mercurius": ItemData(78629, True, False),
    "Venus": ItemData(78630, True, False),
    "Terra": ItemData(78631, True, False),
    "Mars": ItemData(78632, True, False),
    "Jupiter": ItemData(78633, True, False),
    "Saturnus": ItemData(78634, True, False),
    "Uranus": ItemData(78635, True, False),
    "Neptunus": ItemData(78636, True, False),
    "Pluto": ItemData(78637, True, False),
    "Voodoo Head": ItemData(78638, True, False),
    "Eye Drops": ItemData(78639, True, False),
    "Act Of Contrition": ItemData(78640, True, False),
    "Member Card": ItemData(78641, True, False),
    "Battery Pack": ItemData(78642, True, False),
    "Moms Bracelet": ItemData(78643, True, False),
    "Scooper": ItemData(78644, True, False),
    "Ocular Rift": ItemData(78645, True, False),
    "Boiled Baby": ItemData(78646, True, False),
    "Freezer Baby": ItemData(78647, True, False),
    "Eternal D6": ItemData(78648, True, False),
    "Bird Cage": ItemData(78649, True, False),
    "Larynx": ItemData(78650, True, False),
    "Lost Soul": ItemData(78651, True, False),
    "Blood Bombs": ItemData(78653, True, False),
    "Lil Dumpy": ItemData(78654, True, False),
    "Birds Eye": ItemData(78655, True, False),
    "Lodestone": ItemData(78656, True, False),
    "Rotten Tomato": ItemData(78657, True, False),
    "Birthright": ItemData(78658, True, False),
    "Red Stew": ItemData(78660, True, False),
    "Genesis": ItemData(78661, True, False),
    "Sharp Key": ItemData(78662, True, False),
    "Booster Pack": ItemData(78663, True, False),
    "Mega Mush": ItemData(78664, True, False),
    "Knife Piece 1": ItemData(78665, True, False),
    "Knife Piece 2": ItemData(78666, True, False),
    "Death Certificate": ItemData(78667, True, False),
    "Bot Fly": ItemData(78668, True, False),
    "Meat Cleaver": ItemData(78670, True, False),
    "Evil Charm": ItemData(78671, True, False),
    "Dogma": ItemData(78672, True, False),
    "Purgatory": ItemData(78673, True, False),
    "Stitches": ItemData(78674, True, False),
    "R Key": ItemData(78675, True, False),
    "Knockout Drops": ItemData(78676, True, False),
    "Eraser": ItemData(78677, True, False),
    "Yuck Heart": ItemData(78678, True, False),
    "Urn Of Souls": ItemData(78679, True, False),
    "Akeldama": ItemData(78680, True, False),
    "Magic Skin": ItemData(78681, True, False),
    "Revelation": ItemData(78682, True, False),
    "Consolation Prize": ItemData(78683, True, False),
    "Tinytoma": ItemData(78684, True, False),
    "Brimstone Bombs": ItemData(78685, True, False),
    "4 5 Volt": ItemData(78686, True, False),
    "Fruity Plum": ItemData(78688, True, False),
    "Plum Flute": ItemData(78689, True, False),
    "Star Of Bethlehem": ItemData(78690, True, False),
    "Cube Baby": ItemData(78691, True, False),
    "Vade Retro": ItemData(78692, True, False),
    "False Phd": ItemData(78693, True, False),
    "Spin To Win": ItemData(78694, True, False),
    "Damocles Passive": ItemData(78695, True, False),
    "Vasculitis": ItemData(78696, True, False),
    "Giant Cell": ItemData(78697, True, False),
    "Tropicamide": ItemData(78698, True, False),
    "Card Reading": ItemData(78699, True, False),
    "Quints": ItemData(78700, True, False),
    "Tooth And Nail": ItemData(78702, True, False),
    "Binge Eater": ItemData(78703, True, False),
    "Guppys Eye": ItemData(78704, True, False),
    "Straw Man": ItemData(78706, True, False),
    "Dads Note": ItemData(78707, True, False),
    "Sausage": ItemData(78708, True, False),
    "Options": ItemData(78709, True, False),
    "Candy Heart": ItemData(78710, True, False),
    "Pound Of Flesh": ItemData(78711, True, False),
    "Redemption": ItemData(78712, True, False),
    "Spirit Shackles": ItemData(78713, True, False),
    "Cracked Orb": ItemData(78714, True, False),
    "Empty Heart": ItemData(78715, True, False),
    "Astral Projection": ItemData(78716, True, False),
    "C Section": ItemData(78717, True, False),
    "Lil Abaddon": ItemData(78718, True, False),
    "Montezumas Revenge": ItemData(78719, True, False),
    "Lil Portal": ItemData(78720, True, False),
    "Worm Friend": ItemData(78721, True, False),
    "Bone Spurs": ItemData(78722, True, False),
    "Hungry Soul": ItemData(78723, True, False),
    "Jar Of Wisps": ItemData(78724, True, False),
    "Soul Locket": ItemData(78725, True, False),
    "Friend Finder": ItemData(78726, True, False),
    "Inner Child": ItemData(78727, True, False),
    "Glitched Crown": ItemData(78728, True, False),
    "Jelly Belly": ItemData(78729, True, False),
    "Sacred Orb": ItemData(78730, True, False),
    "Sanguine Bond": ItemData(78731, True, False),
    "Swarm": ItemData(78732, True, False),
    "Heartbreak": ItemData(78733, True, False),
    "Bloody Gust": ItemData(78734, True, False),
    "Salvation": ItemData(78735, True, False),
    "Vanishing Twin": ItemData(78736, True, False),
    "Twisted Pair": ItemData(78737, True, False),
    "Azazels Rage": ItemData(78738, True, False),
    "Echo Chamber": ItemData(78739, True, False),
    "Isaacs Tomb": ItemData(78740, True, False),
    "Vengeful Spirit": ItemData(78741, True, False),
    "Esau Jr": ItemData(78742, True, False),
    "Berserk": ItemData(78743, True, False),
    "Dark Arts": ItemData(78744, True, False),
    "Abyss": ItemData(78745, True, False),
    "Supper": ItemData(78746, True, False),
    "Stapler": ItemData(78747, True, False),
    "Suplex": ItemData(78748, True, False),
    "Bag Of Crafting": ItemData(78749, True, False),
    "Flip": ItemData(78750, True, False),
    "Lemegeton": ItemData(78751, True, False),
    "Sumptorium": ItemData(78752, True, False),
    "Recall": ItemData(78753, True, False),
    "Hold": ItemData(78754, True, False),
    "Keepers Sack": ItemData(78755, True, False),
    "Keepers Kin": ItemData(78756, True, False),
    "Keepers Box": ItemData(78758, True, False),
    "Everything Jar": ItemData(78759, True, False),
    "Tmtrainer": ItemData(78760, True, False),
    "Anima Sola": ItemData(78761, True, False),
    "Spindown Dice": ItemData(78762, True, False),
    "Hypercoagulation": ItemData(78763, True, False),
    "Ibs": ItemData(78764, True, False),
    "Hemoptysis": ItemData(78765, True, False),
    "Ghost Bombs": ItemData(78766, True, False),
    "Gello": ItemData(78767, True, False),
    "Decap Attack": ItemData(78768, True, False),
    "Glass Eye": ItemData(78769, True, False),
    "Stye": ItemData(78770, True, False),
    "Moms Ring": ItemData(78771, True, False),
    **trap_items,
    # other
    "Victory": ItemData(None, True, False),
}

default_trap_items_weights = {
    "Troll Bomb Trap": 20,
    "Teleport Trap": 20,
    "Retro Vision Trap": 20,
    "Curse Trap": 20,
}

default_junk_items_weights = {
    "Random Pickup": 0,
    "Random Heart": 5,
    "Random Coin": 6,
    "Random Bomb": 5,
    "Random Key": 5,
    "Random Card": 3,
    "Random Pill": 3,
    "Random Chest": 2,
    "Random Trinket": 1,
}

default_weights = {
    # item (major)
    "Treasure Room Item": 10,
    "Shop Item": 10,
    "Boss Item": 8,
    "Devil Deal Item": 5,
    "Angle Deal Item": 5,
    "Secret Room Item": 6,
    "Library Item": 4,
    "Curse Room Item": 4,
    "Planetarium Item": 1,
    # item (experimental)
    "Shell Game Item": 0,
    "Golden Chest Item": 6,
    "Red Chest Item": 6,
    "Beggar Item": 0,
    "Demon Baggar Item": 0,
    "Key Master Item": 0,
    "Battery Bum Item": 0,
    "Mom's Chest Item": 0,
    "Greed Treasure Room Item": 0,
    "Greed Boss Item": 0,
    "Greed Shop Item": 0,
    "Greed Devil Deal Item": 0,
    "Greed Angel Deal Item": 0,
    "Greed Curse Room Item": 0,
    "Greed Secret Room Item": 0,
    "Crane Game Item": 0,
    "Ultra Secret Room Item": 0,
    "Bomb Bum Item": 0,
    "Old Chest Item": 0,
    "Baby Shop Item": 0,
    "Wooden Chest Item": 0,
    "Rotten Beggar Item": 0,
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: name for name, data in item_table.items() if data.id}
