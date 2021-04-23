import json

# Choose a .json file you would like to look for points in (probably points.json)
with open('json/points.json') as f:
	data = json.load(f)

# New dictionary your selected points will go into
new_data = {}

# lcd_list = ["BAC_", "ACDIN."]

# Loops through all of the point names in the .json file
for key in data:
	# Choose a prefix (or prefixes) that you would like to search for in the larger json file (points.json)
	# You can also structure your search in some other way, not looking at the prefix - remember "key" is the point name
	if(key[0:2] == "MD" or key[0:11] == "MUSIC.DRAMA"):
		new_data[key] = data[key]

# Creates a .json file that inclides only the points you would like to import
# Puts the file in the json folder
with open("json/testPointJson_MusicAndDramaCen.json", "w") as outfile:  
    json.dump(new_data, outfile)