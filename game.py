#===========================================
# Room adventure game by python-voldemort
#==================Modules==================

import os
import random
import time 
from battle import battle


#===================================================
#==================in-game classes==================
#===================================================


# Main location class
class Room():
    # Constructor
    def __init__(self):
        self.name = ""
        self.connections = []
        self.items = []
        self.features = []
        self.description = ""
        self.opponents = []
        self.pic = ""
    # Getters 
    def __str__(self):
        if self.pic != None:
            print("=" * 150)
            draw_picture(self.pic, speed=print_speed) # draws an ASCII-Art picture of a room from a file
            print("=" * 150)
        slow_print(self.description, print_speed)
        return ""
    # Setters
    def form_the_room(self, connections, items, description, opponents = [], features = [], pic = None, name = ""):
        self.connections = connections
        self.items = items 
        self.description = description
        self.opponents = opponents
        self.features = features
        self.pic = pic
        self.name = name
    # Ultimate setter, allows to change any characteristic of the room
    def reform_the_room(self, connections = None, items = None, description = None, opponents = None, features = [], pic = None, name = None):
        if connections == None:
            None
        else:
            self.connections = connections
        if items == None:
            None
        else:
            self.items = items
        if description == None:
            None
        else:
            self.description = description
        if opponents == None:
            None
        else:
            self.opponents = opponents
        if features == None:
            None
        else:
            self.features = features
        if pic == None:
            None
        else:
            self.pic = pic
        if name == None:
            None
        else:
            self.name = name

# Player Class
class Player():
    #Constructors:
    def __init__(self):
        self.name = "Unknown"
        self.classType = "Reporter"
        self.HP = 100
        self.mental_health = 100
        self.strength = 10
        self.defence = 0.05
        self.stealth = 0.25
        self.items = []
    #Getters
    # genetal getter, getting all the needed info
    def get_info(self):
        return (self.name, self.classType, self.HP, self.mental_health, self.strength, self.defence)
    def get_MH(self):
        return self.mental_health
    def __str__(self): 
        if self.classType == "DoomSlayer":
            draw_picture("visual assistance/doom.txt", alighnment = "center", speed=print_speed)
            return "\n\nThe only entity in the universe born human that makes Daemons get scared for their own life,\nThe One and Only: {}".format(self.name)
        else: #30
            return "\n  ==============================  \n||Player card                   ||\n||Name: {}".format(self.name) + " " * (24 - len(self.name)) + "||\n||Strength: {}, Defence: {:.1f}    ||\n||HP: {}, MH: {:.0f}              ||\n||Stealth: {:.2f}                 ||\n||==============================||".format(self.strength, self.defence,round(self.HP),self.mental_health, self.stealth)
    # Returns platers health and mental health in text form
    def status(self):
        if self.mental_health >= 100:
            mh = "sharp and undisturbed"
        elif self.mental_health >= 85:
            mh = "worried"
        elif self.mental_health >= 75:
            mh = "anxiety"
        elif self.mental_health >= 50:
            mh = "disturbed and surrealistic"
        elif self.mental_health >= 30:
            mh = "delusional and hallucinating"
        elif self.mental_health >= 10:
            mh = "ò̶͔̀ņ̵͚̇ ̴͔̙̏t̵̲̞͒̆h̶͕͕̆͌è̸̡͌ ̸͎̮͛v̶̳̰͂͌e̵̢͆͘r̶̖͖̂̏g̵̡̮̔̿e̵̡̼̅͋ ̷͓͂͝"
        else:
            mh = "ŗ̷̡̝̦͖̠̱̲̐̃͋̀͛́̏ë̷̢̛͖̲̺͙̟̖̮̦̝́͜w̶͇̞̅̔͗̾̌̋̇́ͅa̴̧̡̛͖̘̠̋̓̅̉͠r̶̡̧̫͉̣͙̩̘̭̦͋d̸̨̧̺̗̭̖͋ę̶͈̪͔͇̻̫̰̬̫̒̆̏̓̑͋̄͜͜d̶̢̮͉̙̜̼̼̖̣́̆̒͆̄͗͊̒̂͝͠ ̴̛͕̯͕̜̈́́͌͌̆̈́͛̒͝ŵ̶̡̛̛̝͔̦̠̭̺̫̪̳̱̃͆͐͋̐́̈i̵̧͆̂̄̑̿̎̿́̍͂̍͐͝ṫ̶̢̝̱͎̤̻̦̠̞̟͝h̵̦̰̒̽͋̎̉̿͂͆ ̷̧̟̬̯̝̠͇̟̖̑͂̽͂̏̔͗͜͜͝h̵͖͈͙̣̭̐̇͂͑̓̈̇̍̅͌̊ơ̷̧̹̱͓̗̪͍̥̝̹̫̻̅̽̔̂̍͊̊̏̏̒͘͘͜͜l̶̡̖̮̮͈̻̻͉̱͓̳̠̙͑̄͑̀͜l̶̡̻͎̟͈̼͍̝̬͋̐͒̉͊̔͒̀̕͝y̷̨͙̣͙̣̯̲̹͎̗͓͔͠͠ ̸̧̧̹̻͉͌ͅķ̶̯͙͇̫̣̗̩͕̦̟̽̇̚n̵̡̡̬̭͕̞̬͚̦͍̗̤̟̑̃̈̎͊̃̌̏̅͠ǫ̴͙̆̐͆͊͊͆̈͐̋́͂͘͠͝w̶̢̫̥̭̤̅͂̆̀̂͝͠͝ĺ̵̤̻̫̼̙̯̫̑͆͗͂̾e̶̢̹̠̫̜̹̟̙͒̍̄ͅd̸̺͍̺̝̘̯̞͔̓̈́̅͋̒͜͝ͅģ̷̛̘̳̪̙̹̔̈́͋̈́͋̌̇̐̐̍̋͒̐̎e̸͓̹̣̬̗̹͑̐́̉̊͒̊̽̈́̂́̽̋̈́"

        if self.HP >= 100:
            hp = "feeling good"
        elif self.HP >= 85:
            hp = "scratched and slightly bruised"
        elif self.HP >= 75:
            hp = "a bit banged up"
        elif self.HP >= 50:
            hp = "hurt and bruised"
        elif self.HP >= 30:
            hp = "in rough shape"
        elif self.HP >= 10:
            hp = "afflicted with many injuries"
        else:
            hp = "on the verge of death"


        return "Your are {}\nYour feel {}\nYou are carrying {}".format(hp, mh, self.items)
    #Setters:
    def define_character(self, name = "Unnamed Wonderer", classType = "Reporter"): # constructs character based on preset builds
        self.name = name
        if classType == "Reporter":
            self.classType = "Reporter"
            self.HP = 100
            self.mental_health = 100
            self.strength = 10
            self.defence = 0.05
            self.stealth = 0.25
            self.items = []
        elif classType == "Boxer":
            self.classType = "Boxer"
            self.HP = 100
            self.mental_health = 100
            self.strength = 20
            self.defence = 0.30
            self.stealth = 0.25
            self.items = []
        elif classType == "Yog":
            self.classType = "Yog"
            self.HP = 130
            self.mental_health = 150
            self.strength = 10
            self.defence = 0.05
            self.stealth = 0.25
            self.items = []
        elif classType == "Thief":
            self.classType = "Thief"
            self.HP = 100
            self.mental_health = 100
            self.strength = 10
            self.defence = 0.20
            self.stealth = 0.7
            self.items = []
        elif classType == "DoomSlayer":
            self.classType = "DoomSlayer"
            self.name = "Doom Guy"
            self.HP = 1500
            self.mental_health = 10**10
            self.strength = 150
            self.defence = 0.999
            self.stealth = 0
            self.weapon = "shotgun"
            self.items = ["The second Crucible", "Praetor Suit", "Super Shotgun"]
    def append_inventory(self, items):
        for item in items:
            self.items.append(item)
    #Battle Related:
    def calculateDefence(self, enem_att):
        self.HP = self.HP - (enem_att - enem_att * self.defence)
    def calculateAttack(self):
        return random.randint(1, self.strength)
    def isStillAlive(self):
        if self.HP > 0:
            return True 
        else:
            return False 
    # DoomGuy specific
    def choose_weapon(self):
        weapon_choice = input("Do you want to use the (s)hotgun or (C)rucible? ").lower()
        if weapon_choice == "c":
            self.weapon = "The second Crucible"
        else:
            self.weapon = "Super Shotgun"
    def finish_him(self):
        finish_moves = ["Rip and tear through the very fabric of hell!","Unleash the fiery wrath of the Crucible upon your foe!","Invoke the infernal might of the Slayer to obliterate your enemy!","With relentless fury, crush the demonic opposition!","Eviscerate with the unstoppable force of hellfire!","Channel the essence of doom, shattering all who oppose!","Let the echoes of hell herald the demise of your adversary!","Unleash a torrent of destruction, reducing all to ashes!","Wield the Crucible's power, leaving nothing but desolation!","Annihilate with the fervor of a thousand damned souls!","Summon the relentless power of the Slayer to bring damnation!","Crush your foe beneath the weight of unstoppable vengeance!","Engulf your enemy in the flames of hell's fury!","Decimate with the indomitable force of the Slayer's might!","Slay with the precision and brutality of a celestial reaper!"]
        print(random.choice(finish_moves))

# Possible opponent class
class Monster(): 
    #Constructors:
    def __init__(self):
        self.name = "Unnamed Creature"
        self.classType = "Sea One"
        self.HP = 125
        self.strength = 15
        self.defence = 0.03

    #Getters:
    #genetal getter, getting all the needed info
    def get_info(self):
        return (self.name, self.classType, self.HP, self.strength, self.defence)
    def __str__(self): 
        if self.classType == "Deep One":
            names_do = ["You witness a startling vision—a Deep One with alien, luminescent eyes and sleek, scaled skin. It invokes a mixture of fascination \nand unease as you grapple with the unknown", "You are met with the sight of an enigmatic being—a Deep One with webbed extremities and ethereal bioluminescence. Awe and wonder \nfill you as you contemplate the mysteries lurking in the deep", "The first glimpse reveals a creature of eerie beauty with fish-like features that captivate and unsettle you", "A nightmarish apparition manifests before you with elongated limbs and mysterious eyes. A primal fear challenges \nyour understanding of the natural world.", "A surreal sight unfolds as you encounter a Deep One with tentacle-like extensions, blurring the lines between human and cephalopod \nin a disorienting dance of shapes.", "You witness an amphibious marvel—a Deep One with partial webbing and a strange, otherworldly aura. It challenges preconceived \nnotions of what belongs to the land and what belongs to the sea.", "A vision of the Deep One appears as an illusion from the abyss, its natural armor gleaming with an iridescent glow. A surreal and almost \ndreamlike encounter leaves you questioning reality.", "Your initial glimpse captures a mesmerizing figure, shrouded in iridescent scales that play tricks on your eyes. You question the reality \nof the encounter and the sanity of your perception."]
            return names_do[random.randint(0, len(names_do) - 1)]
        elif self.classType == "Young Hybrid":
            names_yh = ["You notice a youth with subtly irregular facial features—slightly elongated limbs, a peculiar symmetry that hints at an otherworldly \nheritage, and a gaze that seems to linger a moment too long", "You come across an adolescent with an unsettling beauty, their skin appearing almost translucent, revealing an odd luminescence beneath \nthe surface, giving them an ethereal quality that stands out in human crowds.", "You observe a teenager with a curiously symmetrical appearance, as if nature itself couldn't decide on a uniform pattern, resulting in \nan unsettling blend of beauty and peculiarity that draws attention.", "You encounter a young person whose proportions seem slightly askew, with limbs that appear just a touch too long or a torso that hints \nat an unconventional skeletal structure, creating an uneasy sense of strangeness.", "You come across an adolescent whose movements, while graceful, seem slightly off-kilter, as if their body follows an unearthly rhythm \nthat defies the norms of human locomotion.", "You meet a youth with eyes that convey a mysterious depth, holding a gaze that evokes an uncanny knowingness, subtly hinting at a connection \nto realms beyond the understanding of ordinary onlookers.", "You notice an individual displaying subtle deformities—perhaps fingers that taper slightly too much or an oddly formed jawline—subverting \nexpectations of conventional human anatomy in a way that challenges normalcy.", "You come across a teenager with an almost unnatural pallor to their skin, a shade that suggests an absence of sunlight or a pigment that \ntranscends typical human hues, giving them an otherworldly appearance.", "You encounter a young person who seems to exist on the fringes of the human spectrum, their overall countenance reflecting an otherworldly \nallure that hints at a connection to the mysterious depths.", "You notice an individual with features that defy easy categorization, such as subtly webbed digits or an oddly shaped ear, creating an \nunsettling yet intriguing appearance that sets them apart from their peers."]
            return names_yh[random.randint(0, len(names_yh) - 1)]
        elif self.classType == "Transitioning Hybrid":
            names_th = ["Before you is an individual with an uncanny synthesis of aquatic and human features—a seamless blend that hints at a mysterious connection \nto the depths of the ocean." , "You encounter a being that defies conventional categorization, displaying an eerie yet captivating fusion of scales, webbed appendages, \nand an enigmatic aura that transcends the boundaries of the ordinary.", "An individual stands before you, their appearance a testament to a profound integration of oceanic elements and human form, creating an \nunsettling yet intriguing harmony.", "Before your eyes is a harmonized anomaly—a hybrid with an otherworldly elegance that belies the oddity of their aquatic features seamlessly \ncoalescing with human traits.", "You notice a person whose subtle aquatic allure is evident in their refined features—scaled skin, webbed attributes, and an overall \naesthetic that reflects an unexpected harmony between two distinct worlds.", "Before you stands an enigma, a being in its final stage of merging aquatic and human characteristics, creating an appearance that is both \nenigmatic and strangely alluring.", "Witness an individual whose existence seems infused with the essence of the ocean—features subtly altered to reflect a deep-sea connection, \na captivating anomaly in the human landscape.", "You come across an individual whose hybridity is seamless, with aquatic and human traits blending effortlessly, presenting an appearance \nthat challenges conventional notions of beauty.", "Before your eyes is a presence inspired by the depths of the ocean—an individual with a fully realized fusion of aquatic elements, their \nunique appearance resonating with a profound connection to the sea.", "Encounter a being exuding an oceanic elegance—features adapted to an aquatic existence while retaining a semblance of human grace, creating \na captivating and subtly disconcerting aesthetic."]
            return names_th[random.randint(0, len(names_th) - 1)]
        elif self.classType == "Sea Shogoth":
            names_ss = ["Before your eyes emerges a cacophony of forms—a sea shoggoth with a bewildering array of shapes and textures, an entity that challenges \nthe very notion of solidity and coherence.", "Encounter a being embodying primordial chaos—a sea shoggoth with no discernible structure, its form a writhing mass of tentacles, appendages, \nand swirling depths that plunge into the unknown.", "You behold a maelstrom of shapes—an ever-swirling sea shoggoth with tendrils extending in all directions, each movement a cosmic dance that \ntranscends the boundaries of earthly comprehension.", "Before you is a manifestation of the shifting abyss—a sea shoggoth that pulsates with eldritch energy, its form a nightmarish dance of \nliquefied horrors and extraterrestrial geometry.", "You behold a creature of eldritch fluidity—an embodiment of chaos with amorphous tendrils, pseudopods, and a formlessness that challenges \bthe sanity of those who gaze upon it"]
            return names_ss[random.randint(0, len(names_ss) - 1)]
        else:
            return "Before you stands a very old, but sturdy looking old man"           
    #Setters:
    def define_monster(self, classType, name = ""): # constructs monster based on preset builds
        if name == "":
            name = classType
        if classType == "Deep One":
            self.classType = classType
            self.name = name
            self.HP = 175
            self.strength = 20
            self.defence = 0.3
        elif classType == "Old Man":
            self.classType = classType
            self.name = "Raymond Bailey"
            self.HP = 60
            self.strength = 18
            self.defence = 0.05
        elif classType == "Young Hybrid":
            self.classType = classType
            self.name = name
            self.HP = 40
            self.strength = 8
            self.defence = 0.05
        elif classType == "Transitioning Hybrid":
            self.classType = classType
            self.name = name
            self.HP = 120
            self.strength = 14
            self.defence = 0.15 
        elif classType == "Sea Shogoth":
            self.classType = classType
            self.name = name
            self.HP = 400
            self.strength = 300
            self.defence = 0.4               
    #Battle Related:
    def calculateDefence(self, enem_att):
        self.HP = self.HP - (enem_att - enem_att * self.defence)
    def calculateAttack(self):
        return random.randint(1, self.strength)
    def isStillAlive(self):
        if self.HP > 0:
            return True 
        else:
            return False 
    def revive(self):
        self.define_monster(self.classType)

# Item affecting characteristics class   
class Item():
    def __init__(self):
        self.name = ""
        self.description_loc = ""
        self.attributes = {}
    def __str__(self):
        return self.name
    def describe(self):
        return print_all(self.description_loc)
    def give_attributes(self):
        return self.attributes
    def form_the_item(self, name, description_loc, attributes):
        self.name= name 
        self.description_loc = description_loc
        self.attributes = attributes

    
#===================================================
#==================Game initiation==================
#===================================================

# ====Form all flags====
# Nessecary for events not to repeat
em_bt_seen = False #empty boat interaction
conc_init_talk = False # initial conversation with concierge
fountain_scratch = False # Fountain interaction
window_horror_rivst_day = False # river street horror in the window interaction
op_save_private_bread_fl = False # river street gate interaction that allows player to get some bread
devils_reef_close = False # water street devils reef interaction decreasing mental health
raymond_talk = False # initial conversation with old man in Docks
raymond_ext_talk = False # continuation of conversation with old man in Docks that results in him passing out either from alcohol or player's fists
knowledge_concierge = False # Important flag given if old man is bribed with moonshine that allows to later steal backroom key from concierge
evening = False # act two
room_fight = False # so the killer deep one won't spawn infinetly inside 310B
da_end = False # achiving victory
secret = False # secret ending unlocked

# ====Form all initial items====
w_items = {} 
golden_ingot = Item()
golden_ingot.form_the_item("golden_ingot", "in_game_text/item_descriptions/golden_ingot.txt", {"MH" : -10})
w_items["golden_ingot"] = golden_ingot
bread = Item()
bread.form_the_item("bread", "in_game_text/item_descriptions/bread.txt", {})
w_items["bread"] = bread 
moonshine_bottle = Item()
moonshine_bottle.form_the_item("moonshine_bottle", "in_game_text/item_descriptions/moonshine_bottle.txt", {})
w_items["moonshine_bottle"] = moonshine_bottle

# ====Form all standard locations====

rooms = {}

r_dock = Room()
r_hotel_loby = Room()
r_central_plaza = Room()
r_river_street = Room()
r_water_street = Room()
r_rail = Room()
r_310b = Room()
r_311b = Room()
r_backroom = Room()

r_dock.form_the_room(["water_street"], ["golden_ingot"], "in_game_text/dock_day.txt", features=["empty_boat", "old_man"], pic="visual assistance/dock.txt", name="Dock")
rooms["docks"] = r_dock
r_hotel_loby.form_the_room(["central_plaza"], [], "in_game_text/hotel_loby_day.txt", features=["concierge", "carpet", "strange_portret"],  pic="visual assistance/hotel_loby.txt", name="Gilman Hotel")
rooms["hotel_loby"] = r_hotel_loby
r_central_plaza.form_the_room(["hotel_loby", "river_street"], [], "in_game_text/central_plaza_day.txt", features=["locals", "dormant_fountain", "pigeons"], pic="visual assistance/central_plaza.txt", name="Central Plaza")
rooms["central_plaza"] = r_central_plaza
r_river_street.form_the_room(["central_plaza", "water_street", "rail"], [], "in_game_text/river_street_day.txt", features=["window", "gate"], pic= "visual assistance/river_street.txt", name="River Street")
rooms["river_street"] = r_river_street
r_water_street.form_the_room(["river_street", "docks"], [], "in_game_text/water_street_day.txt", features=["devils_reef"], pic="visual assistance/water_street.txt", name="Water Street")
rooms["water_street"] = r_water_street
r_rail.form_the_room(["river_street"], ["moonshine_bottle"], "in_game_text/rail_day.txt",features=["arkcham", "abandoned_wagon"], pic="visual assistance/rail.txt", name="Rail")
rooms["rail"] = r_rail
r_310b.form_the_room([], [], "in_game_text/night/rooms/310B.txt", features=["bed", "desk", 'door'], pic= "visual assistance/310B.txt", name="310B")
rooms["310b"] = r_310b
r_backroom.form_the_room([], [], "in_game_text/night/rooms/back_room.txt", features = ["head", "exit"], pic="visual assistance/back_room.txt", name="Backroom of Gilman Hotel" )
    
#=====================================================
#==================in-game functions==================
#=====================================================


# Draws ASCII-ART pictures used in the game
def draw_picture(location, alighnment = "left", speed = 0.09):
    with open(location, "r") as image:
        # Read all instanteniously
        if speed == -1:
            print(image.read())
            return 0
        image = image.readlines()
        # Read line by line // for dramatic effect
        if alighnment == "left":
            for line in image:
                print(line, end="")
                time.sleep(speed)
            print()
        elif alighnment == "center":
            for line in image:
                print("\t\t\t" + line)
                time.sleep(speed)
            print()

# Prints text file with user defined speed character by character for style
def slow_print(location, speed = 0.01):
    if speed == -1:
        speed = 0
    with open(location, "r") as text:
        text = text.readlines()
        for line in text:
            for char in line:
                print(char, end="",flush = True)
                time.sleep(speed) #uncomment

# name explains this function's function well
def apply_item_attributes(item, negative = 1):
    attributes = item.give_attributes()
    for key in attributes.keys():
        if key == "MH":
            player.mental_health += attributes[key] * negative
        if key == "HP":
            player.HP += attributes[key] * negative
        if key == "attack":
            player.strength += attributes[key] * negative
        if key == "defence":
            player.defence += attributes[key] * negative
        if key == "stealth":
            player.stealth += attributes[key] * negative

# prints text stored in a text file as a chunck
def print_all(location):
    with open(location, "r") as text:
        return text.read()

# main function for all of the feature interactions
def interact(feature):
    global current_loc 
    global evening 
    global da_end
    global secret
    # DAYTIME
    # Interaction features in Docks
    if feature == "empty_boat":
        print(print_all("in_game_text/feature_descriptions/empty_boat.txt"))
        global em_bt_seen
        if em_bt_seen == False:
            print("Meanwhile you don't want to touch anything inside the boat, an old fisherman's knife promts your attention. \nIt would be nice to have a little something from this journey - you think")
            take_decision = input("\nDo you wish to take it (Y)es/(N)o: ").lower()
            while take_decision not in ["y", "n"]:
                take_decision = input("\nDo you wish to take it (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
            if take_decision == "n":
                print("Maybe it is smarter not to steal from these people")
            else:
                docker = Monster()
                docker.define_monster("Transitioning Hybrid", name="Docker")
                current_loc.opponents.append(docker)
                dockers_knife = Item()
                dockers_knife.form_the_item("dockers_knife", "text.txt", {"MH" : 5, "attack":8, "defence":0.03})
                player.append_inventory(["dockers_knife"])
                apply_item_attributes(dockers_knife)
                print("The docker appears from nowhere screaming: \'Ye wee pumpin' stealer, ah wull feed ye tae th' yin!\'")
        else:
            print("You decide not to risk taking it")
        em_bt_seen = True
    elif feature == "old_man":
        global raymond_talk
        global raymond_ext_talk
        global knowledge_concierge
        if raymond_ext_talk == False:
            slow_print("in_game_text/feature_descriptions/old_man_desc.txt", speed=print_speed)
            talk_r_decision = input("\nDo you wish to talk to him? (Y)es/(N)o: ").lower()
            while talk_r_decision not in ["y", "n"]:
                talk_r_decision = input("\nDo you wish to talk to him? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
            if talk_r_decision == "n":
                print()
                return 0
            if raymond_talk == False:
                print("You decide to approach the old man and talk to him: \n")
                slow_print("in_game_text/feature_descriptions/raymond_talk.txt",speed=print_speed)
                print("\Old man turns away and sighns - \"I wish only for a bottle of something that would make me forget\"")
                raymond_talk = True
            else:
                print("You decide to approach this old man once again")
                if "moonshine_bottle" in player.items:
                    player.items.remove("moonshine_bottle")
                    print("- I think we started off the wrong foot, may we start again?")
                    print("You hand a bottle of moonshine to the old man")
                    slow_print("in_game_text/feature_descriptions/raymond_talk_extended.txt", speed=print_speed)
                    knowledge_concierge = True
                    raymond_ext_talk = True
                else:
                    pressure_decision = input("\nDo you wish to pressure him? (Y)es/(N)o: ").lower()
                    while pressure_decision not in ["y", "n"]:
                        pressure_decision = input("\nDo you wish to pressure him? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
                    if pressure_decision == "y":
                        slow_print("in_game_text/feature_descriptions/raymond_fight.txt", speed=print_speed)
                        raymond = Monster()
                        raymond.define_monster("Old Man")
                        current_loc.opponents.append(raymond)
                        raymond_ext_talk = True
        else:
            print("Old man lies unconscious on the ground\n")
    # Interaction features in hotel loby
    elif feature == "concierge":
        print("A concierge stands behind a slightly worn desk, his demeanor a blend of formality and guarded curiosity. Cloaked in a faded \nuniform, he surveys the room with eyes that have witnessed the many comings and goings in Insmouth. His face, etched with the passage \nof time, carries an air of mystery, and as you approach, he regards you with an enigmatic gaze. A simple name tag \non his lapel reads \"Concierge\"")
        talk_decision = input("\nDo you wish to talk to him? (Y)es/(N)o: ").lower()
        while talk_decision not in ["y", "n"]:
            talk_decision = input("\nDo you wish to talk to him? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
        global conc_init_talk 
        if conc_init_talk == False and talk_decision == "y":
            slow_print("in_game_text/feature_descriptions/init_talk_con.txt", speed=print_speed)
            conc_init_talk = True
        elif talk_decision == "y" and conc_init_talk == True:
            print("You decide to ask the concierge if he has any updated on your friend")
            time.sleep(1)
            print("You are greeted by a simple but sharp \"No\"\n")
    elif feature == "carpet":
        slow_print("in_game_text/feature_descriptions/carpet_hl.txt", speed=print_speed)
    elif feature == "strange_portret":
        slow_print("in_game_text/feature_descriptions/strange_portret_hl.txt", speed=print_speed)
    # Interaction features in central plaza
    elif feature == "locals":
        slow_print("in_game_text/feature_descriptions/localc.txt", speed=print_speed)
    elif feature == "dormant_fountain":
        global fountain_scratch
        if fountain_scratch == False:
            slow_print("in_game_text/feature_descriptions/dormant_fountain.txt", speed=print_speed)
            player.HP -= 2
            time.sleep(1.5)
            draw_picture("visual assistance/fountain_sighn.txt", alighnment="center")
            player.mental_health -= 3
            fountain_scratch = True
        else:
            print("In the middle of the plaza stays lonely, waterless fountain. Its circular basin, crafted from weathered stone, lies silent and serene. \nMeanwhile, its once-flowing waters now rest in a state of tranquility reflecting the muted hues of the surrounding cobblestone paths.")
            print("You won't touch this thing again")
    elif feature == "pigeons":
        slow_print("in_game_text/feature_descriptions/pigeons_gen.txt", speed=print_speed)
        if "bread" in player.items:
            pigeon_dec = input("Do you wish to interact with pigeons (Y)es/(No): ").lower()
            while pigeon_dec not in ["y", "n"]:
                pigeon_dec = input("\nDo you wish to interact with pigeons (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
            if pigeon_dec == "y":
                player.items.remove("bread")
                slow_print("in_game_text/feature_descriptions/pigeons_suc.txt", speed=print_speed)
                if player.mental_health > 50:
                    slow_print("in_game_text/feature_descriptions/pigeon_letter_h_mh.txt", speed=print_speed)
                else:
                    slow_print("in_game_text/feature_descriptions/pigeon_letter_l_mh.txt", speed=print_speed)
        else:
            print("When you approach the flock, pigeons fly away")
    # Interaction features in river street
    elif feature == "window":
        global window_horror_rivst_day
        if window_horror_rivst_day == False:
            slow_print("in_game_text/feature_descriptions/window_rivst_day.txt", speed=print_speed)
            player.mental_health -= 25
            window_horror_rivst_day = True
        else:
            print("I will not return to that window again!")
    elif feature == "gate":
        global op_save_private_bread_fl
        if op_save_private_bread_fl == False:
            print("You see one slightly opened gate")
            enter_cortyard = input("Do you wish to peek in? (Y)es/(N)o: ").lower()
            while enter_cortyard not in ["y", "n"]:
                enter_cortyard = input("\nDo you wish to peek in? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
            if enter_cortyard == "y":
                slow_print("in_game_text/feature_descriptions/gate_riverst_day.txt", speed=print_speed)
                op_save_private_bread = input("Do you want to risk retrieving the bread? (Y)es/(N)o: ").lower()
                while op_save_private_bread not in ["y", "n"]:
                    op_save_private_bread = input("\nDo you want to risk retrieving the bread? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
                if op_save_private_bread == "y":
                    print("You lunge towards the bread")
                    time.sleep(0.5)
                    print("You grab it")
                    time.sleep(0.5)
                    print("As you run back, a shady figure of a teen follows you")
                    player.items.append("bread")
                    hungry_boy = Monster()
                    hungry_boy.define_monster("Young Hybrid",name ="Hungry Boy")
                    current_loc.opponents.append(hungry_boy)
                    print("Boy yells: Gie it back, tis mines")
                    op_save_private_bread_fl = True
                else:
                    print("You decide not to risk")
        else:
            print("What if his parents return? No, I won't risk it")
    # Interaction features in water street
    elif feature == "devils_reef":
        global devils_reef_close
        if devils_reef_close == False:
            slow_print("in_game_text/feature_descriptions/devils_reef.txt", speed=print_speed)
            look_closer = input("\nDo you wish to look closer? (Y)es/(N)o: ").lower()
            while look_closer not in ["y", "n"]:
                look_closer = input("\nDo you wish to look closer? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
            if look_closer == "y":
                slow_print("in_game_text/feature_descriptions/devils_reef_closelook.txt",speed=print_speed)
                player.mental_health -= 13
                devils_reef_close = True
        else:
            slow_print("in_game_text/feature_descriptions/devils_reef.txt", speed=print_speed)
            print("\nI don't want to look there anymore")
    # Interaction features in rail
    elif feature == "arkcham":
        print("You notice an old and overgrown sign saying \"Arkcham\"")
        time.sleep(0.5)
        print("I can't leave yet, Alex might need my help")
    elif feature == "abandoned_wagon":
        if player.mental_health >= 75:
            slow_print("in_game_text/feature_descriptions/abandoned_wagon_hmh.txt", speed=print_speed)
        else:
            slow_print("in_game_text/feature_descriptions/abandoned_wagon_lmh.txt", speed=print_speed)
    # NIGHT
    # Interaction features in water street 
    elif feature == "docks":
        print("Noticing strange movement down at the docks, you decide to look closer")
        if player.classType != "DoomSlayer":
            slow_print("in_game_text/night/features/docks_view.txt", speed=print_speed)
        else:
            slow_print("in_game_text/night/features/docks_view_doom.txt", speed=print_speed)
    elif feature == "reef":
        print("You decide to look closer on what is happening on the reef")
        if player.classType != "DoomSlayer":
            slow_print("in_game_text/night/features/reef.txt", speed=print_speed)
        else:
            slow_print("in_game_text/night/features/reef_doom.txt", speed=print_speed)
    # Interaction features in 310B
    elif feature == "bed":
        global room_fight
        global room_fight
        if evening == False:
            slow_print("in_game_text/night/features/bed.txt", speed=print_speed)
            sleep = input("\nDo you wish to sleep? (Y)es/(N)o: ").lower()
            while sleep not in ["y", "n"]:
                sleep = input("\nDo you wish to sleep? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
            if sleep == "y":
                if "bread" in player.items:
                    print("Before falling asleep you eat the bread you have stolen")
                    player.items.remove("bread")
                    player.HP += 10
                if "moonshine_bottle" in player.items:
                    print("You use moonshine_bottle you found to treat both your external and internal wounds")
                    player.items.remove("moonshine_bottle")
                    player.HP += 10
                    player.mental_health += 10
                player.HP += 5
                print("You drift off to sleep")
                time.sleep(1)
                print("You hear strange noises downstairs")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear') # taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
                print("=" * 150)
                players_card = Player.__str__(player).split("\n")
                players_card.pop(0)
                count = 1
                for line in players_card:
                    if count == 1:
                        print("January 14th, 1986" + " " * 98 + line)
                    elif count == 2:
                        print("Time: 03:18" + " " * 105 + line)
                    else:   
                        print(" " * 116 + line)
                    count += 1
                print()
                slow_print("in_game_text/night/wake_up.txt",speed=print_speed)
                evening = True
        else:
            print("Pointlessly you stare at the door")
            if room_fight == False:
                print("\nLocals try to break your door")
                fight = random.randint(0, 100)
                if fight <= 70:
                    print("The door stands strong")
                else:
                    print("The door flies off the handle")
                    current_loc.opponents.append(deep_one_6)
                    battle(player, deep_one_6, current_loc)
                    if player.isStillAlive() == True:
                        room_fight = True
                        r_310b.connections.append("hotel_loby")
    elif feature == "desk":
        if evening == False:
            slow_print("in_game_text/night/features/desk.txt", speed=print_speed)
        else:
            print("You pointlesly stare at the writing desk")
            if room_fight == False:
                print("\nLocals try to break your door")
                fight = random.randint(0, 100)
                if fight <= 70:
                    print("The door stands strong")
                else:
                    print("The door flies off the handle")
                    current_loc.opponents.append(deep_one_6)
                    battle(player, deep_one_6, current_loc)
                    if player.isStillAlive() == True:
                        room_fight = True
                        r_310b.connections.append("hotel_loby")
    elif feature == "door":
        print("This door leads to an adjacent corner room")
        if evening == True:
            print("You attempt to barge the doors open")
            barge = random.randint(0, 100)
            if barge < ((player.strength/22)*100):
                print("You successfuly barge the door")
                if room_fight == False:
                    slow_print("in_game_text/night/311B.txt", speed=print_speed)
                else:
                    slow_print("in_game_text/night/311B_win.txt", speed=print_speed)
                time.sleep(1)
                jump = random.randint(0,100) + player.strength
                if jump <= 50:
                    print("\nBut you fail, and fall towards the ground of river_street")
                    player.HP -= 80
                    current_loc = r_river_street
                else:
                    print("\nAnd you successfuly land on the adjacent roof")
                    print("\nYou notice downpipe that you use to safely descend to river_street")
                    current_loc = r_river_street
            else:
                print("You fail barge the door")
                if room_fight == False:
                    print("\nLocals try to break your door")
                    fight = random.randint(0, 100)
                    if fight <= 70:
                        print("The door stands strong")
                    else:
                        print("The door flies off the handle")
                        current_loc.opponents.append(deep_one_6)
                        battle(player, deep_one_6, current_loc)
                        if player.isStillAlive() == True:
                            room_fight = True
                            r_310b.connections.append("hotel_loby")
    # Interaction features in rail
    elif feature == "arckham":
        if secret == False :
            slow_print("in_game_text/night/features/archam_base_victory.txt",speed=print_speed)
            print("Ending 1/3 achieved, the mistery of your friend's dissaperance remains a secret, evil still lives on Devil's reef, but you still ESCAPED FROM SHADOWS OF Insmouth")
            da_end = True
        else:
            slow_print("in_game_text/night/features/archam_base_victory.txt",speed=print_speed)
            print("Ending 2/3 achieved, your friend has been avenged, evil still lives on Devil's reef, but you still ESCAPED FROM SHADOWS OF Insmouth")
            da_end = True
    # Interaction features in hotel loby 
    elif feature == "backroom":
        if "backroom_key" in player.items:
            print("You use the stolen key to enter the room, mentaly preparing yourself for what's inside")
            current_loc = r_backroom
            player.mental_health -= 14
        else:
            print("You attempt to open the door, but fail because it is closed with a key")
    # Interaction features in hotel backroom
    elif feature == "head":
        slow_print("in_game_text/night/features/alex_head.txt", speed=print_speed)
        if secret == False:
            player.mental_health -= 30
            secret = True
            if player.mental_health <= 15:
                current_loc.features.append("strange_symbol")
                player.mental_health -= 4
    elif feature == "exit":
        print("As you rush to leave this grusome place the door swings open, and you see concierge himself")
        print("- I see you figured out my little secret, well now its time for you to join your friend at last")
        print("\n //Your blood boiles in sight of this murderer")
        player.strength += 8
        player.mental_health += 5
        player.HP += 30
        current_loc = hotel_loby
        hotel_loby.features.remove("backroom")
        current_loc.opponents.append(concierge)
        battle(player, concierge, current_loc)
        print("You have avenged your friend, now it is time to leave this damned place through that roof")
    elif feature == "strange_symbol":
        print("- \"This sign again, just like on the fountain\"\n")
        time.sleep(1)
        draw_picture("visual assistance/fountain_sighn.txt", alighnment="center")
        print("\n\n- But this time with strange text beneath")
        slow_print("in_game_text/night/features/strange_symbol.txt",speed=print_speed)
        if "golden_ingot" in player.items:
            print("\n//You insert coin into the small hole in the wall, right underneath the symbol and text")
            player.items.remove("golden_ingot")
            password = input("Scream the Password: ")
            if password == "4221":
                print("Floor starts to temble")
                time.sleep(1.5)
                print("Wall in front of you falls, revealing an old skeleton and a chest")
                time.sleep(2)
                print("You touch the skeleton, and something clicks")
                time.sleep(1)
                print("- Fuck yeah! I'm back.\n")
                print("You take what's rightfuly yours from your chest")
                time.sleep(1)
                player.define_character(player.name,"DoomSlayer")
                print("As you revive from the dead the door swings open, and you see concierge himself")
                print("A flicker of confusion crosses his face as the harsh overhead light reveals a figure vastly different from the typical visitors of Insmouth.")
                print("mix of fear and bewilderment flashes across his face, realizing that the night's unfolding horrors have taken an unexpected turn. In that \nbrief moment, the concierge contemplates the gravity of the situation, realizing that the forces at play in Insmouth may have summoned an even \ngreater, more relentless force ")
                print("\nWithout hesitation you raise the mighty Super Shotgun, its barrel gleaming ominously in the dim light.\n -Bang!")
                input("Type anything to show these fishes and their little reef their demise: ")
                print("You shoot at the wall creating a passageway to the river_street")
                r_river_street.reform_the_room(connections=["water_street"],description="in_game_text/night/features/doom/river_street.txt")
                r_water_street.reform_the_room(connections=["docks"], description="in_game_text/night/features/doom/water_street.txt")
                r_dock.reform_the_room(connections=[], description="in_game_text/night/features/doom/docks.txt", features=["mottor_boat"])
                current_loc = r_river_street
        else:
            None
    # Interaction features in Docks
    elif feature == "mottor_boat":
        print("\"This will do\" - you think as you approach one of the mottor boats atached to a pier")
        print("Beware the inhabitants of the devils reef, the DOOM is comming")
        slow_print("in_game_text/night/features/doom/doom_victory.txt", speed=print_speed)
        print("\nSecret Ending 3/3 achieved, your friend has been avenged, the afte of evil living on the Devil's reef remains unknown, and you still CONQUERED THE SHADOWS OF Insmouth")
        da_end = True
    return 0

# Forms all of the night time enemies
def form_enemies():
    deep_one_1 = Monster()
    deep_one_2 = Monster()
    deep_one_3 = Monster() 
    deep_one_4 = Monster()
    deep_one_5 = Monster()
    deep_one_6 = Monster()
    young_hybrid_1 = Monster()
    young_hybrid_2 = Monster()
    young_hybrid_3 = Monster()
    trans_hyb_1 = Monster()
    trans_hyb_2 = Monster()
    trans_hyb_3 = Monster()
    trans_hyb_4 = Monster()
    trans_hyb_5 = Monster()
    concierge = Monster()
    deep_one_1.define_monster("Deep One")
    deep_one_2.define_monster("Deep One")
    deep_one_3.define_monster("Deep One")
    deep_one_4.define_monster("Deep One")
    deep_one_5.define_monster("Deep One")
    deep_one_6.define_monster("Deep One")
    young_hybrid_1.define_monster("Young Hybrid")
    young_hybrid_2.define_monster("Young Hybrid")
    young_hybrid_3.define_monster("Young Hybrid")
    trans_hyb_1.define_monster("Transitioning Hybrid")
    trans_hyb_2.define_monster("Transitioning Hybrid")
    trans_hyb_3.define_monster("Transitioning Hybrid")
    trans_hyb_4.define_monster("Transitioning Hybrid")
    trans_hyb_5.define_monster("Transitioning Hybrid")
    concierge.define_monster("Transitioning Hybrid", name="Concierge Gilman")
    return (deep_one_1,deep_one_2, deep_one_3, deep_one_4, deep_one_5, deep_one_6, young_hybrid_1, young_hybrid_2, young_hybrid_3, trans_hyb_1,trans_hyb_2,trans_hyb_3,trans_hyb_4,trans_hyb_5, concierge)

# Transition into second Act
def set_evening():
    print("As the night draws near, and your friend is yet to be found you decide to stay overnight at the local hotel")
    input("Type anything to transition into the second act: ")
    os.system('cls' if os.name == 'nt' else 'clear') # taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    # form all enemies and reform locations for their nighttime form
    global deep_one_1,deep_one_2, deep_one_3, deep_one_4, deep_one_5, deep_one_6, young_hybrid_1, young_hybrid_2, young_hybrid_3, trans_hyb_1,trans_hyb_2,trans_hyb_3,trans_hyb_4,trans_hyb_5, concierge
    deep_one_1,deep_one_2, deep_one_3, deep_one_4, deep_one_5, deep_one_6, young_hybrid_1, young_hybrid_2, young_hybrid_3, trans_hyb_1,trans_hyb_2,trans_hyb_3,trans_hyb_4,trans_hyb_5, concierge = form_enemies()
    r_dock.reform_the_room(connections=["devils_reef", "water_street"], description="in_game_text/night/rooms/docks_night.txt", features=[], pic="visual assistance/dock_night.txt", opponents=[deep_one_1,deep_one_2,deep_one_3,deep_one_4])
    r_water_street.reform_the_room(description="in_game_text/night/rooms/water_st_night.txt", features=["docks", "reef"], pic="visual assistance/water_street_night.txt", opponents=[trans_hyb_1, trans_hyb_2])
    r_river_street.reform_the_room(connections=["water_street", "rail"], description="in_game_text/night/rooms/river_street_night.txt", features=[], opponents=[young_hybrid_1,young_hybrid_2])
    r_hotel_loby.reform_the_room(connections=["310B"], description="in_game_text/night/rooms/hotel_loby.txt", pic="visual assistance/hotel_loby_night.txt", features=["carpet", "strange_portret", "backroom"])
    r_rail.reform_the_room(features=["arckham"], description="in_game_text/night/rooms/rail_night.txt")
    # transition into the second act
    print("=" * 58 + "ACT TWO -- THE NIGHT OF REVELATION" + "=" * 58) 
    players_card = Player.__str__(player).split("\n")
    players_card.pop(0)
    count = 1
    for line in players_card:
        if count == 1:
            print("January 13th, 1986" + " " * 98 + line)
        elif count == 2:
            print("Time: 20:17" + " " * 105 + line)
        else:   
            print(" " * 116 + line)
        count += 1
    if conc_init_talk == True:
        slow_print("in_game_text/night/concierge_talk.txt", speed=print_speed)
    else:
        slow_print("in_game_text/night/concierge_talk_first.txt", speed=print_speed)
    if knowledge_concierge == True:
        print("\n\nRemembering what an old man had to say in the Docks, you are worried about what might lay in that backroom.")
        time.sleep(2)
        print("As you go up the stairs, concierge leading the way. You notice an opportunity to snatch the key from his back pocket")
        steal_decision = input("\nDo you want to risk it? (Y)es/(N)o: ").lower()
        while steal_decision not in ["y", "n"]:
            steal_decision = input("\nDo you want to risk it? (Y)es/(N)o #Type \'Y\' for yes or \'N\' for no: ").lower()
        if steal_decision == "y":
            steal = random.randint(0, 100)
            if steal > (player.stealth*100):
                print("You successfuly steal the key")
                player.items.append("backroom_key") 
            else:
                print("You fail to steal the key, but fortunately he didn't notice your attempt")
    time.sleep(1)
    print("- Here is your room, don't go anywhere at night. We have curfew till 6:00 am")
    input("type anything to continue: ")
    return r_310b


#=================================================
#==================Main Gameplay==================
#=================================================


# Intro 
print("\n\nRECOMENDED WINDOW RESOLUTION OF AT LEAST 150x60")
print_speed = input("Type how fast do you want the text and pictures to be printed(slow, fast, instant): ").lower()
if print_speed == "slow":
    print_speed = 0.01
elif print_speed == "fast":
    print_speed = 0.0012
else:
    print_speed = -1

input("Type anything to start the game once you are ready: ")
print("=" * 128)
draw_picture("visual assistance/intro_text.txt", speed=print_speed)
print("=" * 128)
print("January 13th, 1986\nTime: 14:47\n")
print("Hiking through the rough terrain, you suddenly stop to check your map on your way to the shady and largely unknown city of Insmouth")
print("It was practically impossible to find it, considering that for some reason this \"city\" is omitted from the majority of the maps")
print("Yet, you were lucky to buy a local map from some lunatic in Arkham with very strange, buldgy eyes.")
print("\nNow, being here and feeling the drizzle that promises to harden into a serious storm soon, you start thinking if a letter that you")
print("received is trustworthy enough for all of this effort. You take a piece of crumpled paper that once was a letter writen to you\nby your close friend.")
print("\n\n\n")
# Take player's name
print("The letter:\n\n")
player_name = input("Dear ")
# Accept no more than 24 letters for the name 
if len(player_name) >= 24:
    n_name = ""
    for i in range(0, 25):
        n_name += player_name[i]
    player_name = n_name
#Print letter
slow_print("in_game_text/intro_letter.txt", speed = print_speed)
input("\n\nType anything to finish reading: ")
print("\n\n\n")
slow_print("in_game_text/after_letter.txt",speed= print_speed)
print("\n\n")
print("================================================================================================================================")
print("|| Rush the hill like during old boxing trainings || Concentrate on the path like during yoga || Find the most reliable rocks ||")
print("|| Perk \"Boxer\":                                  || Perk \"Yog\":                              || Perk \"Thief\":                ||")
print("|| Attack + 10 points                             || HP + 30 points                           || Defence chance + 15%         ||")
print("|| Defence chance + 25%                           || MH + 50 points                           || Stealth + 45%                ||")
print("||Type(R)                                         ||Type(C)                                   ||Type(F)                       ||")
print("================================================================================================================================")

# Choose starting class
chosen_perk =  input("Choose your approach: ").lower()
while chosen_perk != "r" and chosen_perk != "c" and chosen_perk != "f":
    chosen_perk = input("Invalid input, try again: ").lower()

player = Player()
if chosen_perk == "r":
    player.define_character(name = player_name, classType="Boxer")
    print("\nYou rush towards the peak, and despite the rough terrain, you muscle your way through\n")
elif chosen_perk == "c":
    player.define_character(name = player_name, classType="Yog")
    print("\nDespite being tired you concentrate on making one more step at a time, making your way to the top\n")
else:
    player.define_character(name = player_name, classType="Thief")
    print("\nWith your expirienced thief's eye, you see the most comfortable way up, successfuly climbing this hill\n")

input("\n\n\nType anything to transition into the first act: ")
os.system('cls' if os.name == 'nt' else 'clear') # taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python

# First Act 
print("=" * 60 + "ACT ONE - GRIM and EMPTY PLACE" + "=" * 60) 
players_card = Player.__str__(player).split("\n")
players_card.pop(0)
count = 1
for line in players_card:
    if count == 1:
        print("January 13th, 1986" + " " * 98 + line)
    elif count == 2:
        print("Time: 15:17" + " " * 105 + line)
    else:
        print(" " * 116 + line)
    count += 1
print("\nFinally! - You exclaim\n")
print("The city of Insmouth: ")
print("=" * 150)
draw_picture("visual assistance/Insmouth_view_from_above.txt", speed=print_speed)
print("\n=" + "=" * 149)
slow_print("in_game_text/first_act_one.txt",speed=print_speed)

# Choice of initial location
print("\n\n")
print("Choose where to search your friend first: ")
print("1) He really liked the ocean, local fisherman dock is the best place to start")
print("2) According to the map this place has only one hotel, I should start there")
print("3) My mother always taught me to start at the center, I shall explore the central plaza")
first_loc = input("\nType your choise: ")
while first_loc != "1" and first_loc != "2" and first_loc != "3":
    first_loc = input("Invalid input, try typing 1,2, or 3: ").lower()

print("\n")
if first_loc == "1":
    current_loc = r_dock
elif first_loc == "2":
    current_loc = r_hotel_loby
else:
    current_loc = r_central_plaza

player.HP += 50
# Main game loop
count = -1
while(True):
    if player.isStillAlive() == False or da_end == True:
        break
    print(current_loc.name + ":\n")
    print(current_loc)
    print("The {} connects to {}".format(current_loc.name, current_loc.connections))
    print("\n\n")
    if len(current_loc.opponents) >= 1:
        for enemy in current_loc.opponents:
            print("You notice an enemy, and attempt to hide")
            hide = random.randint(0, 100)
            if hide < (player.stealth*100):
                print("You successfuly avert the fight by hiding")
                current_loc.opponents.remove(enemy)
            else:
                print("You attempt hiding, but you have been spoted")
                battle(player, enemy, current_loc)
    if player.isStillAlive() == False:
        break
    print("You look arround the {} and notice the following: {} \\\\Type interact \'object name\' to interact".format(current_loc.name, current_loc.features))
    print("You also see the following items: {} \\\\Type look \'object name\' to see closer".format(current_loc.items))
    print("\n")
    print(player.status())
    print("\n" + "=" * 150)
    action = input("Your action: ").lower()
    action = action.split(" ")
    if (action[0] == "look" or action[0] == "la" or action[0] == "see"): 
        try:
            if action[1] in current_loc.items: 
                print("You look at {}: {}\n".format(action[1], w_items[action[1]].describe()))
                action = input("Do you want to take it? (type take \'object name\'): ").split(" ")
            elif action[2] in current_loc.items:
                print("You look at {}: {}\n".format(action[2], w_items[action[2]].describe()))
                action = input("Do you want to take it? (type take \'object name\'): ").split(" ")
            else:
                print("Invalid object, try again")
        except:
            print("Invalid object, try again")
    if (action[0] == "take" or action[0] == "pick" or action[0] == "grab"):
        try:
            if action[1] in current_loc.items:
                player.items.append(action[1])
                apply_item_attributes(w_items[action[1]])
                current_loc.items.remove(action[1])
                os.system('cls' if os.name == 'nt' else 'clear') # taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
                continue
            elif action[2] in current_loc.items:
                player.items.append(action[2])
                apply_item_attributes(w_items[action[1]])
                current_loc.items.remove(action[2])
                os.system('cls' if os.name == 'nt' else 'clear') # taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
                continue
            else:
                    print("Invalid object, try again")
        except:
            print("Invalid object, try again")
    if action[0] == "interact":
        try:
            if action[1] in current_loc.features:
                interact(action[1])
            elif action[2] in current_loc.features:
                interact(action[2])
            else:
                print("Invalid object, try again")
        except:
            print("Invalid object, try again")
    if action[0] == "move" or action[0] == "walk" or action[0] == "run" or action[0] == "transition" or action[0] == "go" or action[0] == "sneak":
        if action[1] in current_loc.connections:
            current_loc = rooms[action[1]]
            count += 1
        elif action[2] in current_loc.connections:
            current_loc = rooms[action[2]]
            count += 1
        else:
                print("Invalid destination, try again")
    if action[0] == "break" or player.isStillAlive() == False or da_end == True:
        break
    if action[0] == "suicide" or player.mental_health == 0:
        print("YOU DECIDE TO SURRENDER\nANOTHER SOULD LOST IN THE SHADOWS OF Insmouth".lower())
        break
    input("Type anything to continue: ")
    if count == 10:
        current_loc = set_evening()
        count += 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear') # taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python