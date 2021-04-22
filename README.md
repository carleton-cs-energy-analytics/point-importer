# Point-Importer
Used to import points from specific buildings to the database without re-importing everything. Follow the steps below to add a new building's points

1. Download point-analysis folder from github (you can clone if you want, but make sure everything is working before pushing) and put it in your home directory on the server (must be on the server to push info to the database) - you will be working in here

2. Find the json file that matches the building you would like to add to the database and remember/write down the name for later
    b. It will be in point-analysis/point-importer/json
    c. If it is not there, there are probably no siemens points matching your building
    Note: the json files in energy-analytics-comps/data/csv_descriptions on the github are incomplete
    If you want to make a new .json file, see “How to make a new point json file” below

3. Build a decoder for your desired building by looking at former decoders and the point syntax for your building
    a. Former decoders are in /point-analysis/point_importer/decoders
        i. You can find information on what point abbreviations/encodings mean in these decoders
    b. More info on point syntax can be found in energy-analytics-comps/data/csv_descriptions on the github:
        i. ‘PointDecoder.json’ OR ‘What the points are.txt’
    c. Put your new decoder in the /point-analysis/point_importer/decoders folder
3. Navigate to /point-analysis/point_importer/siemens_master.py
    a. In the get_points() method, change ‘./data/points.json’ (or whatever is in that spot) to ‘<yourJSONFileName>’ (from step 2)
    b. To the imports at the top, add:
“from decoders.<your decoder file name without ‘.py’> import <your point decoder class>
Ex: “from decoders.hulings_point_decoder import HulingsPointDecoder”
If you are using a smart text editor/virtual environment (like VS Code, Atom, etc.), it might alert you that there are errors by putting “decoders.” at the beginning, but when your run the code it has to be there and will not throw errors
In get_point_object() set building_decoder_class = <your point deoder class> (In the place of CassatPointDecoder below)

What you should have in your /point-analysis/point_importer folder by now:
importer.py and a json folder with all of the old json files (these should already have been in the point_importer folder)
A decoders folder with all of the old decoders, point.py, and your new decoder (step 3)
Changed siemens_master.py (step 4)
Run importer.py - if there are errors, see below
There might be errors that come from the different data structures (or levels of data structures) used in all of the building testPointJson files
For example, one testPointJson file might have a list of length one with a string inside that you would like to reference, but point_decoder.py references it like it is just a string
They usually come up in point_decoder.py, since that point decoder is used for the decoding of all buildings
These can be solved by going into point_decoder.py (or your new point decoder python file) and changing the exact references to match how the point names are structured your created json file
As a rule of thumb, if you are getting weird errors coming from data structures, check point_decoder.py thoroughly to make sure that you are referencing everything correctly. The errors might not be coming from point_decoder.py in the error log, but they are probably rooted there.
Run the code once all errors have been solved
Check the database to make sure your data has been uploaded
If you run into errors in your code while partway through uploading data to the database (importer.py will throw an error saying that you cannot upload duplicate points to the database), you must delete all of the points that you uploaded before the error before running importer.py again.
This is because you cannot create duplicate points, and new points do not override old points - TODO???
To do this, you can usually run a DELETE sql query on all points with point_id’s greater than a certain number, since new points will usually have the highest point_id’s




##  Updating due to Changed Point Definitions
This should be very infrequent, only occurring when renovations or new construction occurs.
In this case, we need to update points.json. 
1.  Update definition files in siemens-point-descriptions with the new definitions
2. run `python3 analysis-tools/definitions2json.py`
## Updating point name acronyms
We have only decoded the device acronyms within Boliou and Evans. <a href="https://www.downloads.siemens.com/download-center/Download.aspx?pos=download&fct=getasset&id1=A6V10435967">Siemens documentation</a> is a useful resource to refer to while creating more mappings between device acronyms and actual device names.


## Importing Points to DB
Every time the decoders are updated, the importer needs to be run again. 
1. from the backend repo, run the `drop.sql`, `schema.sql`, and `seed.sql` scripts in the `migrations` directory (in that order). 
2. run `python3 importers/importer.py`

Note: if importing to the production DB, the `DATABASE_HOST`, `DATABASE_NAME`, `DATABASE_USER`, and `DATABASE_PASSWORD`
environment variables will have to be set. If not set, it defaults to the local database.

## Project Structure & Making Decoder Changes
#### siemens_master
This script contains the master decoding function which reads info from `points.json`, 
and creates point objects using the correct decoder for each point. This function is called
from the importer.

#### Decoders
all of the `*point_decoder.py` files contain classes that are collections of static methods that
decode different aspects of a point. They all inherit from `point_decoder.py`, which acts as a 
general decoder for things that are consistent across buildings. Right now, we have a decoder for each 
building, and one "override_point_decoder" for points we want to decode seperate from their building. This
hierarchy could be extended one level deeper if we find out that, for example, in some building there are two 
general trends for decoding certain atrributes of a point. 

### Importer 
The script that gets decoded point objects from siemens_master, and imports them to the database.

### Tests
These are not true unit tests. They don't tests specific methods. Instead, they are more like end-to-end tests of 
the entire decoding process. They run the decoders, then test that all the points conform to 
things that should be true. For example, "all points have a point name" etc.
