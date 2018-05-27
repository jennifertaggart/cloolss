""" I am CLothing Organizer/Optimizer Logical Style System!
Run me with the Python interpreter for now.
I read in formatted data files of clothing items and print out outfits.
I am in pre-beta.
"""
import random
import glob
import re
files = glob.glob('./*.txt')
config = open('cloolss.cfg').read()

# Do LOTS of checking to make sure files are formatted correctly
#def checkfiles ()

def clean_and_in_season(clothingitem):
    """Test whether clothing is clean and in-season."""
    if (clothing_item[6] == "clean"):
    	if (clothing_item[5] == season or clothing_item[5] == "seasonless"):
    		return True

def clothing_type(clothingitem):
    """Test whether clothing item is a top, bottom, layer, or accessory 
    and add it to the appropriate array.
    """	
    bottom_types = ['pants', 'shorts', 'skirt', 'dress']
    layering_types = ['sweater', 'blazer']
    accessory_types = ['scarf','hat']
    for bottom in bottom_types:
        if (clothing_item[0] == bottom):
            possible_bottoms.append(clothing_item)
            #print("Added pants or shorts or skirt!")
    for layer in layering_types:
        if (clothing_item[0] == layer):
            possible_layers.append(clothing_item)
            #print("Added layer!")
    for accessory in accessory_types:
        if (clothing_item[0] == accessory):
            possible_accessories.append(clothing_item)
            #print("Added accessory!")
    if (clothing_item[3].isdigit()):
        possible_tops.append(clothing_item)
        #print("Added top!")                        
    

def match(thing_collection, new_thing):
    """Tests whether a new thing matches any items in a collection of 
    existing things by looping over all colors in collection and 
    checking them against all colors in the new thing. Returns match 
    if any two colors match.
    """
<<<<<<< HEAD
    # Had to rather aggressively tell python these were lists, may be
    # better way to do this
    collection_colors = thing_collection[1].split()
    # Read these from a config file using configpaeser eventually
    neutrals = ['black', 'white', 'indigo', 'nude', 'brown', 'tan', 'khaki', 
    'navy', 'gray']
    collection_colors = collection_colors + neutrals
=======
    # Having a hell of a time passing my arrays for clothing items to this 
    # function as arrays. *arg1 doesn't work because there are two arrays I'm
    # passing in, I think. So I am ending up with a string. Using split and 
    # regexp to process now, circle back later for better solution.
    # import my colors as a string  
    thing_collection_colors_line = thing_collection[1]
    # Sigh. Basically remove all the array syntax from my mal-stringified 
    # array (I mean list) except the commas, then split on the commas to make 
    # it an array.
    thing_collection_colors_line = re.sub(r'\'|\[|\]|\"', '', thing_collection_colors_line)
    #print(thing_collection_colors_line)
    collection_colors = thing_collection_colors_line.split(",")
    #neutrals = ['black', 'white', 'indigo', 'nude', 'brown', 'tan', 'khaki', 'navy', 'gray']
    #collection_colors = collection_colors.extend(neutrals)
>>>>>>> tmp
    print("Collection colors are")
    print(collection_colors)
    #print(len(collection_colors))
    new_thing_colors_line = new_thing[1]
    new_thing_colors_line = re.sub(r'\'|\[|\]|\"', '', new_thing_colors_line)
    print(new_thing_colors_line)
    new_thing_colors = new_thing_colors_line.split(",")
    #new_thing_colors = new_thing_colors_line.strip("][").split(",")
    print("New thing colors are")
    print(new_thing_colors)
    for color in collection_colors:
        #print(color)
        for anothercolor in new_thing_colors:
            #print(anothercolor)
            if (color == anothercolor):
                print("Match!")
                return match 	

def create_outfit():
    """Choose a random bottom and append it to outfit.
    """
    outfit = []
    choose_bottom = random.randint(0,(len(possible_bottoms)-1))
    print(choose_bottom)
    bottom = possible_bottoms[choose_bottom]
    print("Chosen bottom is:")
    print(bottom)
    outfit.append(bottom)
    choose_top = random.randint(0,(len(possible_tops)-1))
    top = possible_tops[choose_top]
    print("Chosen top is:")
    print(top)
    if match(bottom, top):
        outfit.append(top)
        choose_accessory = random.randint(0,(len(possible_accesories)-1))
        if match(outfit,accessory):
            outfit.append(accessory)
            print("Outfit created!")
            print(outfit)

    else:
        print("Go to the store!")                   			

#Define outfit and clothing item for testing
#outfit = ['scarf', ['purple'], 'loose fitting', 'NA', 'gauze', 'seasonless', 
#'clean']
#clothing_item = ['scarf', ['yellow', 'green', 'dark green', 'brown', 'pink', 
#'baby blue', 'orange', 'black'], 'loose fitting', 'NA', 'gauze', 'seasonless'
#, 'clean']
#match(outfit, clothing_item)

print("Hello World, I'm CLOOLSS!")
print("CLothing Organizer/Optimizer Logical Style System!")
#Arrays are called lists in python whyyyyy
# clothingdatabase is going to be the working database of items of clean 
# clothing appropriate to season setting season to dry right now
season = 'dry season'
clothing_database = []
possible_bottoms = []
possible_tops = []
possible_layers = []
possible_accessories = []

# Shoes and scarves
for file in files:
	# TO DO: need to do LOTS of validation of input here!
	# Open the file, read in the lines, and split into an array with one line
	# per entry
	clothing_item = open(file).read().splitlines() 
	if clean_and_in_season(clothing_item):
		#print("Item is clean and in season!")
		clothing_type(clothing_item)
		#print("I found out what type of clothing")
 
#print(possible_bottoms[0])
create_outfit()
#print(possible_accessories[0])
		#print("Item is clean and in season!")
		
print("That's all I can do right now, bye!")	

# TO DO: Generate three sample outfits (print them out)
# TO DO: Use Google AppEngine SDK and Google Appengine to put on web (see realpython article)
# TO DO: Implement js with localstorage for washed/not washed, have a "did laundry" button that sets everything to washed again
