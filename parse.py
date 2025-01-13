import json
with open('data.json') as f:
    d = json.load(f)
    artist = d["artist"]
    name = d["name"]
    f = open("artist.txt", "w")
    f.write(artist)
    f.close()
    f = open("title.txt", "w")
    f.write(name)
    f.close()
