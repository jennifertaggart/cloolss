# CLothing Organizer/Optimizer Logical Style System

This code is in pre-beta, and is primarily a vehicle for learning more Python. 
CLOOLSS reads in formatted data files of clothing items and gets user input 
on daily temperature, then prints out outfits as a Python list. CLOOLSS does 
some testing of the clothing data files for properly formatted input. It 
checks if each item is clean and in season before adding the item to an 
appropriate Python list. Right now, CLOOLSS color matches a randomly chosen 
bottom (ie pants, shorts, skirt) with a top (making an exception for a list 
of neutral colors) and adds a random accessory and a random pair of shoes. 
(It just adds a random accessory and shoes to dresses, with no matching 
attempts.) Then it tests the estimated clo (amount of insulation) provided by 
the outfit against estimated "summer" and "winter" clo values. CLOOLSS does 
not do layering yet.

## Usage
CLOOLSS is run with the Python interpreter. It is written in Python 3. The 
structured data files describing your clothing should live in the same 
directory as the script, should have a .txt extension, and should be 
structured as follows:
* Line 1: shirt OR shorts OR pants OR skirt OR dress OR scarf OR shoes
* Line 2: Python list containing all the colors that describe the clothing item
* Line 3: close-fitting OR loose-fitting (program does not use this data yet)
* Line 4: Sleeve length, as a number from 0 to 1
* Line 5: fabric (program does not use this data yet)
* Line 6: rainy season OR dry season
* Line 7: clean OR wash
* Line 8: estimated clo, where 1 clo is the warmth provided by a men's business 
  suit at room temperature.

Example - file floralshell.txt contains:<br/>
 shirt<br/>
 ['black', 'white', 'pink', 'sea green', 'light green', 'dark green', 'yellow', 'greenish brown']<br/>
 loose-fitting<br/>
 0<br/>
 rayon<br/>
 dry season<br/>
 clean<br/>
 0.08<br/>

## Authors and Credits

Author: Jennifer Taggart

cloolss.py pays homage to the outfit-selecting opening scene of a similarly-named
teen movie from 1995 

I cribbed a lot of the clo values from this paper:
http://www.cbe.berkeley.edu/research/other-papers/McCullough%20-%20Wyon%201983%20Insulation%20characteristics%20of%20winter%20and%20summer%20indoor%20clothing.pdf

## License

Still researching this!