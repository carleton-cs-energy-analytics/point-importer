# A script that finds all Point names in a certain .json file
# Use this to decode point names
import json

with open('json/points.json') as f1:
  points = json.load(f1)

# counts how many points match your statements
count = 0

# Loop through all of the keys (point names) and get different types of point names
# by separating them out into like-groups so they are easier to decode
for key in points:
    if(key[0:2] == "MD" or key[0:11] == "MUSIC.DRAMA"): # or key[0:2] == "WT") and key[0:5] != "WAREH" and key[0:5] != "WATER"):
        count += 1
        print(key) # prints out each point name that matches your search - useful for figuring out if your logic is correct

print(" ")
print("COUNT: " + str(count))


'''
split = key1.split(".")
last = split[len(split)-1]
# FOR CASSAT 4/14/2021 (you can probably delete this if you're seeing it)

room = False
split = key1.split(".")
if(len(split)==4):
    whole = split[2]
    if(whole[1].isdigit()):
        room = True
    
if(len(split) == 3):
    whole = split[1]
    if(len(whole)>3):
        if(whole[1].isdigit() and whole[2].isdigit() and whole[3].isdigit()):
            room = True
if(split[1][0].isdigit() or split[1] == "BASEMENT"):
    if(split[1] == "BASEMENT"):
        room = True
    else:
        room = True
if(split[1][0:2]=="RM"):
    room = True

if(room == True):
    if(last not in new and last not in tried):
        new.append(last)

if(room == False):
    print(key1)
'''