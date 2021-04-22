import json

# Choose a .json file you would like to look for points in
with open('json/points.json') as f:
	data = json.load(f)

# New dictionary to put your selected points into
new_data = {}

# lcd_list = ["BAC_", "ACDIN."]

# Loops through all of the point names in the .json file
for key in data:
	# Choose a prefix that you would like to search for in the larger json file
	# You can also structure your search in some other way, not looking at the prefix - remember key is the point name
	
	# building = key.split(".")[0]
	# building2 = key.split("-")[0]
	if(key[0:2] == "MD" or key[0:11] == "MUSIC.DRAMA"):
		new_data[key] = data[key]

# Creates a .json file that inclides only the points you would like to import
# Puts the file in the json folder
with open("json/testPointJson_MusicAndDramaCenter.json", "w") as outfile:  
    json.dump(new_data, outfile)