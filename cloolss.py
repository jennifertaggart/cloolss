# Run me with the Python interpreter for now
# I am CLothing Organizer/Optimizer Logical Style System!
print("Hello World, I'm CLOOLSS!")
print("CLothing Organizer/Optimizer Logical Style System!")
# Do LOTS of checking to make sure files are 
import glob
files = glob.glob('./*.txt')

#Arrays are called lists in python whyyyyy
# clothingdatabase is going to be the working database of items of clean clothing appropriate to season
# setting season to dry right now
season = "dry season"
clothingdatabase = []
possiblebottoms = []
bottomtypes = ["pants", "shorts", "skirt", "dress"]
toptypes = ["no sleeves", "short sleeves", "long sleeves", "3/4 sleeves"]
layeringtypes = ["sweater", "blazer"]
# Shoes and scarves
for file in files:
	# TO DO: need to do LOTS of validation of input here!
	clothingitem = open(file).read().splitlines() #stackoverflow for reading file in and making each line entry in array
	# print(clothingitem[2])
	# DON'T use clothingdatabase = clothingdatabase.append(blah) because that returns none
	if (clothingitem[6] == "clean"):
		if (clothingitem[5] == season or clothingitem[5] == "seasonless"):
		    clothingdatabase.append(clothingitem)
		    print(len(clothingdatabase))
		    # TO DO need to handle edge case if you have no clean clothing, or no clothing for season
		    # add bottoms to array of possible bottoms
		    for type in bottomtypes:
		        if (clothingitem[0] == type):
		        	possiblebottoms.append(clothingitem)

print("Possible bottoms:")
for item in possiblebottoms:
    print(item)
#print(clothingdatabase[0][1])
print("That's all I can do right now, bye!")	

# TO DO: Generate three sample outfits (print them out)
# TO DO: Use Google AppEngine SDK and Google Appengine to put on web (see realpython article)
# TO DO: Implement js with localstorage for washed/not washed, have a "did laundry" button that sets everything to washed again
