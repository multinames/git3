import json

filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding="latin1")
player1 = {
    "PlayerName": "Donald Trump",
    "Score": 345,
    "awards": ["OR", "NV", "NY"]
}

player2 = {
    "PlayerName": "Clinton Hilary",
    "Score": 346,
    "awards": ["WT", "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ------------------------------------------------- SAVE by Jnson-------------------

json.dump(myplayers, myfile)
myfile.close()
