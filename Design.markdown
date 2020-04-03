### Spec
The idea is to automatically download and parse the important data from dps.report and save it as variables.

For now, these variables will be exported into an .csv file and treated by excel. It's possible in the future that the data would automatically be treated. 

### High Level Design

# JSON Extraction
1) Input a dps.report URL
2) Modify the URL to the get JSON endpoint
3) Download the JSON and parse it (probably using request and json libraries)

# JSON Conversion
1) Find relevant data (res count, down count, death count, DPS ranking) and match it to the player. This is the hard bit - we gotta parse the JSON correctly. 
2) Create a struct for a player, if player did not exist yet. Probably dictionary with key-value pair for value and name. 
3) Fill the struct with the relevant data.
4) For each dps.report URL, increment the struct with the number from that pull.

# Export to Excel
1) Set an empty excel template for this.
2) For each player, export the value of the dictionary to the relevant column. 
3) Let excel do the processing. 

# Testing
1) Make sure the number is actually correct - some logs might have a JSON structured differently. Shouldn't, but hey.
2) And that we can access the values neatly. Print the dictionary out ideally.
3) And that it's able to match values to accounts.
4) Print the total, then see if it matches in excel.