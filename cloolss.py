""" I am CLothing Organizer/Optimizer Logical Style System!
Run me with the Python interpreter for now.
I read in formatted data files of clothing items and print out outfits.
I am in pre-beta.
"""
import random
import glob
import re

def error_stuff():
    """ Print error message and exit program
    """
    error_message = "Invalid clothing item. Please move this clothing item's file out of the clothing directory!"
    print(error_message)
    print(clothing_item)
    exit()

def validate_input():
    """ Test the clothing files for valid input. Line 1 must match something 
    in valid clothing item array. Line 4 must be a number, or NA, or N/A. Line 5 is not checked because
    we aren't doing anything with it yet. Other lines must match set of 2 or 3 specific sctrings, or NA or N/A
    """
    valid_clothing_items = ['shirt', 'shoes', 'scarf', 'hat', 'dress', 'skirt', 'pants', 'shorts', 'sweater', 'blazer']
    valid_item_flag = 0
    for item in valid_clothing_items:
        if (item == clothing_item[0]):
            valid_item_flag = 1
    if (valid_item_flag == 0):
            print("Problem in first line!")
            error_stuff()
    #print(clothing_item[1])
    if ((clothing_item[2] != 'loose-fitting') and (clothing_item[2] != 'close-fitting')):
        if ((clothing_item[2] != 'NA') and (clothing_item[2] != 'N/A')):
            print("Problem in 3rd line")
            error_stuff()
    # Line 2 is read as a string, so can't just check if type is list.
    # Check for beging with [', end with '], and an even number of 's
    if (re.search("^\[", clothing_item[2]) != 'None'):
        if (re.search("$\]", clothing_item[2]) != 'None'):
            #all_my_little_quotes = re.search("\[", clothing_item[2])
            #print(all_my_little_quotes)
            #print("Maybe I have a list!")
            pass #finish this later
#new_thing_colors_line = re.sub(r'\'|\[|\]|\"', '', new_thing_colors_line)
 #   if isinstance(check_list,list):
  #      print("Test list success!")        
   # if not isinstance(clothing_item[2],str):
    #    print("I am not a list!")
     #   error_stuff()  
    # Can try live in the middle of a function like this?          
    try:
        return float(clothing_item[3])
    except ValueError:
        if ((clothing_item[3] != 'NA') and (clothing_item[3] != 'N/A')):
            print("Problem in 4th line")
            error_stuff()  
    # Not checking line 5 (fabric) yet because no specific plans.                       
    if (clothing_item[5] != 'dry season'):
        if (clothing_item[5] != 'rainy season'):
            if (clothing_item[5] != 'seasonless'):
                print("Problem is 6th line!")
                error_stuff()
    if ((clothing_item[6] != 'clean') and (clothing_item[6] != 'wash')):
        print("Problem in 7th line!")
        error_stuff()
    #print(clothing_item[6])        

def clean_and_in_season(thing):
    """Test whether clothing is clean and in-season."""
    if (clothing_item[6] == "clean"):
    	if (clothing_item[5] == season or clothing_item[5] == "seasonless"):
    		return True

def clothing_type(thing):
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
    if (clothing_item[0] == "shoes"): 
        #print("It's a shoe!")
        possible_shoes.append(clothing_item)                          
    

def match(thing_collection, new_thing, add_neutrals):
    """Tests whether a new thing matches any items in a collection of 
    existing things by looping over all colors in collection and 
    checking them against all colors in the new thing. Returns match 
    if any two colors match.
    """
    # Only add the neutral colors if the add_neutrals flag is set, so we don't 
    # add them every time we match something
    if (add_neutrals == 1):
        # Read these from a config file using configpaeser eventually
        neutrals = ['black', 'white', 'indigo', 'nude', 'brown', 'tan', 
        'khaki', 'navy', 'gray']
    else:
        neutrals = []    
    # Having a heck of a time passing my arrays for clothing items to this 
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
    collection_colors = thing_collection_colors_line.split(",") + neutrals
    #collection_colors = collection_colors.extend(neutrals)
    #print("Collection colors are")
    #print(collection_colors)
    #print(len(collection_colors))
    new_thing_colors_line = new_thing[1]
    new_thing_colors_line = re.sub(r'\'|\[|\]|\"', '', new_thing_colors_line)
    #print(new_thing_colors_line)
    new_thing_colors = new_thing_colors_line.split(",")
    #new_thing_colors = new_thing_colors_line.strip("][").split(",")
    #print("New thing colors are")
    #print(new_thing_colors)
    for color in collection_colors:
        #print(color)
        for anothercolor in new_thing_colors:
            #print(anothercolor)
            if (color == anothercolor):
                print("Match!")
                collection_colors = collection_colors + new_thing_colors
                print("New collection colors are:")
                print(collection_colors)
                return collection_colors 	

def convert_to_celsius(temp):
    return((temp - 32)/1.8)

def clo_test():
    print("Clo test called!")
    while True:
        try:
            low = float(input("What is the expected low (F)?")) 
            break 
        except ValueError:
            print("I need a number, like 50 or 42.3")  
    while True:         
        try:       
            high = float(input("What is the expected high (F)?"))
            break
        except ValueError:
            print("I need a number, like 76 or 100.5")
    if (high < low):
        print("Low is greater than high? I'm confused...")
        exit(1)
    low_c = convert_to_celsius(low)
    high_c = convert_to_celsius(high)
    print(low_c) 
    print(high_c)
    #clo_for_low = 
    #clo_for_high =     

def create_outfit():
    """Choose a random bottom and append it to outfit.
    """
    outfit = []
    choose_bottom = random.randint(0,(len(possible_bottoms)-1))
    #print(choose_bottom)
    bottom = possible_bottoms[choose_bottom]
    #print("Chosen bottom is:")
    #print(bottom)
    outfit.append(bottom)
    choose_top = random.randint(0,(len(possible_tops)-1))
    top = possible_tops[choose_top]
    #print("Chosen top is:")
    #print(top)
    # Match with neutrals flag set to get neutral items added to color
    # collection
    if match(bottom, top, 0):
        outfit.append(top)
        choose_accessory = random.randint(0,(len(possible_accessories)-1))
        accessory = possible_accessories[choose_accessory]
        outfit.append(accessory)
        choose_shoes = random.randint(0,(len(possible_shoes)-1))
        shoes = possible_shoes[choose_shoes]
        outfit.append(shoes)
        print("Outfit created! Here's what to wear:")
        print(outfit)
        return True
    else:
        print("Fail! Trying again...")
        create_outfit()
        return False
                      		
def main():
    print("Hello, I'm CLOOLSS!")
    print("CLothing Organizer/Optimizer Logical Style System!")
    print("I am in pre-beta.")
    files = glob.glob('./*.txt')
    # Get the input highs and lows
    clo_test()
    # I am probably not supposed to be declaring a whole bunch of global 
    # variables in my main function. Figure out better way to do this. 
    global season, clothing_database, possible_bottoms, possible_tops 
    global possible_layers, possible_accessories, possible_shoes
    season = 'dry season'
    clothing_database = []
    possible_bottoms = []
    possible_tops = []
    possible_layers = []
    possible_accessories = []
    possible_shoes = []
    # Shoes and scarves
    for file in files:
        # Open the file, read in the lines, and split into an array with one 
        # line per entry
        global clothing_item
        clothing_item = open(file).read().splitlines() 
        validate_input()
        if clean_and_in_season(clothing_item):
    	    #print("Item is clean and in season!")
    	    clothing_type(clothing_item)
    	    #print("I found out what type of clothing")
    print("About to call create outfit")        
    create_outfit()
    print("That's all I can do right now, bye!")	

main()
   
# TO DO: Implement in js with localstorage for washed/not washed, have a 
# "did laundry" button that sets everything to washed again
# Set up your own neutrals
# Pants length/ heel height checking module
# Better outfit insulation estimation with clo
# Shoe rest rule where shoes have to rest x number of days after they are worn
# Should do some unit testing