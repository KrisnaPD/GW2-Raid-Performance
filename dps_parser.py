import requests
from collections import defaultdict

# Open list of logs. The list must be in the same directory as the script, and named input.txt
# The file can contain anything, as long as the log address is in a separate word.
with open("input.txt", encoding="utf8") as f:
    dps_report_addresses = f.read()

# Split string by newline and space, and filter the log addresses, then put it in a list.
logs = []
for x in dps_report_addresses.split():
    if "https://dps.report" in x:
        logs.append(x)

# Create empty dictionary to put players and performance later
players_total = defaultdict(lambda: defaultdict(int))

# Iterate over the list of logs, and parse each individual logs
for log in logs:

    # Use the getJson endpoint to get the JSON, and parse it to a Python dictionary
    log_json_address = "https://dps.report/getJson?permalink=" + log
    response = requests.get(log_json_address)
    log_json = response.json()

    # Iterate over all players. Add their performance to existing players, or create new players
    # if not.
    for i in range(len(log_json["players"])):

        player = log_json["players"][i]["account"]

        # Edge case for CA swords
        if player == "Conjured Sword":
            continue

        players_total[player]["down"] += log_json["players"][i]["defenses"][0]["downCount"]
        players_total[player]["dead"] += log_json["players"][i]["defenses"][0]["deadCount"]
        players_total[player]["res"] += log_json["players"][i]["support"][0]["resurrects"]
        players_total[player]["total_encounter"] += 1

        # Print who died where
        if log_json["players"][i]["defenses"][0]["deadCount"] > 0:
            print("%s died at %s" %(player, log_json["fightName"]))

# Convert dictionary to csv and write it to a file
csv_output = "Player ID, Down, Dead, Res, Total Encounter \n"

for player in players_total:
    csv_output += "%s, %d, %d, %d, %d \n" %(player, players_total[player]["down"], players_total[player]["dead"], players_total[player]["res"], players_total[player]["total_encounter"])

f = open("output.csv","w+")
f.write(csv_output)
f.close()