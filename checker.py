import requests
import os

valid = 0
invalid = 0
with open("tokens.txt") as f:
    for line in f:
        os.system('cls')
        print("Valid: " + str(valid) + "\nInvalid: " + str(invalid))
        token = line.strip("\n")
        if requests.get("https://discordapp.com/api/v6/users/@me/library", headers={'Content-Type': 'application/json', 'authorization': token}).status_code == 200:
            valid += 1
            file = open("hits.txt", "a").write(token + "\n")
        else:
            invalid += 1