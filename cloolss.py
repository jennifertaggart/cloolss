""" I am CLothing Organizer/Optimizer Logical Style System!
Run me with the Python interpreter for now.
I read in formatted data files of clothing items and print out outfits.
I am in pre-beta.
"""
import glob
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
        if (clothing_item[0] == 'bottom'):
            possible_bottoms.append(clothing_item)
    for layer in layering_types:
        if (clothing_item[0] == 'layer'):
            possible_layers.append(clothing_item)
    for accessory in accessory_types:
        if (clothing_item[0] == 'accessory'):
            possible_accessories.append(clothing_item)
    if (clothing_item[3].isdigit()):
        possible_tops.append(clothing_item)                            
    

def match(outfit, clothingitem):
    """Tests whether a new clothing item matches any items in outfit by 
    looping over all colors in outfit and checking them against all colors 
    in the new clothing item returns match if any two colors match
    """
    outfit_colors = outfit[1]
    clothing_item_colors = clothing_item[1]
    for color in outfit_colors:
        print(color)
        for anothercolor in clothing_item_colors:
            print(anothercolor)
            if (color == anothercolor):
                print("Match!")
                return match 	

def create_outfit():
    print("Outfit created!")               			

#Define outfit and clothing item for testing
outfit = ['scarf', ['purple'], 'loose fitting', 'NA', 'gauze', 'seasonless', 
'clean']
clothing_item = ['scarf', ['yellow', 'green', 'dark green', 'brown', 'pink', 
'baby blue', 'orange', 'black'], 'loose fitting', 'NA', 'gauze', 'seasonless'
, 'clean']
match(outfit, clothing_item)

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
		clothing_type(clothing_item)
		print("Item is clean and in season!")
		
print("That's all I can do right now, bye!")	

# TO DO: Generate three sample outfits (print them out)
# TO DO: Use Google AppEngine SDK and Google Appengine to put on web (see realpython article)
# TO DO: Implement js with localstorage for washed/not washed, have a "did laundry" button that sets everything to washed again
