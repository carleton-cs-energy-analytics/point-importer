# Point-Importer
Used to import points from specific buildings to the database without re-importing everything. Follow the steps below to add a new building's points

## How to Add a New Building and its Points to the Database
1. Download point-importer folder from github (you can clone if you want, but make sure everything is working before pushing, or just don't push) and put it in your **home directory** on the server **(must be on the server to push info to the database)** - you will be working in here

2. Find the json file that matches the building you would like to add to the database and remember/write down the name for later

    1. It will be in /point-importer/json

    2. If it is not there, there are probably no siemens points in your building (or at least documented points)

    3. **Note:** the json files in energy-analytics-comps/data/csv_descriptions on the github are incomplete

    4. **If you want to make a new .json file**, see “How to make a new point json file” below

3. Build a decoder for your desired building by looking at former decoders and the point syntax for your building

    1. Former decoders are in /point-importer/decoders

        1. You can find information on what point abbreviations/encodings mean in these decoders

        2. **Make sure** you check that the names in the database *tags* table to ensure that you are tagging the points with the correct wording

            1. Example: use "Setpoint" instead of "Set Point"

    2. More info on point syntax can be found in energy-analytics-comps/data/csv_descriptions on the github:

        1. ‘PointDecoder.json’ OR ‘What the points are.txt’

    3. Put your new decoder in the **/point-importer/decoders** folder

4. Navigate to /point-importer/siemens_master.py

    1. In the get_points() method, change ‘with open('/json/points.json’)' (or whatever is in that spot) to (from step 2):
            
        ```python
        with open(‘/json/<yourJSONFileName>’)
        ```

    2. To the imports at the top, add:

        ```python
        from decoders.<your decoder file name without ‘.py’> import <your point decoder class>
        ```

        Example: 
        ```python
        from decoders.hulings_point_decoder import HulingsPointDecoder
        ```

        **Note:** If you are using a smart text editor/virtual environment (like VS Code, Atom, etc.), it might alert you that there are errors by putting “decoders.” at the beginning, but when your run the code it has to be there and will not throw errors

    3. In get_point_object() method set
    
        ```python
        building_decoder_class = <your point decoder class>
        ```

5. What you should have in your /point-importer folder by now:

    1. importer.py and a json folder with all of the old json files (these should already have been in the point-importer folder)

    2. A /decoders folder with all of the old decoders, point.py, and your new decoder (step 3)

    3. Changed siemens_master.py (step 4)

6. Run importer.py - **if there are errors, see below**

    1. There might be errors that come from the different data structures (or levels of data structures) used in all of the building testPointJson files

        1. For example, one testPointJson file might have a list of length one with a string inside that you would like to reference, but point_decoder.py references it like it is just a string

            ```python
            ["Point Name"] # instead of 
            "Point Name"
            ```
        
        2. Errors usually come up in point_decoder.py, since that point decoder is used for the decoding of all buildings

        3. These can be solved by going into point_decoder.py (or your new point decoder python file) and changing the exact references to match how the point names are structured your created json file

    2. As a rule of thumb, if you are getting weird errors coming from data structures, **check point_decoder.py** thoroughly to make sure that you are referencing everything correctly. The errors might not be coming from point_decoder.py in the error log, but they are probably rooted there.

7. Run the code once all errors have been solved

    1. Check the database to make sure your data has been uploaded

8. **If you run into errors in your code while partway through uploading data to the database** (importer.py will throw an error saying that you cannot upload duplicate points to the database), you must delete all of the points that you uploaded before the error before running importer.py again.
    1. This is because you cannot create duplicate points, and new points do not override old points - TODO???

    2. To do this, you can usually run a DELETE sql query on all points with point_id’s greater than a certain number, since new points will usually have the highest point_id’s

## How to Create a New Point json File:
1. All points are found in /point-importer/json/points.json

2. Extracting points from points.json can be done by running a script that looks for all keys that have that building’s code (EV for Evans, HU for Hulings, etc.) at the beginning of the point name
    
    1. **Note:** There can be multiple prefixes/codes for buildings and some are not delimited by commas, dashes, spaces, etc.
    
    2. See /point-importer/getPoints.py for an example script on how to extract the points you would like to import (this script puts the points into a json file)

    3. Look in energy-analytics-comps/data/csv-descriptions/PointDecoder.json for more info on how buildings are encoded

3. Edit the findPointNames.py if statements to match which points you would like to find

    1. There are some guidelines in that file’s comments on how to do it

    2. Test out which points your logic gets before you put anything into getPoints.py (it doesn't really matter but it's easier)

4. Put your if statement(s) that find all (and only) the correct points that are in your building into getPoints.py

5. **Important:** change the .json name of the output file to match what your fild should be named - **if you do not do this an old json file might be overwritten**

6. Run getPoints.py (you can run it again if you mess up and nothing bad will happen - just remember to delete your messed up .json file if you change the name)

7. You now have a json file to use to import points!
