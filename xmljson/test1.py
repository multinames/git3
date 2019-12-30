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

#--------------------------------------------------LOAD by Json

myfile = open(filename, mode='r', encoding="latin1")
jason_data = json.load(myfile)

for user in jason_data:
    print("Player name is: " +str(user["PlayerName"]))
    print("Player Score is: " +str(user["Score"]))
    print("Player Award N1: " + str(user["awards"][0]))
    print("Player Award N2: " + str(user["awards"][1]))
    print("Player Award N3: " + str(user["awards"][2]))
    print("-------------------------------------------")